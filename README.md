# Atomic Sequence

A lock-free, thread-safe sequence/counter which uses the C++ atomic library under the hood. This gives a ~5-10x speed up compared to threading locks.

## Install
```
pip install atomic-sequence
```

## Usage

```python
from atomicsequence import Sequence

sequence = AtomicSequence(0)

# set current sequence value to 1
sequence.set(1)

# get current value
value = sequence.get()

# increment the sequence value and get the new value
value = sequence.increment_and_get(1)

# increment the sequence value and get the value directly preceding the operation
value = sequence.get_and_increment(1)
```

## Testing
To run unittests and benchmarks use tox:

```
pipenv install --dev
pipenv run tox
```
