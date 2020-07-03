import datetime
import functools
import json
import os
import tkinter as tk
import webbrowser
from datetime import timedelta
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import matplotlib as mpl
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.ticker import StrMethodFormatter

import eia_data.commodity_prices as prices
import petrolpy_equations.petrolpy_equations as petrolpy

json_dark = open(r"themes\\dark_vscode.json", "r")
json_dark_data = json.loads(json_dark.read())
json_dark.close()
json_light = open(r"themes\\light_vscode.json", "r")
json_light_data = json.loads(json_light.read())
json_light.close()

DARK_THEME = json_dark_data.get("settings")
LIGHT_THEME = json_light_data.get("settings")

mpl.use("TkAgg")
LARGE_FONT = ("Verdana", 16)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

black_25 = "#404040"
black_30 = "#4d4d4d"
black_50 = "#808080"
blue_70 = "#6666ff"
blue_90 = "#ccccff"
grey_90 = "#e6e6e6"


class Application(tk.Tk):
    """Main Application used as root tkinter window"""

    # The notebook pattern will be used to organize frames

    def __init__(self):

        tk.Tk.__init__(self)

        tk.Tk.iconbitmap(
            self, default=r"icon\\app_colored_bottle.ico",
        )
        tk.Tk.wm_title(self, "PetroAlchemy - Petrolpy Application")

        self.main_style = ttk.Style()
        self.main_style.theme_create(
            "dark", parent="clam", settings=DARK_THEME,
        )
        self.main_style.theme_create(
            "light", parent="clam", settings=LIGHT_THEME,
        )

        self.main_style.theme_use("clam")
        themes = (
            "default",
            "dark",
            "light",
        )

        self.plot_style = "bmh"
        plot_styles = ("bmh", "seaborn-whitegrid", "ggplot", "fivethirtyeight")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Application variables

        self.well_list = []
        self.well_dataframes_dict = {}
        self.well_selected = tk.StringVar()
        self.well_selected_label = tk.StringVar()
        self.well_selected_label.set("No well has been selected")

        self.decline_curves_dict = {}
        self.oil_curves = []
        self.gas_curves = []

        self.curve_phase = tk.StringVar()
        self.curve_start_date = tk.StringVar()
        self.curve_qi = tk.IntVar()
        self.curve_di_secant = tk.DoubleVar()
        self.curve_b_factor = tk.DoubleVar()
        self.curve_min_decline = tk.DoubleVar()
        self.curve_name = tk.StringVar()

        # Edit menubar for Application

        menubar = tk.Menu(container)
        menu_file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menu_file)

        menu_file.add_command(
            label="Import Production", command=lambda: self.import_data()
        )
        menu_file.add_command(
            label="Save Cashflow",
            command=lambda: self.children["!frame"]
            .children["!cashflowinputpage"]
            .save_cashflow(),
        )

        menu_theme = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=menu_theme)

        menubar.add_command(label="Help", command=lambda: self.help_docs())
        menubar.add_command(label="Give Feedback", command=lambda: self.feedback_link())

        """ menu_plot_style = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Plot Style", menu=menu_plot_style) """

        # For loop to add themes to menubard and bind command to theme update

        for theme in themes:
            menu_theme.add_command(
                label=theme, command=lambda theme=theme: self.update_theme(theme)
            )

        # For loop to add styles to menubard and bind command to style update

        """ for style in plot_styles:
            menu_plot_style.add_command(
                label=style, command=lambda style=style: self.update_plot_style(style)
            ) """

        tk.Tk.config(self, menu=menubar)

        # Create notebook object and attach to container

        notebook = ttk.Notebook(container)
        notebook.grid(
            row=0, column=0, sticky="NESW", rowspan=4, columnspan=4, padx=1, pady=1
        )
        notebook.enable_traversal()

        # Add tabs to notebook

        home_page = HomePage(container, self)
        notebook.add(home_page, text="Home Page")

        plot_page = PlotPage(container, self)
        notebook.add(plot_page, text="Production Plot")

        cashflow_input_page = CashflowInputPage(container, self)
        notebook.add(cashflow_input_page, text="Cashflow Inputs")

        cashflow_output_page = CashflowOutputPage(container, self)
        notebook.add(cashflow_output_page, text="Cashflow Output")

        # Add status bar label for current well selected at the bottom of the application window

        label_status_bar = ttk.Label(
            container,
            textvariable=self.well_selected_label,
            font=SMALL_FONT,
            background=blue_70,
            foreground="white",
        )
        label_status_bar.grid(row=4, column=0, sticky="SWE", rowspan=1, columnspan=4)

        # Add keyboard shortcuts to go to previous or next well in list

        self.bind("<Control-f>", self.prev_well)
        self.bind("<Control-j>", self.next_well)

    def prev_well(self, event):
        """Change current well to previous well in list"""

        current_well = (
            self.children["!frame"].children["!homepage"].combobox_well_select.get()
        )
        current_index = self.well_list.index(current_well)

        prev_well = self.well_list[current_index - 1]
        self.children["!frame"].children["!homepage"].combobox_well_select.set(
            prev_well
        )
        self.children["!frame"].children[
            "!homepage"
        ].combobox_well_select.event_generate("<<ComboboxSelected>>")

    def next_well(self, event):
        """Change current well to next well in list"""

        current_well = (
            self.children["!frame"].children["!homepage"].combobox_well_select.get()
        )
        current_index = self.well_list.index(current_well)

        next_well = self.well_list[current_index + 1]
        self.children["!frame"].children["!homepage"].combobox_well_select.set(
            next_well
        )
        self.children["!frame"].children[
            "!homepage"
        ].combobox_well_select.event_generate("<<ComboboxSelected>>")

    def help_docs(self):
        """Open read the docs website"""

        webbrowser.open("https://petroalchemy.readthedocs.io/en/latest/?badge=latest")

    def feedback_link(self):
        """Open survey link"""

        webbrowser.open("https://www.surveymonkey.com/r/F22RYZ5")

    def import_data(self):
        """Select file to import into dataframe"""

        try:
            fnames = filedialog.askopenfilenames(initialdir=os.getcwd())

            for fname in fnames:
                file_type = Path(fname).suffix

                if file_type == (".xlsx" or ".xls"):
                    df = pd.read_excel(fname, parse_dates=True)

                elif file_type == (".csv"):
                    df = pd.read_csv(fname, parse_dates=["Date"])

                df.columns = map(str.lower, df.columns)

                # CSV doesn't always parse dates correctly

                df.date = [time.date() for time in df.date]

                well_names = df["well name"].unique().tolist()

                num_wells = len(well_names)

                for well_name in well_names:

                    well_name = str(well_name)

                    if well_name not in self.well_list:

                        self.well_list.append(well_name)

                        dict_well_name = well_name.replace(" ", "_")
                        self.well_dataframes_dict[dict_well_name] = df.loc[
                            df["well name"] == well_name
                        ]

                        if num_wells == 1:

                            messagebox.showinfo(
                                "Import Finished", f"{well_name} has been added"
                            )

                    else:
                        messagebox.showinfo(
                            "Import Failed",
                            f"{well_name} already exists, check the file and try again",
                        )

            if num_wells > 1:

                messagebox.showinfo(
                    "Import Finished", f"{num_wells} wells have been added"
                )

        except:
            messagebox.showinfo(
                "Import Failed",
                "The data is in the wrong format, try again. If using csv try excel instead.",
            )

        self.children["!frame"].children["!homepage"].combobox_well_select[
            "state"
        ] = "normal"
        self.children["!frame"].children["!homepage"].combobox_well_select.set(
            well_names[0]
        )
        self.children["!frame"].children["!plotpage"].combobox_curve_start_date.set(
            df["date"][0]
        )
        self.children["!frame"].children[
            "!cashflowinputpage"
        ].combobox_forecast_date.set(df["date"][0])
        self.children["!frame"].children[
            "!homepage"
        ].combobox_well_select.event_generate("<<ComboboxSelected>>")

    def update_theme(self, theme):
        """Sets application theme/style"""
        if theme == "default":
            theme = "clam"

        self.main_style.theme_use(theme)

    def update_plot_style(self, style):
        """Sets plot style"""
        self.plot_style = style
        self.children["!frame"].children[
            "!homepage"
        ].combobox_well_select.event_generate("<<ComboboxSelected>>")


