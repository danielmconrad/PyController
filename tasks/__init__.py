import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from invoke import Collection
from . import tests, examples, environment


ns = Collection(tests, examples, environment)