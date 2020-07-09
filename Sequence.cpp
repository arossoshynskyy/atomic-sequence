#include "Sequence.h"


Sequence::Sequence() {}

Sequence::Sequence(long value) {
    this->value = value;
}

long Sequence::get() {
    return value.load();
}

void Sequence::set(long value) {
    this->value.exchange(value);
}

long Sequence::increment_and_get(long value) {
    this->value.fetch_add(value);
    return this->value.load();
}
