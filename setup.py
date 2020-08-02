from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize


with open("README.md", "r") as fh:
    long_description = fh.read()

ext_modules = cythonize(
    Extension("atomic", sources=["sequence/sequence.pyx"], language="c++",),
    compiler_directives={"embedsignature": True},
)

setup(
    author="Andriy Rossoshynskyy",
    author_email="andriy.rossoshynskyy@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    description="A lock-free, thread-safe sequence counter using the C++ atomic library.",
    ext_modules=ext_modules,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="atomic-sequence",
    # include_package_data=True,
    install_requires=["Cython"],
    packages=find_packages(),
    package_data={"": ["src/*", "*.pxd", "*.pyx", "*.cpp", ".h"],},
    python_requires=">=3.6",
    setup_requires=["Cython"],
    url="https://github.com/arossoshynskyy/atomic-sequence",
    version="0.0.5",
)
