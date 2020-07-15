import logging
import random

from aiogram import Bot, Dispatcher, executor, types

from config import TELEGRAM_API_KEY

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)


QUOTES = [
    "Пожалуйста, милый, не мучай себя так, это моя привилегия.",
    "Ты единственный кактус в цветнике моей жизни.",
    "Ты отвратительная женщина. Тебя гложет злость и жадность. Мы могли бы стать друзьями.",
    "Все женщины таковы — встречают идеального мужчину, и тут же пытаются его переделать.",
    "Не казни себя. Это моя работа.",
    "Прошлой ночью ты превзошёл себя. В тебя словно вселился голодный демон. Ты меня напугал. Сделай это снова…",
    "Грязный трюк, старина! Это мне нравится.",
    "Для тебя жизнь — это развлечения и игра. Танцы на кладбище, смрад, разложение…",
    "Прожить день без тебя — вот единственная пытка.",
]


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nThe task of the evil bot is to give you a wish from the cartoon Addams family.")


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.reply("The task of the evil bot is to give you a wish from the cartoon Addams family.")


@dp.message_handler()
async def send_angry(message: types.Message):
    await message.reply(QUOTES[random.randint(0, 8)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

