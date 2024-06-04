# aiogram==2.23.1

from ru.bot.conf_data import pvlsbk_quiz_bot  # уникальный telegramBot token
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token=pvlsbk_quiz_bot)
dp = Dispatcher(bot)
filename = 'questions.txt'


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Приветствую в моей викторине! Готовы начать игру?")


@dp.message_handler()
async def ask_question(message: types.Message):

    questions = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            question = lines[i].strip()
            options = [lines[j].strip() for j in range(i + 1, i + 5)]
            answer = int(lines[i + 5].strip())
            questions.append((question, options, answer))

    score = 0

    for question, options, answer in questions:
        await message.reply(question)
        for i, option in enumerate(options, 1):
            await message.reply(f"{i}. {option}")

        user_answer = int(message.text)

        if user_answer == answer:
            await message.reply(f"\nПоздравляю! \"{options[answer - 1]}\" - это правильный ответ.\n")
            score += 1
        else:
            await message.reply(f"\nУвы, но ответ неправильный.\n"
                                f"Правильный ответ: {options[answer - 1]}\n")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


