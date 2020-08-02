# Atomic Sequence

A lock-free sequence which uses the C++ atomic library under the hood. This gives
a ~3.5x speed increase over using python locks 

## Install
The packge can be installed the usual way using setup.py

```
python setup.py install
```

## Testing
To run unittests and benchmarks use tox:

```
pipenv run tox
```
