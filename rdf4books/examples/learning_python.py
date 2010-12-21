from rdf4books.vocabs.frbr import *
from pymantic.util import en, de
from rdflib import ConjunctiveGraph, Namespace
complete_work_graph = ConjunctiveGraph()

learning_python_work = Work.new(complete_work_graph, 
                                "http://purl.org/NET/rdf4books/work/learning_python")
learning_python_work["dc:title"] = set((en("Learning Python"), 
                                       de("Python Lernen")))

expressions = []
learning_python_1e = Expression.new(complete_work_graph, "http://purl.org/NET/rdf4books/editions/learning_python_1en")
learning_python_1e["frbr:realizationOf"] = learning_python_work
learning_python_1e["dc:title"] = "Learning Python"
expressions.append(learning_python_1e)

lp_1e_print_book = Manifestation.new(complete_work_graph, "http://purl.org/NET/rdf4books/product/isbn-9781565924642")
lp_1e_print_book["frbr:embodimentOf"] = learning_python_1e
learning_python_1e["frbr:embodiment"] = lp_1e_print_book

learning_python_work["frbr:realization"] = set(expressions)

complete_work_graph.bind("work", Namespace("http://purl.org/NET/rdf4books/work/"))
complete_work_graph.bind("product", Namespace("http://purl.org/NET/rdf4books/product/"))
complete_work_graph.bind("editions", Namespace("http://purl.org/NET/rdf4books/editions/"))


print  complete_work_graph.serialize(format="n3")