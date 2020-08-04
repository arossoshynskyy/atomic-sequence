from setuptools import Extension, setup, find_packages
from distutils.command.sdist import sdist as _sdist


# Can't import cython until setup is read, can't read setup until
# Cython is installed.
try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

if use_cython:
    ext_modules = cythonize(
        Extension("atomic", sources=["sequence/sequence.pyx"], language="c++",),
        compiler_directives={"embedsignature": True},
    )
else:
    ext_modules = [Extension("atomic", sources=["sequence/sequence.cpp"], language="c++")]


with open("README.md", "r") as fh:
    long_description = fh.read()


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
    packages=find_packages(),
    package_data={"": ["src/*", "*.pxd", "*.pyx", "*.cpp", ".h"],},
    python_requires=">=3.6",
    url="https://github.com/arossoshynskyy/atomic-sequence",
    version="0.0.7",
)
