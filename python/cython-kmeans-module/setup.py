from setuptools import setup
from Cython.Build import cythonize

setup(
    name='KMeansModule',
    ext_modules=cythonize("kmeans.pyx", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)