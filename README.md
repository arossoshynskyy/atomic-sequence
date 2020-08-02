# Atomic Sequence

A lock-free sequence which uses C++ atomic library under the hood.

## Testing
The package must be built in-place before running any tests. This will 
generate an .so file that can be imported without distributing the package.

```
pipenv python setup.py build_ext --inplace
pipenv python -m pytest
```

## Install
The cpakge can be installed the usual way using setup.py

```
python3.8 setup.py install
```
