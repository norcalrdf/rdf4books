from pymantic.rdf import Resource, register_class
from frbr import Manifestation

@register_class("bibo:Book")
class Book(Resource):
    namespaces = {"bibo":"http://purl.org/ontology/bibo/"}