from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.callback_data import CallbackData

from config import Config


class Keyboards:
    locale_callback_data = CallbackData('locale', 'language_code')
    deposit_check_callback = CallbackData('check_dep', 'one_win_id')

    @staticmethod
    def get_welcome_menu() -> InlineKeyboardMarkup:
        next_button = InlineKeyboardButton(text='ACTIVATE BOT ✅', callback_data='next')
        return InlineKeyboardMarkup(row_width=1).add(next_button)

    @staticmethod
    def get_check_registration(user_id: int) -> InlineKeyboardMarkup:
        reg = InlineKeyboardButton(text='REGISTRATION 🤑', url=Config.get_registration_link(user_id=user_id))
        check_registration = InlineKeyboardButton(text='CONFIRM REGISTRATION 🔐', callback_data='check_registration')
        return InlineKeyboardMarkup(row_width=1).add(reg, check_registration)

    # @staticmethod
    # def get_check_deposit(user_id) -> InlineKeyboardMarkup:
    #     deposit = InlineKeyboardButton(text='TOP UP YOUR BALANCE', url=Config.get_registration_link(user_id=user_id))
    #     check = InlineKeyboardButton(text='TOPPED UP? PRESS HERE ✅', callback_data='check_deposit')
    #     return InlineKeyboardMarkup(row_width=1).add(deposit, check)

    @staticmethod
    def get_play() -> InlineKeyboardMarkup:
        game_url = 'https://stasmoons.github.io/GoodyWebApp/index.html'
        play = InlineKeyboardButton(text='START BOT 💸', web_app=WebAppInfo(url=game_url))
        return InlineKeyboardMarkup(row_width=1).add(play)

