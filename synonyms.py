# -*- coding: utf-8 -*-
import sys
from classes import EndpointDEDE

ENDPOINTS = {
    'de_DE': EndpointDEDE,
}

if len(sys.argv) < 2:
    print("usage: {0} <word:required> <locale:optional>".format(sys.argv[0]))
    exit(0)

PARAMS = {
    'word': sys.argv[1],
    'locale': 'de_DE' # Default locale: de_DE
}

if len(sys.argv) > 2:
    if ENDPOINTS.has_key(sys.argv[2]):
        PARAMS['locale'] = sys.argv[2]
    else:
        print("This locale is not available yet. Following locales are available: {0}".format(', '.join(list(ENDPOINTS.keys()))))
        exit(0)

endpoint = ENDPOINTS[PARAMS['locale']](PARAMS['word'])
endpoint.fetch()
print(endpoint.json())
