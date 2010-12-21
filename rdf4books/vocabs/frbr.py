from pymantic.rdf import Resource, register_class

class FRBRResource(Resource):
    namespaces = {"frbr":"http://purl.org/vocab/frbr/core#",
                  "dc":"http://purl.org/dc/terms/"}

@register_class("frbr:Concept")
class Concept(FRBRResource):
    """A class whose members are an abstract idea or notion. This class 
    corresponds to the FRBR group three entity 'Concept'."""
    pass

@register_class("frbr:CorporateBody")
class CorporateBody(FRBRResource):
    """A class whose members are an organization or group of individuals and/or 
    other organizations. This class corresponds to the FRBR group two entity 
    'Corporate Body'."""
    pass

@register_class("frbr:Endeavour")
class Endeavour(FRBRResource):
    """A class whose members are any of the products of artistic or creative 
    endeavour. This class represents any one of the FRBR group one entities."""
    scalers = ["dc:title"]

@register_class("frbr:Work")
class Work(Endeavour):
    """A class whose members are an abstract notion of an artistic or 
    intellectual creation. This class corresponds to the FRBR group one entity 
    'Work'."""
    pass

@register_class("frbr:Manifestation")
class Manifestation(Endeavour):
    """A class whose members are the physical embodiment of one or more 
    expressions. This class corresponds to the FRBR group one entity 
    'Manifestation'."""
    pass

@register_class("frbr:Expression")
class Expression(Endeavour):
    """A class whose members are a realization of a single work usually in a 
    physical form. This class corresponds to the FRBR group one entity 
    'Expression'."""
    pass

@register_class("frbr:Item")
class Item(Endeavour):
    """A class whose members are an exemplar of a single manifestation. This 
    class corresponds to the FRBR group one entity 'Item'."""
    pass

@register_class("frbr:Image")
class Image(Expression):
    pass

