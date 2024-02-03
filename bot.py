from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import openai

# Token o'zgaruvchini o'zgartiring
TOKEN = "6875263138:AAHY7niyIHqhQT7VIUzaHLMwGgLnbUedmlU"

# OpenAI API key va engine ID sifatida foydalanilayotgan ma'lumotlarni quyidagi o'zgaruvchilarda saqlang
OPENAI_API_KEY = "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"

ENGINE_ID = "gpt-3.5-turbo-instruct"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_surname = State()
    waiting_for_phone = State()

# Asosiy menuni yaratamiz
menu = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('BEST DOCTORS')
button2 = KeyboardButton(' HOSPITAL')
button3 = KeyboardButton('Registratsiya')
menu.add(button1, button2, button3)

# /start buyrug'i uchun funksiya
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom! Botimizga xush kelibsiz!", reply_markup=menu)

# Birinchi tugma uchun funksiya
@dp.message_handler(lambda message: message.text == 'BEST DOCTORS')
async def button1_handler(message: types.Message):
    await message.answer("Siz ozingizga kerakli bo'lgan doktorni tanlang ")

    # Boshqa tugmalarni yaratamiz
    sub_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    sub_button2 = KeyboardButton('Diyetolog')
    sub_button3 = KeyboardButton('KORDIOLOG')
    sub_button4 = KeyboardButton('NERVOLOG')
    sub_button5 = KeyboardButton('Orqaga')
    sub_menu.add(sub_button2, sub_button3, sub_button4, sub_button5)

    # Foydalanuvchiga yangi tugmalarni yuboramiz
    await message.answer("Siz tanlang", reply_markup=sub_menu)

@dp.message_handler(lambda message: message.text == 'Orqaga')
async def back_handler(message: types.Message):
    await message.answer("Asosiy menyuga qaytildi.", reply_markup=menu)





@dp.message_handler(lambda message: message.text == 'HOSPITAL')
async def button1_handler(message: types.Message):
    await message.answer("Siz ozingizga kerakli bo'lgan doktorni tanlang ")

    # Boshqa tugmalarni yaratamiz
    sub_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    sub_button2 = KeyboardButton('LOCAL HOSPITAL')
    sub_button3 = KeyboardButton('PRIVATE HOSPITAL')
    sub_button4 = KeyboardButton('NERVOLOG')
    sub_button5 = KeyboardButton('BACK')
    sub_menu.add(sub_button2, sub_button3,  sub_button5)

    # Foydalanuvchiga yangi tugmalarni yuboramiz
    await message.answer("Siz tanlang", reply_markup=sub_menu)

@dp.message_handler(lambda message: message.text == 'BACK')
async def back_handler(message: types.Message):
    await message.answer("Asosiy menyuga qaytildi.", reply_markup=menu)

@dp.message_handler(lambda message: message.text == 'LOCAL HOSPITAL')
async def LOCAL(message: types.Message):
    # Inline buttonni yaratamiz
  
    # Foto va matn yuboramiz
    await bot.send_photo(
        chat_id=message.chat.id, 
         photo="https://www.communityhospitalhp.com/wp-content/uploads/sites/10/2022/01/community-hospital.jpeg", 
        caption="⚕️SIZ UCHUN HAMMASI BEPUL"
    )
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_button1 = InlineKeyboardButton("NAVOIY", callback_data='more_info11')
    inline_button2 = InlineKeyboardButton("TASHKENT", callback_data='more_info12')
    inline_button3 = InlineKeyboardButton("BUXORO", callback_data='more_info13')
    inline_button4 = InlineKeyboardButton("ANDIJON", callback_data='more_info14')
    inline_button5 = InlineKeyboardButton("JIZZAX", callback_data='more_info15')
    inline_button6 = InlineKeyboardButton("SAMARQAND", callback_data='more_info16')
    inline_button7 = InlineKeyboardButton("QASHQADARYO", callback_data='more_info17')
    inline_button8 = InlineKeyboardButton("XORAZM", callback_data='more_info18')
    

    inline_keyboard.add(inline_button1,inline_button2,inline_button3,inline_button4,inline_button5,inline_button6,inline_button7,inline_button8)

    # Ma'lumotlarni yuboramiz
    await message.answer(text="VILOYATIZNI TANLANG\n",
                         reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info11')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info12')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info13')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info14')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info15')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info16')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info17')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info18')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 









