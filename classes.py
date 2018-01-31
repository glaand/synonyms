# -*- coding: utf-8 -*-
import requests
import json

class Endpoint(object):
    word = None
    url = None
    response = None
    document_type = 'json'
    synonyms = []

    def __init__(self, word):
        self.word = word

    def fetch(self):
        res = requests.get(self.url.format(**{
            'query': self.word
        }))
        if self.document_type == 'json':
            self.response = res.json()
        else:
            self.response = res.content()
        return True

    def get(self):
        return self.synonyms

    def json(self):
        return json.dumps(self.get())

class EndpointDEDE(Endpoint):
    url = 'https://www.openthesaurus.de/synonyme/search?q={query}&format=application/json'

    def get(self):
        if self.response.has_key('synsets'):
            synsets = self.response['synsets']
            if synsets:
                if synsets[0].has_key('terms'):
                    terms = synsets[0]['terms']
                    for term in terms:
                        self.synonyms.append(term['term'].encode('utf-8'))
        return self.synonyms
