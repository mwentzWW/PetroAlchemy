def set_production_widgets(parent, well_name, phase="Oil"):
    """Set production tab widgets on phase change by user"""

    dict_well_name = str(well_name).replace(" ", "_")

    df_selected = parent.well_dataframes_dict.get(dict_well_name)

    parent.ui.lineEditDeclineCurveName.setText(f"{well_name} {phase} Decline Curve")

    phase_lower = phase.lower()

    parent.ui.spinBoxRate.setValue(int(df_selected[phase_lower][:6].max()))
    max_id = df_selected[phase_lower][:6].idxmax()

    if len(df_selected.index) > 11:
        di_estimate_float = (
            df_selected[phase_lower][max_id] - df_selected[phase_lower][max_id + 12]
        ) / df_selected[phase_lower][max_id]

        time_scale = (
            df_selected["date"][max_id + 12] - df_selected["date"][max_id]
        ).days

        if time_scale == 365:
            di_estimate_pct = round(di_estimate_float * 100, 2)
            parent.ui.doubleSpinBoxDi.setValue(di_estimate_pct)
    else:
        parent.ui.doubleSpinBoxDi.setValue(75)