@dp.message_handler(lambda message: message.text == 'PRIVATE HOSPITAL')
async def LOCAL(message: types.Message):
    # Inline buttonni yaratamiz
  
    # Foto va matn yuboramiz
    await bot.send_photo(
        chat_id=message.chat.id, 
         photo="https://gumlet.assettype.com/newslaundry%2F2020-05%2Fa29773b2-4a54-4732-b566-a579f31c6bdd%2Fprivatehealthcare.jpg?auto=format%2Ccompress", 
        caption="⚕️SIZ UCHUN HAMMASI BEPUL"
    )
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_button1 = InlineKeyboardButton("NAVOIY", callback_data='other_info11')
    inline_button2 = InlineKeyboardButton("TASHKENT", callback_data='other_info12')
    inline_button3 = InlineKeyboardButton("BUXORO", callback_data='other_info13')
    inline_button4 = InlineKeyboardButton("ANDIJON", callback_data='other_info14')
    inline_button5 = InlineKeyboardButton("JIZZAX", callback_data='other_info15')
    inline_button6 = InlineKeyboardButton("SAMARQAND", callback_data='other_info16')
    inline_button7 = InlineKeyboardButton("QASHQADARYO", callback_data='other_info17')
    inline_button8 = InlineKeyboardButton("XORAZM", callback_data='other_info18')
    

    inline_keyboard.add(inline_button1,inline_button2,inline_button3,inline_button4,inline_button5,inline_button6,inline_button7,inline_button8)

    # Ma'lumotlarni yuboramiz
    await message.answer(text="VILOYATIZNI TANLANG\n",
                         reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info11')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info12')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info13')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info14')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info15')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info16')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info17')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 
    
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info18')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" ул. Абу Али ибн Сино, 27""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=40.088894, longitude=65.374251) 



# Registration handler
@dp.message_handler(commands=['registratsiya'], state="*")
async def start_registration(message: types.Message, state: FSMContext):
    await message.answer("Registratsiya uchun, iltimos, ismingizni kiriting:")
    await RegistrationStates.waiting_for_name.set()

# Registration step: Name
@dp.message_handler(state=RegistrationStates.waiting_for_name)
async def register_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Familiyangizni kiriting:")
    await RegistrationStates.next()

# Registration step: Surname
@dp.message_handler(state=RegistrationStates.waiting_for_surname)
async def register_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await message.answer("Telefon raqamingizni kiriting:")
    await RegistrationStates.next()

# Registration step: Phone number
@dp.message_handler(state=RegistrationStates.waiting_for_phone)
async def register_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    # Here you can save the collected information to your database or perform any necessary actions
    await message.answer("Registratsiya muvaffaqiyatli tugallandi!")
    await state.finish()

# Handle cancellation
@dp.message_handler(state="*", commands='cancel')
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Registratsiya bekor qilindi.")

@dp.message_handler(lambda message: message.text == 'Registratsiya')
async def registration_handler(message: types.Message):
    await message.answer("Registratsiya uchun, iltimos, ismingizni kiriting:")
    await RegistrationStates.waiting_for_name.set()

