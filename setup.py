from setuptools import Extension, setup, find_packages

ext_modules = [
    Extension("atomicsequence", sources=["sequence/sequence.pyx"], language="c++"),
]


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
    setup_requires=["setuptools>=18.0", "Cython>3.0"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="atomic-sequence",
    packages=find_packages(),
    package_data={"": ["src/*", "*.pxd", "*.pyx", "*.cpp", ".h"]},
    python_requires=">=3.7",
    url="https://github.com/arossoshynskyy/atomic-sequence",
    version="0.0.9",
)
