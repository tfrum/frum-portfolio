from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([Extension("linked_list.pyx", compiler_directives={'language_level': "3"})])
)