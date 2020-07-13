from setuptools import Extension, setup
from Cython.Build import cythonize

sources = ["sequence/sequence.pyx", "sequence/Sequence.cpp"]

ext_modules = cythonize(
    [Extension("sequence", sources=sources, language="c++")], annotate=True
)

setup(
    author="Andriy Rossoshynskyy",
    description="Lock-free, thread-safe sequence.",
    ext_modules=ext_modules,
    name="atomic-sequence",
)
