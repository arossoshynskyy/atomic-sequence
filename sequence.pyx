cimport Sequence


cdef class Sequence:
    """ Used to track sequences and perform atomic operations """
    cdef Sequence value

    def __cinit__(self):
        self.value = Sequence(-1)

    cdef get(self):
        return self.value.load()

    cdef set(self, long value):
        self.value.exchange(value)

    cdef increment_and_get(self, long value):
        self.value.fetch_add(value)
        return self.value.load()