import io
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.fsm import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from PIL import Image, ImageDraw, ImageFont
import config

# Ініціалізація бота та диспетчера
bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class CommandState:
    waiting_for_name = "waiting_for_name"

@dp.message_handler(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привіт! Введи своє ім'я для генерації сертифіката:")
    await state.set_state(CommandState.waiting_for_name)

@dp.message_handler(state=CommandState.waiting_for_name)
async def handle_name(message: types.Message, state: FSMContext):
    user_name = message.text

    # Генерація сертифікату
    clock = await bot.send_message(message.chat.id, "⏳ Генерується сертифікат...")
    
    await asyncio.sleep(1)

    with Image.open("dtek.jpg") as im:
        draw = ImageDraw.Draw(im)
        font_path = "MontserratAlternates-Regular.ttf"
        
        font = ImageFont.truetype(font_path, 64)
        text_color = (0, 0, 0)

        # Позиція тексту імені
        text_position = (130, 560)
        draw.text(text_position, user_name, font=font, fill=text_color)

        image_buffer = io.BytesIO()
        im.save(image_buffer, format="JPEG")
        image_buffer.seek(0)

    await asyncio.sleep(1)

    await bot.delete_message(message.chat.id, clock.message_id)
    await bot.send_photo(message.chat.id, image_buffer, caption="Ваш сертифікат згенеровано!")
    await state.finish()

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