# Uchinchi tugma uchun funksiya
@dp.message_handler(lambda message: message.text == 'KORDIOLOG')
async def button3_handler(message: types.Message):
    # Inline buttonni yaratamiz
  
    # Foto va matn yuboramiz
    await bot.send_photo(
        chat_id=message.chat.id, 
        photo="https://med24.uz/upload/resize_cache/webp/iblock/bfe/262_172_1c01a1ffd119c78b8866afaa9ab404db6/6aiwteyylkl2ugh3xsm7ijfx4f00htrl.webp", 
        caption="⚕️ Zufarov Tulkin Murzaumarovich - kardiolog, 34 yil tajribaga ega shifokor. Onlayn yoki telefon orqali qabulga yozilish"
    )
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_button = InlineKeyboardButton("KOPROQ MALUMOT", callback_data='more_info')
    inline_button2 = InlineKeyboardButton("MANZIL", callback_data='other_info')
    inline_keyboard.add(inline_button,inline_button2)

    # Ma'lumotlarni yuboramiz
    await message.answer(text="Kattalarni qabul qiladi\n\nTashkilot: shahar klinik kasalxonasi №15\nManzil: Toshkent, O'zbekiston\nLavozimi: rezident shifokor",
                         reply_markup=inline_keyboard)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,     text = """Ish davri 1995-2003
Respublika ixtisoslashtirilgan kardiologiya ilmiy-amaliy tibbiyot markazi tashkiloti
Manzil: Toshkent, O'zbekiston

Bo'lim boshlig'i lavozimi
2003 - 2019
Evro Servis tashkiloti (Uchtepa tumani)
Manzil: Toshkent, O'zbekiston
Lavozimi: Kardiolog

Ish davri: 2020 yil-hozir vaqt
Ta'lim / o'quv kurslari: Trening turi
Ta'lim muassasasi: Oliy o'quv yurti
Andijon davlat tibbiyot instituti

Fakultet / Yo'nalish / Bo'lim: Bundan tashqari
Davolash: Bakalavr darajasi
Ixtisoslashuv: O'qish davri: kardiolog 1984 - 1990
Ilmiy yutuqlar: Malaka
Ilmiy daraja-birinchi toifadagi shifokor""")   
# Botni ishga tushuramiz

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text="""🏥 NS Medical (Uchtepa filiali) klinikasi, Toshkent: shifokor. Onlayn yoki telefon orqali qabulga yozilish. Mo'ljal: Charog'on restorani""" 
    )

    await bot.send_location(callback_query.from_user.id, latitude=41.312307, longitude=69.178168)
    
    
    
    
    
    
    
    
    
    
    
@dp.message_handler(lambda message: message.text == 'Diyetolog')
async def button3_handler(message: types.Message):
    # Inline buttonni yaratamiz
  
    # Foto va matn yuboramiz
    await bot.send_photo(
        chat_id=message.chat.id, 
        photo="https://med24.uz/upload/resize_cache/webp/iblock/c87/262_172_1c01a1ffd119c78b8866afaa9ab404db6/c87c79e44bc19d59e29800776e01825c.webp", 
        caption="⚕️ Xodjayeva Nodira Vahidovna - fizioterapevt, endokrinolog, diyetolog, 12 yil tajribaga ega shifokor. Onlayn yoki telefon orqali qabulga yozilish"
    )
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_button = InlineKeyboardButton("KOPROQ MALUMOT", callback_data='more_info2')
    inline_button2 = InlineKeyboardButton("MANZIL", callback_data='other_info2')
    inline_keyboard.add(inline_button,inline_button2)

    # Ma'lumotlarni yuboramiz
    await message.answer(text="Kattalarni qabul qiladi\n\nTashkilot: shahar klinik kasalxonasi №15\nManzil: Toshkent, O'zbekiston\nLavozimi:kordiolog ",
                         reply_markup=inline_keyboard)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info2')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,     text = """
                           Ish davri 1995-2003
Respublika ixtisoslashtirilgan kardiologiya ilmiy-amaliy tibbiyot markazi tashkiloti
Manzil: Toshkent, O'zbekiston

Bo'lim boshlig'i lavozimi
2003 - 2019
Evro Servis tashkiloti (Uchtepa tumani)
Manzil: Toshkent, O'zbekiston
Lavozimi: diyetolog

