from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Контакты')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='wtf')



socials = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK', url='https://vk.com/kkuriiov')],
    [InlineKeyboardButton(text='Telegram', url='https://t.me/qwerty375')]
])


profill = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/qwerty375')]
])

corzina = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Keyboards ', url='https://clck.ru/366gWF')],
    [InlineKeyboardButton(text='Mouse', url='clck.ru/366gXf')]
])
