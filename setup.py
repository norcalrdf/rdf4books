from setuptools import setup, find_packages
import sys, os

version = '2010.12'

setup(name='rdf4books',
      version=version,
      description="RDF Model for Books",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Gavin Carothers',
      author_email='gavin@carothers.name',
      url='',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "pymantic",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
