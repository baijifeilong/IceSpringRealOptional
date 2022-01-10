# Created by BaiJiFeiLong@gmail.com at 2022/1/10 11:16

from __future__ import annotations

from typing import Type

from IceSpringRealOptional.generics import T


class TypingUtils(object):
    @staticmethod
    def gg(value, _type: Type[T]) -> T:
        return value


gg = TypingUtils.gg
