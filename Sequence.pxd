cdef extern from "Sequence.h" nogil:
    cdef cppclass Sequence:
        Sequence(long value) except +
        long get()
        void set(long value)
        long increment_and_get(long value)
