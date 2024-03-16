from aiogram import executor
from create_bot import dp
from hendlers import commands_player

commands_player.register_handlers_commands_player(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

