import math
import numpy as np
from typing import List


def convert_secant_di_to_nominal(secant_di: float, b_factor: float) -> float:
    """ Converts secant decline rate which most people assume 
        for decline rates to nominal for decline curve equations
        
    """

    if b_factor == 0:
        # Exponential

        nominal_di = secant_di

    else:

        nominal_di = (((1 - secant_di) ** (-b_factor)) - 1) / b_factor

    return nominal_di


def arps_decline_rate_q(
    qi: float,
    b_factor: float,
    nominal_di: float,
    delta_time: List[float],
    min_decline: float = 0.06,
) -> List[float]:
    """Returns list of production rates at time t for hyperbolic decline"""

    decline = nominal_di

    time = np.array(delta_time)

    q_rates = []

    time_switch_exp = None

    for t in time:

        time_dt = decline / (1 + b_factor * nominal_di * t)

        if time_dt < min_decline:
            # Arps Exponential at minimum decline

            if time_switch_exp is None:
                time_switch_exp = t
                qi_exp = q_rates[-1]

            t = t - time_switch_exp

            q_delta_time = qi_exp * math.exp(-(min_decline * t))

        elif b_factor == 0:
            # Arps Exponential

            q_delta_time = qi * math.exp(-(decline * t))

        elif b_factor == 1.0:
            # Arps Harmonic

            q_delta_time = qi / (1 + decline * t)

        else:
            # Arps Hyperbolic

            q_delta_time = qi / ((1 + b_factor * decline * t) ** (1 / b_factor))

        q_rates.append(q_delta_time)

    return q_rates


def ann_to_monthly_disc_rate(annual_disc_rate: float) -> float:
    """ Given discount rate returns effective monthly discount rate

        Example: convert 10% annual, ann_to_monthly_disc_rate(0.10)
    """

    monthly_disc_rate = ((1 + annual_disc_rate) ** (1 / 12)) - 1

    return monthly_disc_rate


def irr(values: list, monthly=False) -> float:
    """ Given values returns annual IRR to 1% accuracy,
        assuming one negative cashflow beginning which should yield one solution for IRR

        Defaults to annual input values, set monthly=True for monthly values

        IRR returned as float, ex: 10% IRR returned as 0.10

    """

    if sum(values) <= 0:
        return 0

    irr = 0
    npv_rate = 1

    npv_rates = []

    while npv_rate > 0 and irr < 101:

        irr += 1
        npv_values = []

        for time, value in enumerate(values):
            npv_value = (value) / ((1 + (irr / 100)) ** time)
            npv_values.append(npv_value)

        npv_rate = sum(npv_values)
        npv_rates.append(npv_rate)

    if monthly:
        return ((1 + (irr / 100)) ** 12) - 1
    else:
        return irr / 100
