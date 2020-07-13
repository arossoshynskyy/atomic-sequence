#ifndef SEQUENCE_H
#define SEQUENCE_H

#include <atomic>

using std::atomic;


class Sequence {
    public:
        atomic<long> value;
        Sequence();
        Sequence(long value);
        long get();
        void set(long value);
        long increment_and_get(long value);
        long get_and_increment(long value);
};


#endif