Ish davri: 2020 yil-hozir vaqt
Ta'lim / o'quv kurslari: Trening turi
Ta'lim muassasasi: Oliy o'quv yurti
toshkent davlat tibbiyot instituti

Fakultet / Yo'nalish / Bo'lim: Bundan tashqari
Davolash: Bakalavr darajasi
Ixtisoslashuv: O'qish davri: diyetolog 1984 - 1990
Ilmiy yutuqlar: Malaka
Ilmiy daraja-birinchi toifadagi shifokor
""")   
# Botni ishga tushuramiz

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info2')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" Ayol Care - Ayollar salomatligi markazi klinikasi, Toshkent: 30 shifokor, 13 sharhlar. Onlayn yoki telefon orqali qabulga yozilish. """ 
    )

    await bot.send_location(callback_query.from_user.id, latitude=41.307398, longitude=69.303614) 












@dp.message_handler(lambda message: message.text == 'NERVOLOG')
async def button3_handler(message: types.Message):
    # Inline buttonni yaratamiz
  
    # Foto va matn yuboramiz
    await bot.send_photo(
        chat_id=message.chat.id, 
        photo="https://med24.uz/upload/resize_cache/webp/iblock/a46/262_172_1c01a1ffd119c78b8866afaa9ab404db6/a465a0fd7edf3b30ec910cba348a2ad9.webp", 
        caption="⚕️ Aslanyan Arsen Utkurovich - nevrolog, 31 yil tajribaga ega oliy toifali shifokor, 3 fikr-mulohaza. Onlayn yoki telefon orqali qabulga yozilish"
    )
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_button = InlineKeyboardButton("KOPROQ MALUMOT", callback_data='more_info3')
    inline_button2 = InlineKeyboardButton("MANZIL", callback_data='other_info3')
    inline_keyboard.add(inline_button,inline_button2)

    # Ma'lumotlarni yuboramiz
    await message.answer(text="Kattalarni qabul qiladi\n\nTashkilot: Franc medic\nManzil: Toshkent, O'zbekiston\n nevrolog ",
                         reply_markup=inline_keyboard)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'more_info3')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,     text = """
                           Ish davri 1995-2003
Respublika ixtisoslashtirilgan kardiologiya ilmiy-amaliy tibbiyot markazi tashkiloti
Manzil: Toshkent, O'zbekiston

Bo'lim boshlig'i lavozimi
2003 - 2019
Evro Servis tashkiloti (Uchtepa tumani)
Manzil: Toshkent, O'zbekiston
Lavozimi: nervolog

Ish davri: 2020 yil-hozir vaqt
Ta'lim / o'quv kurslari: Trening turi
Ta'lim muassasasi: Oliy o'quv yurti
toshkent davlat tibbiyot instituti

Fakultet / Yo'nalish / Bo'lim: Bundan tashqari
Davolash: Bakalavr darajasi
Ixtisoslashuv: O'qish davri: nervolog 1984 - 1990
Ilmiy yutuqlar: Malaka
Ilmiy daraja-birinchi toifadagi shifokor
""")   
# Botni ishga tushuramiz

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'other_info3')
async def more_info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text=""" 🏥 Frank Medic klinikasi, Toshkent: 12 shifokor, 28 sharhlar. Onlayn yoki telefon orqali qabulga yozilish. """ 
    )

    await bot.send_location(callback_query.from_user.id, latitude=41.307398, longitude=69.303614) 




















































# ChatGPT uchun xabar javobi handler
@dp.message_handler()
async def chatgpt_response(message: types.Message):
    response = openai.Completion.create(
        engine=ENGINE_ID,
        prompt=f"User: {message.text}\nBot: ",
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
        api_key=OPENAI_API_KEY
    ).choices[0].text

    # Agar javob 4096 belgidan uzun bo'lsa, bir nechta xabar qilib yuborish
    if len(response) > 4096:
        await message.reply(response[:4096])
        await message.reply(response[4096:])
    else:
        await message.reply(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
