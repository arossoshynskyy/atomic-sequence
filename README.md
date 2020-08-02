# Atomic Sequence

A lock-free sequence which uses the C++ atomic library under the hood. This gives
a ~3.5x speed increase over using python locks 

## Install
The packge can be installed the usual way using setup.py

```
python setup.py install
```

## Usage

```python
from atomic import Sequence

sequence = Sequence(0)

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
pipenv run tox
```
