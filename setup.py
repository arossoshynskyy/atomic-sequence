from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = cythonize([Extension("sequence", sources=["sequence.pyx", "Sequence.cpp"], language="c++")], annotate=True)

setup(
    name='Sequence',
    ext_modules=ext_modules,
)
