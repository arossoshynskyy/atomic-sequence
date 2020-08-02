from sequence.sequence cimport Sequence as CppSequence


cdef class Sequence:
    """ Used to track sequences and perform atomic operations """
    cdef CppSequence* value

    def __cinit__(self, value):
        self.value = new CppSequence(value)

    def get(self):
        return self.value.get()

    def set(self, long value):
        self.value.set(value)

    def increment_and_get(self, long value):
        """ Increment the current value of the sequence by a given amount
        and return the new value """
        return self.value.increment_and_get(value)

    def get_and_increment(self, long value):
        """ Increment the current value of the sequence by a given amount
        and return the value directly preceding the operation """
        return self.value.get_and_increment(value)

    def __dealloc__(self):
        del self.value