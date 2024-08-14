import io
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import config

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Массив користувачів
users = [
    {"name": "Anakin Skywalker", "email": "test@gmail.com", "score": "100/100"},
    {"name": "Герасименко Ірина", "email": "gerasimenko2121@gmail.com", "score": "12/15"},
    {"name": "Дмитренко Юлія", "email": "yuliiadmytrenko.workmail@gmail.com", "score": "11/15"},
    {"name": "Бездітко Ольга", "email": "olgabezdetko1994@gmail.com", "score": "11/15"},
    {"name": "Мостіпан-Ак Леся", "email": "less8713@gmail.com", "score": "11/15"},
    {"name": "Бондар Юлія", "email": "ylia.bondar.2@gmail.com", "score": "11/15"},
    {"name": "Гладун Анастасія", "email": "nastia.gladun@gmail.com", "score": "11/15"},
    {"name": "Романюк Лілія", "email": "lylyanochka@gmail.com", "score": "10/15"},
    {"name": "Чистякова Дар'я", "email": "daracistakova364@gmail.com", "score": "10/15"},
    {"name": "Мокрицька Валерія", "email": "lerkaklimyukova@gmail.com", "score": "10/15"},
    {"name": "Білик Інеса", "email": "inesa.bilyk@gmail.com", "score": "10/15"},
    {"name": "Гейман Яна", "email": "heymanyana@gmail.com", "score": "10/15"},
    {"name": "Дементєєв Дмитро", "email": "acuta.pugione@gmail.com", "score": "10/15"},
    {"name": "Шийка Олена", "email": "olenashyyka@gmail.com", "score": "10/15"},
    {"name": "Гвоздецька Лариса", "email": "lar.hvozdetska@gmail.com", "score": "9/15"},
    {"name": "Шпакова Дар'я", "email": "shpakova.daria.goiteens@gmail.com", "score": "9/15"},
    {"name": "Невинна Оксана", "email": "linochka030109@gmail.com", "score": "9/15"},
    {"name": "Mariia Kostiak", "email": "mariiakostiak@gmail.com", "score": "9/15"},
    {"name": "Остропільська Вікторія", "email": "v.ostropilska@goiteens.global", "score": "9/15"},
    {"name": "Сопко Катерина", "email": "zadirraka2013@gmail.com", "score": "9/15"},
    {"name": "Ляшенко Оксана", "email": "lyashenkoo100502@gmail.com", "score": "8/15"},
    {"name": "Бібченко Антоніна", "email": "antoninaab20@gmail.com", "score": "7/15"},
    {"name": "Гунько Ольга", "email": "olu698950@gmail.com", "score": "7/15"},
    {"name": "Бутрін Кирило", "email": "kirill.butrin@gmail.com", "score": "7/15"},
    {"name": "Біднюк Неля", "email": "ztudo2315@gmail.com", "score": "7/15"},
    {"name": "Кучер Наталія", "email": "natalkakucher20@gmail.com", "score": "7/15"},
    {"name": "Ірха Віолета", "email": "irhavioletta@gmail.com", "score": "7/15"},
    {"name": "Кулібабіна Ганна", "email": "hanna.kulibabina@gmail.com", "score": "6/15"},
    {"name": "olgiboulehibou2012", "email": "olgiboulehibou2012@gmail.com", "score": "6/15"},
    {"name": "Щегорцов Максим", "email": "m.shchehortsov@gmail.com", "score": "6/15"},
    {"name": "Дементєєва Вероніка", "email": "veronikasilakova740@gmail.com", "score": "6/15"},
    {"name": "Подолянець Юлія", "email": "juliapodolanec@onlineeducator.dev", "score": "5/15"},
    {"name": "Гайченя Олена", "email": "gaichenia.elena@gmail.com", "score": "5/15"},
    {"name": "Матяш Вікторія", "email": "matiash.teach@gmail.com", "score": "5/15"},
    {"name": "Завальна Юлія", "email": "zavalnayliua@gmail.com", "score": "4/15"},
    {"name": "Бойко Наталія", "email": "nataboyko569@gmail.com", "score": "4/15"},
    {"name": "Войтенко Марія", "email": "mashagorodna@gmail.com", "score": "3/15"},
    {"name": "Ковтало Оксана", "email": "kovtalo591@gmail.com", "score": "8/15"},
    {"name": "Кирилишена Лілія", "email": "morsimmortalis05@gmail.com", "score": "6/15"},
    {"name": "Городова Дарʼя", "email": "selezendasa53@gmail.com", "score": "9/15"},
    {"name": "Галенко Богдана", "email": "halenkobohdana@gmail.com", "score": "11/15"},
    {"name": "Ляшенко Анастасія", "email": "kuksenko1986@gmail.com", "score": "1/15"},
    {"name": "Боровікова Марина", "email": "marinabv14@gmail.com", "score": "9/15"},
    {"name": "Орманжи Вікторія", "email": "victoriamatveev@gmail.com", "score": "8/15"},
    {"name": "Борецька Софія", "email": "sophiyaboretska@gmail.com", "score": "6/15"},
    {"name": "Тимошенко Анна", "email": "anetka9856@gmail.com", "score": "7/15"},
    {"name": "Фадєєва Наталія", "email": "fadeevanatali0810@gmail.com", "score": "9/15"},
    {"name": "Рибкіна Олена", "email": "lenarybkina30@gmail.com", "score": "10/15"},
    {"name": "Олена Рожко", "email": "olenarozko46@gmail.com", "score": "8/15"},
    {"name": "Злобіна Ірина", "email": "i_krymska@ukr.net", "score": "11/15"},
    {"name": "Svitlana Odzhykovska", "email": "odjikovska@gmail.com", "score": "7/15"},
    {"name": "Манько Сергій", "email": "msa01051984@gmail.com", "score": "7/15"},
    {"name": "Валенчук Світлана", "email": "svalenchukk@gmail.com", "score": "10/15"},
    {"name": "Keller Vladyslav", "email": "skiffvlad90@gmail.com", "score": "10/15"},
    {"name": "Балясова Анна", "email": "annbaliasova@gmail.com", "score": "9/15"},
    {"name": "Волошиненко Тетяна", "email": "tanya.voloshinenko@gmail.com", "score": "10/15"},
    {"name": "Гєєнко Наталія", "email": "nataligeenko@gmail.com", "score": "3/15"},
    {"name": "Новохатько Наталія", "email": "novohatko123456789@gmail.com", "score": "11/15"},
    {"name": "Самусєнко Валерія", "email": "art69time@gmail.com", "score": "6/15"}
]


