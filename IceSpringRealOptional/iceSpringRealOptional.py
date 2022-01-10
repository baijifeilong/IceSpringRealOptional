# Created by BaiJiFeiLong@gmail.com at 2022/1/9 18:23

from __future__ import annotations

from typing import Generic, Optional, Callable, Any, Union

from IceSpringRealOptional.generics import T, U


class Option(Generic[T]):
    _value: Optional[T]

    @classmethod
    def _new(cls, value: Optional[T]) -> Option[T]:
        option = cls()
        option._value = value
        return option

    @classmethod
    def ofNullable(cls, value: Optional[T]) -> Option[T]:
        return cls._new(value)

    @classmethod
    def of(cls, value: T) -> Option[T]:
        assert value is not None
        return cls._new(value)

    @classmethod
    def empty(cls) -> Option[T]:
        return cls._new(None)

    def isPresent(self) -> bool:
        return self._value is not None

    def ifPresent(self, consumer: Callable[[T], Any]) -> None:
        if self._value is not None:
            consumer(self._value)

    def get(self) -> Optional[T]:
        return self._value

    def orElse(self, other: Optional[U]) -> Optional[Union[T, U]]:
        return self._value if self._value is not None else other

    def orElseGet(self, other: Callable[[], U]) -> Union[T, U]:
        return self._value if self._value is not None else other()

    def orElseThrow(self, exceptionSupplier: Callable[[], BaseException]):
        if self._value is not None:
            return self._value
        else:
            raise exceptionSupplier()

    def filter(self, predicate: Callable[[T], bool]) -> Option[T]:
        if predicate(self):
            return self
        return self.__class__.empty()

    def map(self, mapper: Callable[[T], U]) -> Option[U]:
        if self._value is not None:
            return self.__class__.of(mapper(self._value))
        return self.__class__.empty()

    def flatMap(self, mapper: Callable[[T], Option[U]]) -> Option[U]:
        if self._value is not None:
            return mapper(self._value)
        return self.__class__.empty()

    def __str__(self) -> str:
        return f"<Option:{self._value}>"

    def __repr__(self) -> str:
        return f"<Option:{repr(self._value)}>"

    def __eq__(self, other: Union[T, Any]):
        if isinstance(other, Option):
            return self._value == other._value
        return False
