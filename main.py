import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram import types
import keyboards as kb

bot = Bot(token='')
dp = Dispatcher()


# Main command /start
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Welcome!', reply_markup=kb.main)


@dp.message(F.text == 'Корзина')
async def contacts(message: Message):
    await message.answer('Наша корзина', reply_markup=kb.corzina)


@dp.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('Наши контакты', reply_markup=kb.socials)


@dp.message(F.text == 'Мой профиль')
async def contacts(message: Message):
    await message.answer(f'Ваше имя: {message.from_user.first_name}')
    await message.answer(f'Ваш ID: {message.from_user.id}')


# Setting an id/name using message.from_user.id
@dp.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')
    await message.answer_photo(
        photo='https://www.shutterstock.com/shutterstock/photos/2129672915/display_1500/stock-vector-modern-technology-banners-collection-in-cyberpunk-style-abstract-sci-fi-text-boxes-with-glitch-2129672915.jpg',
        caption='1 способ url')
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIBrmUip9fMkUTVoUtSvYZK74aG6eqQAAK8yzEb4BQRScAb1vLylonKAQADAgADeQADMAQ',
        caption='2 способ id')


# Example of sending images
@dp.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(
        photo='https://www.shutterstock.com/shutterstock/photos/1594457860/display_1500/stock-vector-artificial-intelligence-tech-background-digital-technology-deep-learning-and-big-data-concept-1594457860.jpg',
        caption='2 способ url')


# Example of photo processing
@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(message.photo[-1].file_id)


# Example of sending documents
@dp.message(F.text == '/send_doc')
async def cmd_send_doc(message: Message):
    await message.answer_document(document='BQACAgIAAxkBAAIBtWUiqbrHEQc8WTCRB-eQUCdIieDCAALuOQAC4BQRSaj5hvgYGQkWMAQ',
                                  caption='Документация aiogram3 eng')


# Example of sending documents +id+
@dp.message(F.document)
async def get_document(message: Message):
    await message.answer(message.document.file_id)


# It will work if more than one failed
@dp.message()
async def echo(message: Message):
    await message.answer('I dont understand you...')


async def main():
    await dp.start_polling(bot)


# The main() function is run only if the script is run from this file
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