class CommandState:
    waiting_for_email = "waiting_for_email"
    waiting_for_name = "waiting_for_name"
    waiting_for_confirmation = "waiting_for_confirmation"

@dp.message_handler(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привіт! Тут ти можеш згенерувати сертифікат від GoITeens\n""\n"
                         "Введи свою електронну пошту:")
    await state.set_state(CommandState.waiting_for_email)

@dp.message_handler(state=CommandState.waiting_for_email)
async def handle_email(message: types.Message, state: FSMContext):
    email = message.text

    # Перевірка електронної пошти
    user = next((u for u in users if u["email"] == email), None)
    
    if user:
        user_name = user["name"]
        user_score = user["score"]
        
        # Відправка повідомлення з підтвердженням
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Так, все вірно!", callback_data="confirm"))
        markup.add(InlineKeyboardButton("Ні, ім'я не вірне", callback_data="edit_name"))
        
        await message.answer(f"Так, ми знайшли Вас в базі. Ви {user_name}, Ваш бал за тестування {user_score}.\n""\n"
                             "У разі питань щодо оцінювання тестування - зверніться до Тетяни Чав'як", reply_markup=markup)
        await state.set_state(CommandState.waiting_for_confirmation)
        await state.update_data(user_name=user_name, user_score=user_score, email=email)
    else:
        await message.answer("Пошта не вірна, спробуйте знову:")
        await state.set_state(CommandState.waiting_for_email)

