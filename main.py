
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import TOKEN
from handlers import start, language, message_forwarder, admin_panel

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)
language.register_handlers(dp)
message_forwarder.register_handlers(dp)
admin_panel.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
