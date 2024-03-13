from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class AnimallData(BaseFilter):
    def __init__(self, animals_list: tuple) -> None:
        self.animals_list = animals_list

    async def __call__(self, callback: CallbackQuery) -> Any:
        return callback.data in self.animals_list
