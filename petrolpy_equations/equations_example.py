import equations as petrolpy
import pandas as pd

df = pd.read_excel(r'data_example\Gusher #1.xlsx', parse_dates=True)

df.columns = map(str.lower, df.columns)

df["delta_time_yrs"] = [
            ((date - df["date"][0]).days / 365) for date in df["date"]
        ]

di_secant = float(0.6)
b_factor = float(1.1)
qi = float(2700)

nominal_di = petrolpy.convert_secant_di_to_nominal(
    di_secant, b_factor
)

df["curve"] = [
            petrolpy.hyp_decline_rate_q(
                qi,
                b_factor,
                nominal_di,
                delta_time
            )
            for delta_time in df["delta_time_yrs"]
        ]

print(df.curve)