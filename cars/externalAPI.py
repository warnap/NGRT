import requests
from config.settings import API_URL


def get_models(make):
    url = API_URL + 'vehicles/getmodelsformake/' + make + '?format=json'

    resp = requests.get(url)
    if resp.status_code == 200:
        models = [itm['Model_Name'].lower() for itm in resp.json()['Results']]
        return models if models else None
    else:
        return None


def check_make(make):
    models = get_models(make)

    return True if models else False


def check_make_model(make, model):
    models = get_models(make)

    return True if model.lower() in models else False


# print(check_make_model('Volvo', 'S40'))