@dp.callback_query_handler(text="confirm", state=CommandState.waiting_for_confirmation)
async def confirm_certificate(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_name = data.get("user_name")
    user_score = data.get("user_score")

    # Генерація сертифікату
    clock = await bot.send_message(callback_query.message.chat.id, "⏳")
    
    await asyncio.sleep(1)

    with Image.open("certificate.png") as im:
        draw = ImageDraw.Draw(im)
        font_path = "MontserratAlternates-Regular.ttf"
        
        font = ImageFont.truetype(font_path, 32)
        font_score = ImageFont.truetype(font_path, 18)
        
        text_color = (0, 0, 0)  # Чорний колір

        # Позиція для імені
        text_bbox = draw.textbbox((0, 0), user_name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        image_width, image_height = im.size
        text_position = ((image_width - text_width) // 2, 420)  # Зміна позиції для імені
        
        draw.text(text_position, user_name, font=font, fill=text_color)

        # Додати score на сертифікат
        score_bbox = draw.textbbox((0, 0), user_score, font=font)
        score_width = score_bbox[2] - score_bbox[0]
        score_position = (70, 744)  # Зміна позиції для балів
        
        draw.text(score_position, user_score, font=font_score, fill=text_color)

        image_buffer = io.BytesIO()
        im.save(image_buffer, format="PNG")
        image_buffer.seek(0)

    await asyncio.sleep(1)

    await bot.delete_message(callback_query.message.chat.id, clock.message_id)
    await bot.send_photo(callback_query.message.chat.id, image_buffer, caption="Ваш сертифікат згенеровано!")
    await state.finish()

@dp.callback_query_handler(text="edit_name", state=CommandState.waiting_for_confirmation)
async def edit_name(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Введіть ім'я, яке має бути в сертифікаті:")
    await state.set_state(CommandState.waiting_for_name)

    # Зберегти email для подальшої перевірки
    data = await state.get_data()
    email = data.get("email")
    await state.update_data(email=email)

@dp.message_handler(state=CommandState.waiting_for_name)
async def handle_name(message: types.Message, state: FSMContext):
    new_name = message.text
    data = await state.get_data()
    email = data.get("email")

    # Перевірка електронної пошти
    user = next((u for u in users if u["email"] == email), None)
    
    if user:
        user_score = user["score"]

        # Генерація сертифікату з новим іменем
        clock = await bot.send_message(message.chat.id, "⏳")
        
        await asyncio.sleep(1)

        with Image.open("certificate.png") as im:
            draw = ImageDraw.Draw(im)
            font_path = "MontserratAlternates-Regular.ttf"
            font = ImageFont.truetype(font_path, 32)
            font_score = ImageFont.truetype(font_path, 18)
            
            text_color = (0, 0, 0)  # Чорний колір

            # Позиція для нового імені
            text_bbox = draw.textbbox((0, 0), new_name, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            image_width, image_height = im.size
            text_position = ((image_width - text_width) // 2, 420)  # Зміна позиції для нового імені
            
            draw.text(text_position, new_name, font=font, fill=text_color)

            # Додати score на сертифікат
            score_bbox = draw.textbbox((0, 0), user_score, font=font)
            score_width = score_bbox[2] - score_bbox[0]
            score_position = (70, 744)  # Зміна позиції для балів
            
            draw.text(score_position, user_score, font=font_score, fill=text_color)

            image_buffer = io.BytesIO()
            im.save(image_buffer, format="PNG")
            image_buffer.seek(0)

        await asyncio.sleep(1)

        await bot.delete_message(message.chat.id, clock.message_id)
        await message.answer_photo(image_buffer, caption="Ваш оновлений сертифікат згенеровано!")
        await state.finish()
    else:
        await message.answer("Сталася помилка, спробуйте ще раз.")
        await state.finish()

if __name__ == "__main__":
    import keep_alive
    keep_alive.keep_alive()

    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
