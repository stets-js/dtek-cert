import io
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
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

    with Image.open("valley.jpg") as im:
        draw = ImageDraw.Draw(im)
        font_path = "OpenSans-SemiBold.ttf"
        
        font = ImageFont.truetype(font_path, 34)
        text_color = (255, 255, 255)

        # Отримання розмірів зображення
        image_width, image_height = im.size

        # Отримання розміру тексту через textbbox (bounding box)
        text_bbox = draw.textbbox((0, 0), user_name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Обчислення позиції для центрування тексту
        text_position = ((image_width - text_width) // 2, 350)

        # Малювання тексту
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