class HomePage(ttk.Frame):
    """Page to display when program opens"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        welcome_text = "Welcome, you need to import well data to get started. \n\nUse at your own discretion.\n\nThis application is open source to provide useful software to engineers, \nbut is not a replacement for business critical reserve software."

        label_welcome = ttk.Label(self, text=welcome_text, font=LARGE_FONT,)
        label_welcome.grid(column=1, row=1, columnspan=4, rowspan=1, pady=10, padx=10)

        button_import_data = ttk.Button(
            self, text="Import Well Data", command=controller.import_data
        )
        button_import_data.grid(
            column=1, row=2, sticky="W", columnspan=1, rowspan=1, pady=10, padx=10
        )

        self.label_current_well = ttk.Label(
            self, textvariable=controller.well_selected_label, font=LARGE_FONT
        )
        self.label_current_well.grid(
            column=1, row=3, sticky="W", columnspan=1, rowspan=1, pady=10, padx=10
        )

        self.combobox_well_select = ttk.Combobox(
            self, postcommand=self.update_combobox_well_select, state="disabled"
        )
        self.combobox_well_select.grid(
            column=1, row=4, sticky="W", columnspan=1, rowspan=4, pady=10, padx=10
        )
        self.combobox_well_select.bind(
            "<<ComboboxSelected>>", self.update_well_selected
        )

    def update_combobox_well_select(self):
        """Update combobox with current well_list"""

        self.combobox_well_select["values"] = self.controller.well_list

    def update_well_selected(self, event):
        """Callback to update current well_selected. Updates data table and production plot."""

        well_name = self.combobox_well_select.get()
        dict_well_name = str(well_name).replace(" ", "_")

        self.controller.well_selected.set(dict_well_name)
        self.controller.well_selected_label.set(f"Well selected: {well_name}")

        df_selected = self.controller.well_dataframes_dict.get(f"{dict_well_name}")

        plot_page = self.controller.children["!frame"].children["!plotpage"]

        plot_page.combobox_curve_selected.set(f"{well_name} Oil Curve")

        # set plot widgets with oil early max

        plot_page.spinbox_qi.set(int(df_selected.oil[:6].max()))
        max_id = df_selected.oil[:6].idxmax()
        di_estimate_float = (
            df_selected["oil"][max_id] - df_selected["oil"][max_id + 12]
        ) / df_selected["oil"][max_id]
        di_estimate_pct = round(di_estimate_float * 100, 2)
        plot_page.spinbox_di.set(di_estimate_pct)

        # Plot chart

        self.controller.children["!frame"].children["!plotpage"].reset_plot(init=True)

        plot_page.update_widgets()


class PlotPage(ttk.Frame):
    """Frame to hold canvas plot of production"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(
            row=0, column=0, sticky="NESW", rowspan=4, columnspan=4, padx=1, pady=1
        )

        # PlotPage variables

        self.curve_selected = tk.StringVar()

        # Label Frame for decline curve parameters

        frame_widgets = ttk.Labelframe(
            self,
            labelanchor="n",
            text="Decline Curve Analysis",
            width=200,
            takefocus=True,
        )
        frame_widgets.pack(side="left", fill="y", padx=1, pady=1)

        # Set phase to analyze

        label_1 = ttk.Label(frame_widgets, text="Select Phase")
        label_1.pack()

        self.combobox_phase = ttk.Combobox(
            frame_widgets,
            width=5,
            justify=tk.CENTER,
            state="readonly",
            textvariable=controller.curve_phase,
        )
        self.combobox_phase["values"] = ("Oil", "Gas")
        self.combobox_phase.set("Oil")
        self.combobox_phase.bind("<<ComboboxSelected>>", self.update_phase_widgets)
        self.combobox_phase.pack()

        lable_2 = ttk.Label(frame_widgets, text="Select Units")
        lable_2.pack()

        self.combobox_units = ttk.Combobox(
            frame_widgets, width=15, justify=tk.CENTER, state="readonly",
        )
        self.combobox_units["values"] = ("BOPM/MCFPM", "BOPD/MCFPD")
        self.combobox_units.set("BOPM/MCFPM")
        self.combobox_units.bind("<<ComboboxSelected>>", self.update_axis_units)
        self.combobox_units.pack()

        # Select decline curve parameters

        label_3 = ttk.Label(frame_widgets, text="Start of Curve")
        label_3.pack()

        self.combobox_curve_start_date = ttk.Combobox(
            frame_widgets,
            width=10,
            justify=tk.CENTER,
            textvariable=controller.curve_start_date,
        )
        self.combobox_curve_start_date.pack()

        lable_4 = ttk.Label(frame_widgets, text="Initial Rate")
        lable_4.pack()

        self.spinbox_qi = ttk.Spinbox(
            frame_widgets,
            width=10,
            justify=tk.CENTER,
            from_=0,
            to=1_000_000,
            increment=1,
            textvariable=controller.curve_qi,
        )
        self.spinbox_qi.set(1_000)
        self.spinbox_qi.pack()

        lable_5 = ttk.Label(frame_widgets, text="Di (effective %), 1/yr")
        lable_5.pack()

        self.spinbox_di = ttk.Spinbox(
            frame_widgets,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.1,
            textvariable=controller.curve_di_secant,
        )
        self.spinbox_di.set(25.0)
        self.spinbox_di.pack()

        lable_6 = ttk.Label(frame_widgets, text="B Factor")
        lable_6.pack()

        self.spinbox_b_factor = ttk.Spinbox(
            frame_widgets,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=2,
            increment=0.01,
            textvariable=controller.curve_b_factor,
        )
        self.spinbox_b_factor.set(1.1)
        self.spinbox_b_factor.pack()

        lable_7 = ttk.Label(frame_widgets, text="Min. Decline (effective %), 1/yr")
        lable_7.pack()

        self.spinbox_min_decline = ttk.Spinbox(
            frame_widgets,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=1,
            textvariable=controller.curve_min_decline,
        )
        self.spinbox_min_decline.set(6.0)
        self.spinbox_min_decline.pack()

        # Select Curves and modify them

        lable_8 = ttk.Label(frame_widgets, text="Enter/Select Curve Name")
        lable_8.pack(pady=5)

        self.combobox_curve_selected = ttk.Combobox(
            frame_widgets, justify=tk.CENTER, textvariable=self.curve_selected,
        )
        self.combobox_curve_selected.bind(
            "<<ComboboxSelected>>", self.update_curve_selected
        )
        self.combobox_curve_selected.set("Oil Curve Name")
        self.combobox_curve_selected.pack()

        # Create/Update Decline Curve Button

        self.button_create_dc = ttk.Button(
            frame_widgets,
            width=30,
            text="Create/Update Decline Curve",
            command=self.create_dc,
        )
        self.button_create_dc.pack(pady=5, padx=2)

        # Reset plot to remove curves

        self.button_reset_curve = ttk.Button(
            frame_widgets,
            width=30,
            text="Remove Decline Curves",
            command=self.reset_plot,
        )
        self.button_reset_curve.pack(pady=5, padx=2)

        # Plot selected curve

        self.button_plot_curve = ttk.Button(
            frame_widgets, width=30, text="Plot Selected Curve", command=self.plot_curve
        )
        self.button_plot_curve.pack(pady=5, padx=2)

        # Delete curve selected button

        self.button_delete_curve = ttk.Button(
            frame_widgets,
            width=30,
            text="Delete Selected Curve",
            command=self.delete_curve,
        )
        self.button_delete_curve.pack(pady=5, padx=2)

        # Canvas used for plotting

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()

    def update_widgets(self):
        df = self.controller.well_dataframes_dict.get(
            self.controller.well_selected.get()
        )
        self.combobox_curve_start_date["values"] = df.date.tolist()
        self.controller.children["!frame"].children[
            "!cashflowinputpage"
        ].combobox_forecast_date["values"] = df.date.tolist()

    def update_combobox_curve_select(self):
        """Update combobox with current curve list"""

        self.combobox_curve_selected["values"] = list(
            self.controller.decline_curves_dict.keys()
        )

    def update_curve_selected(self, event=None):
        """Callback to update current curve selected and comboboxes on cashflow tab"""

        curve_name = self.combobox_curve_selected.get()
        self.curve_selected.set(curve_name)
        self.combobox_curve_selected.set(curve_name)

        self.controller.children["!frame"].children[
            "!cashflowinputpage"
        ].combobox_oil_curve["values"] = self.controller.oil_curves
        self.controller.children["!frame"].children[
            "!cashflowinputpage"
        ].combobox_gas_curve["values"] = self.controller.gas_curves

        if curve_name in self.controller.oil_curves:
            self.combobox_phase.set("Oil")
        else:
            self.combobox_phase.set("Gas")

        self.update_phase_widgets(init=False)

    def update_axis_units(self, event=None):
        """Callback to add units label to axis"""

        units = self.combobox_units.get()
        self.ax.set_ylabel(units)
        self.canvas.draw()

    def update_phase_widgets(self, event=None, init=True):
        """Callback to update max rate and di for phase"""

        well_name = (
            self.controller.children["!frame"]
            .children["!homepage"]
            .combobox_well_select.get()
        )
        dict_well_name = str(well_name).replace(" ", "_")

        df_selected = self.controller.well_dataframes_dict.get(f"{dict_well_name}")

        curve_phase = self.combobox_phase.get()

        if init:
            self.combobox_curve_selected.set(f"{well_name} {curve_phase} Curve")

        curve_phase = curve_phase.lower()

        self.spinbox_qi.set(df_selected[curve_phase][:6].max())
        max_id = df_selected[curve_phase][:6].idxmax()
        di_estimate_float = (
            df_selected[curve_phase][max_id] - df_selected[curve_phase][max_id + 12]
        ) / df_selected[curve_phase][max_id]
        di_estimate_pct = round(di_estimate_float * 100, 2)
        self.spinbox_di.set(di_estimate_pct)

    def create_dc(self):
        """Creates decline curve from widget curve inputs"""

        if self.curve_selected.get() == "":
            messagebox.showerror("Error", "Enter a name for the curve")
            return

        curve_start_date = datetime.datetime.strptime(
            self.controller.curve_start_date.get(), "%Y-%m-%d"
        )

        months = pd.date_range(curve_start_date, periods=600, freq="M")

        # create days date range because months sets inital date to end of month

        delta_time_yrs = [(date - months[0]).days / 365 for date in months]

        df_curve = pd.DataFrame(
            zip(months, delta_time_yrs), columns=["months", "delta_time_yrs"]
        )

        di_secant = float(self.controller.curve_di_secant.get() / 100)
        b_factor = float(self.controller.curve_b_factor.get())
        min_decline = float(self.controller.curve_min_decline.get() / 100)
        qi = int(self.controller.curve_qi.get())
        curve_name = str(self.curve_selected.get())

        curve_phase = self.combobox_phase.get()

        if curve_phase == "Oil":
            if curve_name in self.controller.oil_curves:
                self.controller.oil_curves.remove(curve_name)
            self.controller.oil_curves.append(curve_name)
            self.controller.children["!frame"].children[
                "!cashflowinputpage"
            ].combobox_oil_curve.set(curve_name)
        else:
            if curve_name in self.controller.gas_curves:
                self.controller.gas_curves.remove(curve_name)
            self.controller.gas_curves.append(curve_name)
            self.controller.children["!frame"].children[
                "!cashflowinputpage"
            ].combobox_gas_curve.set(curve_name)

        nominal_di = petrolpy.convert_secant_di_to_nominal(di_secant, b_factor)

        df_curve[curve_name] = petrolpy.arps_decline_rate_q(
            qi, b_factor, nominal_di, delta_time_yrs, min_decline
        )

        self.delete_curve(curve_name)
        self.controller.decline_curves_dict[curve_name] = df_curve

        self.update_curve_selected()
        self.plot_curve(curve_name)

    def plot_curve(self, curve_name=None):

        if curve_name is None:
            curve_name = self.combobox_curve_selected.get()

        if self.combobox_phase.get() == "Oil":
            color = "g"
            units = "MBO"
            unit_factor = 1_000
        else:
            color = "r"
            units = "BCF"
            unit_factor = 1_000_000

        df_curve = self.controller.decline_curves_dict.get(curve_name)
        self.ax.plot(
            df_curve["months"],
            df_curve[curve_name],
            color,
            label=curve_name,
            linestyle="dashdot",
            linewidth=2,
        )
        self.ax.legend(
            bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0
        )

        # Technical EURs (MBO/BCF)

        eur_1_year = round(df_curve[curve_name][:11].sum() / unit_factor, 1)
        eur_5_year = round(df_curve[curve_name][:59].sum() / unit_factor, 1)
        eur_50_year = round(df_curve[curve_name][:599].sum() / unit_factor, 1)

        textstr = "\n".join(
            (
                f"{curve_name}",
                f"1 Year EUR: {eur_1_year:,} {units}",
                f"5 Year EUR: {eur_5_year:,} {units}",
                f"50 Year EUR: {eur_50_year:,} {units}",
            )
        )

        try:
            del self.ax.texts[-1]
        except:
            pass

        text_box_props = dict(boxstyle="round", facecolor="white")
        text_box = self.ax.text(
            0.85,
            0.95,
            textstr,
            transform=self.ax.transAxes,
            fontsize=10,
            verticalalignment="top",
            bbox=text_box_props,
        )

        self.canvas.draw()
        self.update_combobox_curve_select()

    def delete_curve(self, curve_name=None):

        if curve_name is None:
            curve_name = self.combobox_curve_selected.get()

        if curve_name in self.controller.decline_curves_dict:
            del self.controller.decline_curves_dict[curve_name]
            well_name = (
                self.controller.children["!frame"]
                .children["!homepage"]
                .combobox_well_select.get()
            )
            curve_phase = self.combobox_phase.get()
            self.combobox_curve_selected.set(f"{well_name} {curve_phase} Curve")
            self.update_combobox_curve_select()
            # self.reset_plot()

    def reset_plot(self, init=False):

        if init:
            self = self.controller.children["!frame"].children["!plotpage"]

        well_name = (
            self.controller.children["!frame"]
            .children["!homepage"]
            .combobox_well_select.get()
        )
        dict_well_name = str(well_name).replace(" ", "_")

        df_selected = self.controller.well_dataframes_dict.get(f"{dict_well_name}")

        fig = self.fig

        canvas = self.canvas

        ax = self.ax

        ax.clear()

        # plt.rcParams.update(plt.rcParamsDefault)
        plt.style.use(self.controller.plot_style)

        ax.plot(df_selected["date"], df_selected["oil"], "g", label="Oil", linewidth=2)
        ax.plot(df_selected["date"], df_selected["gas"], "r", label="Gas", linewidth=2)

        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
        ax.yaxis.set_minor_formatter(StrMethodFormatter("{x:,.0f}"))
        ax.tick_params(axis="y", which="major", labelsize=8)
        ax.tick_params(axis="y", which="minor", labelsize=6)
        ax.tick_params(axis="x", which="both", labelsize=8, labelcolor=blue_70)

        years = mdates.YearLocator()  # every year
        months = mdates.MonthLocator()  # every month
        x_format = mdates.DateFormatter("%m/%d/%Y")

        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(x_format)
        ax.xaxis.set_minor_locator(months)

        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax.grid(
            which="major",
            axis="x",
            color="grey",
            linestyle="--",
            linewidth=1,
            alpha=0.5,
        )
        ax.grid(
            which="both",
            axis="y",
            color="grey",
            linestyle="--",
            linewidth=1,
            alpha=0.5,
        )

        datemin = datetime.date(df_selected["date"].min().year, 1, 1)
        datemax = datetime.date(df_selected["date"].max().year + 1, 1, 1)
        ax.set_xlim(datemin, datemax)
        ax.set_ylim(ymin=10)

        fig.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.15)

        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)
        ax.set_title(f"{well_name}", fontsize=16)

        # Figure color
        # fig.set_facecolor(grey_90)

        # Plot background
        ax.set_facecolor(grey_90)

        self.update_axis_units()

        canvas.draw()


