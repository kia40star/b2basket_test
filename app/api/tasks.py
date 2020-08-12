import logging
from xml.etree import cElementTree as ET

import requests

from b2basket.celery import app
from .models import Data


def parse_xml(url):
    response = requests.get(url)
    xml = ET.fromstring(response.content)
    return [el.text for el in xml]


@app.task
def run_task(data_id):
    try:
        data = Data.objects.get(pk=data_id)
        keys = parse_xml(data.url) or list()
        data.update_keys(keys=keys)
    except Data.DoesNotExist:
        logging.warning(f"Tried to parse non-existing data'{data_id}'")
    except Exception as err:
        data.update_keys(error=str(err))
