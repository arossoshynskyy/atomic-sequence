from assertpy import assert_that

from atomicsequence import AtomicSequence


def test_get_set():
    sequence = AtomicSequence(0)

    sequence.set(10)

    assert_that(sequence.get()).is_equal_to(10)


def test_increment_and_get():
    sequence = AtomicSequence(0)

    new_value = sequence.increment_and_get(10)

    assert_that(new_value).is_equal_to(10)


def test_get_and_increment():
    sequence = AtomicSequence(0)

    old_value = sequence.get_and_increment(10)
    new_value = sequence.get()

    assert_that(old_value).is_equal_to(0)
    assert_that(new_value).is_equal_to(10)