class CashflowInputPage(ttk.Frame):
    """Frame to hold cashflow input widgets"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(
            row=0, column=0, sticky="NESW", rowspan=4, columnspan=4, padx=1, pady=1
        )

        # Variable from widgets

        self.working_interest = tk.DoubleVar()
        self.net_revenue_interest = tk.DoubleVar()
        self.disc_rate = tk.DoubleVar()
        self.sev_tax_rate = tk.DoubleVar()
        self.spot_oil_price = tk.DoubleVar()
        self.spot_gas_price = tk.DoubleVar()
        self.oil_diff = tk.DoubleVar
        self.gas_diff = tk.DoubleVar()
        self.opex = tk.DoubleVar()
        self.capex = tk.DoubleVar()

        # Left side columns 0 and 1

        label_left_1 = ttk.Label(self, text="Decline Curve for Oil")
        label_left_1.grid(row=0, column=0, padx=20, pady=10)

        self.combobox_oil_curve = ttk.Combobox(
            self, width=30, justify=tk.CENTER, state="readonly"
        )
        self.combobox_oil_curve["values"] = self.controller.oil_curves
        self.combobox_oil_curve.grid(row=0, column=1, padx=20, pady=10)

        label_left_2 = ttk.Label(self, text="Decline Curve for Gas")
        label_left_2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_gas_curve = ttk.Combobox(
            self, width=30, justify=tk.CENTER, state="readonly"
        )
        self.combobox_gas_curve["values"] = self.controller.gas_curves
        self.combobox_gas_curve.grid(row=1, column=1, padx=20, pady=10)

        label_left_3 = ttk.Label(self, text="Enter/Select Beginning Forecast Date")
        label_left_3.grid(row=2, column=0, padx=20, pady=10)

        self.combobox_forecast_date = ttk.Combobox(self, width=30, justify=tk.CENTER,)
        self.combobox_forecast_date["values"] = self.controller.gas_curves
        self.combobox_forecast_date.grid(row=2, column=1, padx=20, pady=10)

        label_left_4 = ttk.Label(self, text="Enter/Select Working Interest %")
        label_left_4.grid(row=3, column=0, padx=20, pady=10)

        self.spinbox_working_interest = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.01,
            textvariable=self.working_interest,
        )
        self.spinbox_working_interest.set(100)
        self.spinbox_working_interest.grid(row=3, column=1, padx=20, pady=10)

        label_left_5 = ttk.Label(self, text="Enter/Select Net Revenue Interest %")
        label_left_5.grid(row=4, column=0, padx=20, pady=10)

        self.spinbox_net_revenue_interest = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.01,
            textvariable=self.net_revenue_interest,
        )
        self.spinbox_net_revenue_interest.set(75)
        self.spinbox_net_revenue_interest.grid(row=4, column=1, padx=20, pady=10)

        label_left_6 = ttk.Label(self, text="Primary Annual Discount Rate %")
        label_left_6.grid(row=5, column=0, padx=20, pady=10)

        self.spinbox_disc_rate = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=50,
            increment=1,
            textvariable=self.disc_rate,
        )
        self.spinbox_disc_rate.set(10)
        self.spinbox_disc_rate.grid(row=5, column=1, padx=20, pady=10)

        label_left_7 = ttk.Label(self, text="Severance Tax Rate %")
        label_left_7.grid(row=6, column=0, padx=20, pady=10)

        self.spinbox_sev_tax_rate = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=50,
            increment=1,
            textvariable=self.sev_tax_rate,
        )
        self.spinbox_sev_tax_rate.set(7)
        self.spinbox_sev_tax_rate.grid(row=6, column=1, padx=20, pady=10)

        # Right side columns 2 and 3

        # Get current futures prices for Nymex WTI and Natural Gas
        try:

            wti, nat_gas = prices.futures_prices()

        except:

            "Exception occurs if API key is blank or request error"

            wti, nat_gas = 50, 2.50

        label_right_1 = ttk.Label(self, text="Enter Oil Price ($/BBL)")
        label_right_1.grid(row=0, column=2, padx=20, pady=10)

        self.oil_price = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=1000,
            increment=0.01,
            textvariable=self.spot_oil_price,
        )
        self.oil_price.set(wti)
        self.oil_price.grid(row=0, column=3, padx=20, pady=10)

        label_right_2 = ttk.Label(self, text="Enter Gas Price ($/MCF)")
        label_right_2.grid(row=1, column=2, padx=20, pady=10)

        self.gas_price = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=1000,
            increment=0.01,
            textvariable=self.spot_gas_price,
        )
        self.gas_price.set(nat_gas)
        self.gas_price.grid(row=1, column=3, padx=20, pady=10)

        label_right_3 = ttk.Label(self, text="Enter Fixed Oil Differential ($/BBL)")
        label_right_3.grid(row=2, column=2, padx=20, pady=10)

        self.oil_diff = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.01,
            textvariable=self.oil_diff,
        )
        self.oil_diff.set(2.00)
        self.oil_diff.grid(row=2, column=3, padx=20, pady=10)

        label_right_4 = ttk.Label(self, text="Enter Fixed Gas Differential ($/MCF)")
        label_right_4.grid(row=3, column=2, padx=20, pady=10)

        self.gas_diff = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.01,
            textvariable=self.gas_diff,
        )
        self.gas_diff.set(0.50)
        self.gas_diff.grid(row=3, column=3, padx=20, pady=10)

        label_right_5 = ttk.Label(self, text="Enter OPEX ($/Month)")
        label_right_5.grid(row=4, column=2, padx=20, pady=10)

        self.opex = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100_000,
            increment=100,
            textvariable=self.opex,
        )
        self.opex.set(10_000)
        self.opex.grid(row=4, column=3, padx=20, pady=10)

        label_right_6 = ttk.Label(self, text="Enter CAPEX ($ Million)")
        label_right_6.grid(row=5, column=2, padx=20, pady=10)

        self.capex = ttk.Spinbox(
            self,
            width=5,
            justify=tk.CENTER,
            from_=0,
            to=100,
            increment=0.01,
            textvariable=self.capex,
        )
        self.capex.set(6.50)
        self.capex.grid(row=5, column=3, padx=20, pady=10)

        self.button_run_financials = ttk.Button(
            self, text="Run Financials", command=self.run_financials,
        )
        self.button_run_financials.grid(row=6, column=3, padx=20, pady=10)

        self.frame_output = ttk.Labelframe(
            self,
            labelanchor="n",
            text="Cashflow Run Outputs",
            width=800,
            takefocus=True,
        )
        self.frame_output.grid(row=7, column=0, columnspan=5, rowspan=5, pady=10)

        # Display area for summary calculations
        summary_column_names = ("Summary Result", "Value")

        self.treeview_summary = ttk.Treeview(self.frame_output)
        self.treeview_summary["columns"] = summary_column_names
        self.treeview_summary["show"] = "headings"
        self.treeview_summary["height"] = 6
        self.treeview_summary.heading(
            summary_column_names[0], text=summary_column_names[0]
        )
        self.treeview_summary.heading(
            summary_column_names[1], text=summary_column_names[1], anchor="center"
        )

        self.treeview_summary.grid(row=0, column=0, padx=5, pady=10)

        # Display area for discount rate calculations
        discount_column_names = ("Discount Rate", "Value")

        self.treeview_discount = ttk.Treeview(self.frame_output)
        self.treeview_discount["columns"] = discount_column_names
        self.treeview_discount["show"] = "headings"
        self.treeview_discount["height"] = 6
        self.treeview_discount.heading(
            discount_column_names[0], text=discount_column_names[0]
        )
        self.treeview_discount.heading(
            discount_column_names[1], text=discount_column_names[1], anchor="center"
        )

        self.treeview_discount.grid(row=0, column=1, padx=5, pady=10)

        # Display area for EUR values
        eur_column_names = ("EUR", "Value")

        self.treeview_eur = ttk.Treeview(self.frame_output)
        self.treeview_eur["columns"] = eur_column_names
        self.treeview_eur["show"] = "headings"
        self.treeview_eur["height"] = 3
        self.treeview_eur.heading(eur_column_names[0], text=eur_column_names[0])
        self.treeview_eur.heading(
            eur_column_names[1], text=eur_column_names[1], anchor="center"
        )

        self.treeview_eur.grid(row=0, column=2, padx=5, pady=10)

    def run_financials(self):
        """Get all cashflow inputs and run financials"""

        # get gross oil and gas curves

        oil_curve_name = self.combobox_oil_curve.get()
        gas_curve_name = self.combobox_gas_curve.get()

        df_oil = self.controller.decline_curves_dict.get(oil_curve_name)
        df_gas = self.controller.decline_curves_dict.get(gas_curve_name)

        delta_time_yrs = df_oil.delta_time_yrs.tolist()

        oil_curve = df_oil[oil_curve_name]
        gas_curve = df_gas[gas_curve_name]

        months = np.arange(1, 601)

        start_of_curve = pd.date_range(
            self.combobox_forecast_date.get(), periods=600, freq="M"
        )

        data = zip(months, start_of_curve, oil_curve, gas_curve, delta_time_yrs)

        df_cashflow = pd.DataFrame(
            data, columns=["Month", "Date", "Gross Oil", "Gross Gas", "delta_time_yrs"]
        )

        # create net volumes

        net_interest = float(self.net_revenue_interest.get()) / 100

        df_cashflow["Net Oil"] = df_cashflow["Gross Oil"] * net_interest
        df_cashflow["Net Gas"] = df_cashflow["Gross Gas"] * net_interest

        # display oil and gas prices

        spot_oil_price = float(self.oil_price.get())
        spot_gas_price = float(self.gas_price.get())

        oil_diff = float(self.oil_diff.get())
        gas_diff = float(self.gas_diff.get())

        net_oil_price = spot_oil_price - oil_diff
        net_gas_price = spot_gas_price - gas_diff

        df_cashflow["Spot Oil Price ($/BBL)"] = spot_oil_price
        df_cashflow["Spot Gas Price ($/MCF)"] = spot_gas_price

        df_cashflow["Net Oil Price ($/BBL)"] = net_oil_price
        df_cashflow["Net Gas Price ($/MCF)"] = net_gas_price

        # Revenues

        df_cashflow["Net Oil Revenue (M$)"] = (
            df_cashflow["Net Oil"] * df_cashflow["Net Oil Price ($/BBL)"] / 1000
        )
        df_cashflow["Net Gas Revenue (M$)"] = (
            df_cashflow["Net Gas"] * df_cashflow["Net Gas Price ($/MCF)"] / 1000
        )
        df_cashflow["Net Operating Revenue (M$)"] = (
            df_cashflow["Net Oil Revenue (M$)"] + df_cashflow["Net Gas Revenue (M$)"]
        )

        # Taxes, OPEX, and CAPEX

        sev_tax_rate = float(self.sev_tax_rate.get()) / 100
        opex = float(self.opex.get())
        capex = float(self.capex.get())

        df_cashflow["Severance Taxes (M$)"] = (
            df_cashflow["Net Operating Revenue (M$)"] * sev_tax_rate
        )
        df_cashflow["OPEX (M$)"] = opex / 1000
        df_cashflow["CAPEX (M$)"] = capex * 1000
        df_cashflow["CAPEX (M$)"][1:] = 0

        # Net Revenue and Cumulative Net Revenue

        df_cashflow["Net Revenue (M$)"] = (
            df_cashflow["Net Operating Revenue (M$)"]
            - df_cashflow["Severance Taxes (M$)"]
            - df_cashflow["OPEX (M$)"]
            - df_cashflow["CAPEX (M$)"]
        )
        df_cashflow["Cumulative Net Revenue (M$)"] = df_cashflow[
            "Net Revenue (M$)"
        ].cumsum()

        # Discounted values

        ann_disc_rate = float(self.disc_rate.get()) / 100

        monthly_disc_rate = petrolpy.ann_to_monthly_disc_rate(ann_disc_rate)

        df_cashflow["Discounted Net Revenue (M$)"] = df_cashflow["Net Revenue (M$)"] * (
            1 / ((1 + monthly_disc_rate) ** (df_cashflow["Month"] - 1))
        )
        df_cashflow["Cumulative Discounted Net Revenue (M$)"] = df_cashflow[
            "Discounted Net Revenue (M$)"
        ].cumsum()

        npv_rate = df_cashflow["Discounted Net Revenue (M$)"].sum()

        # Store current cashflow dataframe to class

        self.df_cashflow = df_cashflow

        # Annual Net Revenue

        ann_net_revenue = (
            df_cashflow["Net Revenue (M$)"].groupby(df_cashflow.index // 12).sum()
        )

        # Summary Values

        # Economic Life cutoff

        try:
            econ_life_years = round(
                float(
                    (df_cashflow[df_cashflow["Net Revenue (M$)"] > 0].index[-1] + 1)
                    / 12
                ),
                1,
            )
        except IndexError:
            # Error ocurrs when Net Revenue is never positive
            econ_life_years = 0

        # IRR, ROI, DROI as %

        irr_annual = petrolpy.irr(df_cashflow["Net Revenue (M$)"], monthly=True)

        roi = df_cashflow["Net Revenue (M$)"].sum() / (capex * 1000)
        dcf_roi = npv_rate / (capex * 1000)

        # NPV8, NPV10, NPV15, NPV20, NPV25, NPV30

        rates = [8, 10, 15, 20, 25, 30]
        npv_data = []
        npv_values = []

        for rate in rates:

            monthly_disc_rate = petrolpy.ann_to_monthly_disc_rate(rate / 100)

            df_cashflow[f"NPV{rate} (M$)"] = df_cashflow["Net Revenue (M$)"] * (
                1 / ((1 + monthly_disc_rate) ** (df_cashflow["Month"] - 1))
            )
            npv_sum = df_cashflow[f"NPV{rate} (M$)"].sum()
            npv_data.append((f"NPV{rate}", f"{npv_sum:,.0f} M$"))
            npv_values.append(npv_sum)

        # Payout

        try:
            payout_years = round(
                float(
                    (
                        df_cashflow[
                            df_cashflow["Cumulative Net Revenue (M$)"] > 0
                        ].index[0]
                        + 1
                    )
                    / 12
                ),
                1,
            )

        except IndexError:
            # Error ocurrs when Cumulative Net Revenue is never positive
            payout_years = "Infinite"

        # 1 year EUR, 50 (600 months) year EUR, 5 (60 months) year EUR

        oil_eur_1 = int(df_cashflow["Gross Oil"][:11].sum() / 1_000)
        oil_eur_5 = int(df_cashflow["Gross Oil"][:59].sum() / 1_000)
        oil_eur_50 = int(df_cashflow["Gross Oil"][:599].sum() / 1_000)

        gas_eur_1 = round(df_cashflow["Gross Gas"][:11].sum() / 1_000_000, 1)
        gas_eur_5 = round(df_cashflow["Gross Gas"][:59].sum() / 1_000_000, 1)
        gas_eur_50 = round(df_cashflow["Gross Gas"][:599].sum() / 1_000_000, 1)

        eur_data = (
            ("1 Year EUR", f"{oil_eur_1:,} MBO & {gas_eur_1} BCF"),
            ("5 Year EUR", f"{oil_eur_5:,} MBO & {gas_eur_5} BCF"),
            ("50 Year EUR", f"{oil_eur_50:,} MBO & {gas_eur_50} BCF"),
        )

        # Summary data to display

        summary_data = (
            ("Economic Life", f"{econ_life_years} Years"),
            ("NPV of Selected Rate", f"{npv_rate:,.0f} M$"),
            ("Internal Rate of Return", f"{irr_annual:.0%}"),
            ("Payout", f"{payout_years} Years"),
            ("Return on Investment", f"{roi:.0%}"),
            ("Discounted Return on Investment", f"{dcf_roi:.0%}"),
        )

        self.treeview_summary.delete(*self.treeview_summary.get_children())
        for index, row in enumerate(summary_data):

            self.treeview_summary.insert("", index, index, values=row)

        # Discount rate values to display

        self.treeview_discount.delete(*self.treeview_discount.get_children())
        for index, row in enumerate(npv_data):

            self.treeview_discount.insert("", index, index, values=row)

        # EUR values to display

        self.treeview_eur.delete(*self.treeview_eur.get_children())
        for index, row in enumerate(eur_data):

            self.treeview_eur.insert("", index, index, values=row)

        # Summary df to save to excel

        data_dict = {
            "Economic Life (Years)": econ_life_years,
            "NPV of Selected Rate (M$)": npv_rate,
            "Internal Rate of Return": irr_annual,
            "Payout (Years)": payout_years,
            "Return on Investment": roi,
            "Discounted Return on Investment": dcf_roi,
            "NPV8 (M$)": npv_values[0],
            "NPV10 (M$)": npv_values[1],
            "NPV15 (M$)": npv_values[2],
            "NPV20 (M$)": npv_values[3],
            "NPV25 (M$)": npv_values[4],
            "NPV30 (M$)": npv_values[5],
        }

        self.df_summary_output = pd.DataFrame(data_dict, index=["Values"])

        # Output cashflow to text

        self.controller.children["!frame"].children[
            "!cashflowoutputpage"
        ].cashflow_to_text(df=df_cashflow)

    def save_cashflow(self):
        """Save cashflow and summary output to excel"""

        save_as = tk.filedialog.asksaveasfilename(
            filetypes=[("Excel files", ".xlsx .xls")], defaultextension=".xlsx"
        )

        with pd.ExcelWriter(save_as, engine="xlsxwriter") as writer:

            self.df_summary_output.to_excel(
                writer, sheet_name="PetroBase Summary Output", index=False
            )
            self.df_cashflow.to_excel(
                writer, sheet_name="PetroBase Cashflow", index=False
            )


class CashflowOutputPage(ttk.Frame):
    """Frame to hold cashflow input widgets"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(
            row=0, column=0, sticky="NESW", rowspan=4, columnspan=4, padx=1, pady=1
        )

        self.text_cashflow = tk.Text(self, wrap=tk.NONE)

        scroll_x = ttk.Scrollbar(self, orient="horizontal")
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_x.configure(command=self.text_cashflow.xview)

        scroll_y = ttk.Scrollbar(self, orient="vertical")
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.configure(command=self.text_cashflow.yview)

        self.text_cashflow.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_cashflow.configure(
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
        )

    def cashflow_to_text(self, df=None):
        """Inserts cashflow dataframe to text widget"""

        self.text_cashflow.delete("1.0", tk.END)

        columns = (
            "Month",
            "Date",
            "Gross Oil",
            "Gross Gas",
            "Net Oil",
            "Net Gas",
            "Net Oil Price ($/BBL)",
            "Net Gas Price ($/MCF)",
            "Net Oil Revenue (M$)",
            "Net Gas Revenue (M$)",
            "Net Operating Revenue (M$)",
            "Severance Taxes (M$)",
            "OPEX (M$)",
            "CAPEX (M$)",
            "Net Revenue (M$)",
            "Discounted Net Revenue (M$)",
        )

        months = df["Month"]
        dates = df["Date"]

        df = df.applymap("{:,.2f}".format)

        df["Month"] = months
        df["Date"] = dates

        text = df.to_string(
            columns=columns, col_space=15, index=False, justify="center"
        )
        self.text_cashflow.insert(tk.END, text)


def main():
    app = Application()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
    app.mainloop()


if __name__ == "__main__":
    main()
