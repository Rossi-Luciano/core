import requests
import xmltodict
import json

from .models import ScieloJournal, Issue
from processing_errors.models import ProcessingError


def get_collection():
    try:
        collections_urls = requests.get("https://articlemeta.scielo.org/api/v1/collection/identifiers/",
                                        timeout=10)
        for collection in json.loads(collections_urls.text):
            yield collection.get('domain')

    except Exception as e:
        error = ProcessingError()
        error.step = "Collection url search error"
        error.description = str(e)[:509]
        error.type = str(type(e))
        error.save()


