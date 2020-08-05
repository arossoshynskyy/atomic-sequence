import pytest

from baseline import LockingSequence
from atomicsequence import AtomicSequence


@pytest.mark.benchmark(group="increment_and_get")
def test_locking_increment_and_get(benchmark):
    sequence = LockingSequence(0)

    benchmark(sequence.increment_and_get, 1)


@pytest.mark.benchmark(group="increment_and_get")
def test_atomic_increment_and_get(benchmark):
    sequence = AtomicSequence(0)

    benchmark(sequence.increment_and_get, 1)


@pytest.mark.benchmark(group="get_and_increment")
def test_locking_get_and_increment(benchmark):
    sequence = LockingSequence(0)

    benchmark(sequence.get_and_increment, 1)


@pytest.mark.benchmark(group="get_and_increment")
def test_atomic_get_and_increment(benchmark):
    sequence = AtomicSequence(0)

    benchmark(sequence.get_and_increment, 1)


@pytest.mark.benchmark(group="set")
def test_locking_set(benchmark):
    sequence = LockingSequence(0)

    benchmark(sequence.set, 1)


@pytest.mark.benchmark(group="set")
def test_atomic_set(benchmark):
    sequence = AtomicSequence(0)

    benchmark(sequence.set, 1)


@pytest.mark.benchmark(group="get")
def test_locking_get(benchmark):
    sequence = LockingSequence(0)

    benchmark(sequence.get)


@pytest.mark.benchmark(group="get")
def test_atomic_get(benchmark):
    sequence = AtomicSequence(0)

    benchmark(sequence.get)
