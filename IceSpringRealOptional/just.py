# Created by BaiJiFeiLong@gmail.com at 2022/1/10 16:56

from __future__ import annotations

from typing import Generic, Callable, Any

from IceSpringRealOptional.generics import T, U


class Just(Generic[T]):
    _value: T

    @classmethod
    def of(cls, value: T) -> Just[T]:
        just = cls()
        just._value = value
        return just

    def value(self) -> T:
        return self._value

    def apply(self, consumer: Callable[[T], Any]) -> Just[T]:
        consumer(self._value)
        return self

    def then(self, mapper: Callable[[T], U]) -> Just[U]:
        return Just.of(mapper(self._value))
