import requests
from config.settings import API_URL


def get_make_and_models(make):
    url = API_URL + 'vehicles/getmodelsformake/' + make + '?format=json'

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['Results']
        models = [itm['Model_Name'] for itm in data]
        if models:
            make = data[0]['Make_Name']
        else:
            make = None

        return make, models if models else None
    else:
        return None
