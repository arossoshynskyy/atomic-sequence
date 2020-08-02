import pytest

from baseline import LockingSequence
from atomic import Sequence


def increment_and_get(sequence=None):
    sequence.increment_and_get(1)


def get_and_increment(sequence=None):
    sequence.get_and_increment(1)


def set_get(sequence=None):
    sequence.set(1)
    sequence.get()


@pytest.mark.benchmark(group="increment_and_get")
def test_locking_increment_and_get(benchmark):
    sequence = LockingSequence(0)

    benchmark(increment_and_get, sequence=sequence)


@pytest.mark.benchmark(group="increment_and_get")
def test_atomic_increment_and_get(benchmark):
    sequence = Sequence(0)

    benchmark(increment_and_get, sequence=sequence)


@pytest.mark.benchmark(group="get_and_increment")
def test_locking_get_and_increment(benchmark):
    sequence = LockingSequence(0)

    benchmark(get_and_increment, sequence=sequence)


@pytest.mark.benchmark(group="get_and_increment")
def test_atomic_get_and_increment(benchmark):
    sequence = Sequence(0)

    benchmark(get_and_increment, sequence=sequence)


@pytest.mark.benchmark(group="set_get")
def test_locking_set_get(benchmark):
    sequence = LockingSequence(0)

    benchmark(set_get, sequence=sequence)


@pytest.mark.benchmark(group="set_get")
def test_atomic_set_get(benchmark):
    sequence = Sequence(0)

    benchmark(set_get, sequence=sequence)
