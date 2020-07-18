# Atomic Sequence

A lock-free sequence which uses C++ atomic operations under the hood.

## Build

```
python3.8 setup.py build_ext --inplace
```

## Install

```
python3.8 setup.py install
```

## Run tests

```
python -m unittest tests/test_atomic_queue.py
```