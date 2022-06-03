import API
from vkbottle.bot import Bot, Message
post=[]
bot = Bot(token=API.API)


@bot.on.message(text="Добавить на пост <item>")
async def message_handler(message: Message, item=None):
    if item is not None:
        if post.count(item)!=0:
            await message.answer("Уже на посту ")
        else:
            post.append(item)
            await message.answer("Пост пидора принял "+item)


@bot.on.message(text=["Кто на посту?","Кто на посту"])
async def message_handler(message: Message):
    if len(post):
        if len(post)==1:
            str="Пост пидора держит:\n"
        else:
            str="Пост пидора держат:\n"
        for line in post:
            str+=line+"\n"
        await message.answer(str)
    else:
        await message.answer("На посту никого")

@bot.on.message(text="Убрать с поста <item>")
async def message_handler(message: Message,item=None):
    if item is not None:
        if post.count(item):
            post.remove(item)
            await message.answer("Пост пидора сдал "+item)
        else:
            await message.answer(item+" и так не пидор")



@bot.on.message(text="/help")
async def message_handler(message: Message):
    await message.answer("1) Кто на посту @...\n2) Добавить на пост @...\n3) Убрать с поста @...\n(Без нумерации)")

bot.run_forever()