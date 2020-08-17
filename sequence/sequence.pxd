cdef extern from "src/Sequence.cpp":
    pass

cdef extern from "src/Sequence.h":

    cdef cppclass Sequence:
        Sequence(long value) except +
        long get()
        void set(long value)
        long increment_and_get(long value)
        long get_and_increment(long value)
