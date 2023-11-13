
___
# Installing Aiogram3

#### Before you start using Aiogram, you need to install it. To do this, follow these steps:

#### 1. Open a command prompt or terminal.
#### 2. Install the Aiogram library using pip by running the following command:
___
```
pip install -U aiogram
```
___
# Creating a simple bot with Aiogram3
___
#### To create a simple bot using Aiogram, you need to follow these steps:
#### 1. Create a new Python project.
#### 2. Import the necessary Aiogram library classes:

```python
from aiogram import Bot, Dispatcher, types
```
___
#### 3. Create a new bot object:
```python
bot = Bot(token='YOUR_API_TOKEN')
```
___
#### 4. Create a new Dispatcher object:
```python
dp = Dispatcher()
```
___
#### 5. Create a handler function for the /start command:
```python
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi! This is my first Aiogram bot.")
```
___
#### 6. Launch the bot:
```python
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```
___
# Conclusion

#### In this article, we have reviewed the basic steps for installing and getting started with Aiogram. I hope this information was useful for you and will help you start creating your first bots using Aiogram.
___
