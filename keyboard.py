from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def level_keyboard():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="Level 1️⃣"), KeyboardButton(text="Level 2️⃣"))
    rkm.add(KeyboardButton(text="Level 3️⃣"), KeyboardButton(text="Level 4️⃣"))
    return rkm

def stop_keyboard():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="🛑 stop"))
    return rkm