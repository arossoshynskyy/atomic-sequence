from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize


ext_modules = cythonize(
    Extension(
        "atomic",
        sources=["sequence/sequence.pyx"],
        language="c++",
    ), 
    compiler_directives={
      'embedsignature': True},
)

setup(
    author="Andriy Rossoshynskyy",
    description="A lock-free, thread-safe sequence counter using the C++ atomic library.",
    ext_modules=ext_modules,
    name="atomic-sequence",
    #include_package_data=True,
    install_requires=["Cython"],
    packages=find_packages(),
    package_data = {
        "": ["src/*", "*.pxd", "*.pyx", "*.cpp", ".h"],
    },
    setup_requires=["Cython"],
    version="0.0.1",
)
