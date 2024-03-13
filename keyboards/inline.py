from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_another_photo(animal: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ещё', callback_data=animal)]
    ])
    return keyboard
