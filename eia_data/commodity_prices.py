import json
import requests
import time
import os

# Source spot prices from EIA.gov
# Get EIA_API_KEY here https://www.eia.gov/opendata/register.php

json_file = open(r"app_settings.json", "r")
json_data = json.loads(json_file.read())
json_file.close()

api_key = json_data.get("eia_key")


def spot_prices():
    """ Pulls most recent date EIA Spot prices for WTI and Henry Hub Gas from EIA.gov
    
        Returns ($/BBL, $/MMBTU)
    """

    wti_spot_link = f"http://api.eia.gov/series/?api_key={api_key}&series_id=PET.RWTC.D"
    henry_hub_spot_link = (
        f"http://api.eia.gov/series/?api_key={api_key}&series_id=NG.RNGWHHD.D"
    )

    json_response_wti = requests.get(wti_spot_link)
    wti_json_loaded = json.loads(json_response_wti.text)

    time.sleep(0.25)

    json_response_hh = requests.get(henry_hub_spot_link)
    hh_json_loaded = json.loads(json_response_hh.text)

    wti_spot = wti_json_loaded["series"][0]["data"]
    hh_spot = hh_json_loaded["series"][0]["data"]

    wti_last_spot = wti_spot[0][1]
    hh_last_spot = hh_spot[0][1]

    return (wti_last_spot, hh_last_spot)


def futures_prices():
    """ Pulls front month current Nymex prices for WTI and Natural Gas from EIA.gov
    
        Returns ($/BBL, $/MMBTU)
    """

    wti_futures_link = (
        f"http://api.eia.gov/series/?api_key={api_key}&series_id=PET.RCLC1.D"
    )
    nat_gas_future_link = (
        f"http://api.eia.gov/series/?api_key={api_key}&series_id=NG.RNGC1.D"
    )

    json_response_wti = requests.get(wti_futures_link)
    wti_json_loaded = json.loads(json_response_wti.text)

    time.sleep(2)

    json_response_nat_gas = requests.get(nat_gas_future_link)
    nat_gas_json_loaded = json.loads(json_response_nat_gas.text)

    wti_futures = wti_json_loaded["series"][0]["data"]
    nat_gas_futures = nat_gas_json_loaded["series"][0]["data"]

    wti_first_contract = wti_futures[0][1]
    nat_gas_first_contract = nat_gas_futures[0][1]

    return (wti_first_contract, nat_gas_first_contract)
