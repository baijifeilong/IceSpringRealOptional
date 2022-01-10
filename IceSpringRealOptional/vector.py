# Created by BaiJiFeiLong@gmail.com at 2022/1/10 16:56

from __future__ import annotations

from typing import Generic, Callable, Any, Union, Optional

from IceSpringRealOptional.generics import T, U
from IceSpringRealOptional.maybe import Maybe


class Vector(list, Generic[T, U]):
    @classmethod
    def of(cls, *args: T) -> Vector[T]:
        return cls(args)

    def get(self, index: int) -> Maybe[T]:
        return Maybe.ofNullable(self[index] if index < len(self) else None)

    def getOrNone(self, index: int) -> Optional[T]:
        return self[index] if index < len(self) else None

    def getOrElse(self, index: int, other: U) -> Union[T, U]:
        return self[index] if index < len(self) else other

    def getOrElseGet(self, index: int, supplier: Callable[[], U]) -> Union[T, U]:
        return self[index] if index < len(self) else supplier()

    def getOrElseThrow(self, index: int, exceptionSupplier: Callable[[], BaseException]):
        if index < len(self):
            return self[index]
        raise exceptionSupplier()

    def map(self, mapper: Callable[[T], U]) -> Vector[T]:
        return Vector(mapper(x) for x in self)

    def flatMap(self, mapper: Callable[[Any], U]) -> Vector[U]:
        return Vector(y for x in self for y in mapper(x))

    def filter(self, predicate: Callable[[T], bool]) -> Vector[T]:
        return Vector(x for x in self if predicate(x))

    def apply(self, consumer: Callable[[Vector[T]], Any]) -> Vector[T]:
        consumer(self)
        return self
