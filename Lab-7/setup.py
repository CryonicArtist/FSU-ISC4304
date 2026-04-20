from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name="Julia Cython Module",
    ext_modules=cythonize("juliac.pyx", compiler_directives={'language_level': "3"}),
    include_dirs=[numpy.get_include()]
)