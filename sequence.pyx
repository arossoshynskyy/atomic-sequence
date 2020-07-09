from Sequence cimport Sequence


cdef class AtomicSequence:
    """ Used to track sequences and perform atomic operations """
    cdef Sequence* value

    def __cinit__(self, value):
        self.value = new Sequence(value)

    def get(self):
        return self.value.get()

    def set(self, long value):
        self.value.set(value)

    def increment_and_get(self, long value):
        return self.value.increment_and_get(value)