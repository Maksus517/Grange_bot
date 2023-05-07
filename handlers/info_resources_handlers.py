from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, FSInputFile
import random

from lexicon import LEXICON_RU, LEXICON_INFO_RU
from services import get_wiki, get_weather, news_parser, joke_pars
from data import users_data, user_joke
from filters import FilterWiki, FilterOpenWeather
from keyboards import info_keyboard, open_weather_keyboard, assist_keyboard, assist_joke_keyboard

router_ih = Router()


@router_ih.callback_query(Text(text=['button_back']))
async def process_back_press_button(callback: CallbackQuery):
    await callback.message.edit_text(text='<b>Что-то еще?</b>',
                                     reply_markup=info_keyboard)
    users_data[callback.from_user.id]['user_status'] = None


# Кнопка выхода
@router_ih.callback_query(Text(text=['button_no_info']))
async def process_stop_info_press_button(callback: CallbackQuery):
    if callback.from_user.id in users_data:
        await callback.message.edit_text(text=LEXICON_RU['no_text'])
        users_data[callback.from_user.id]['user_status'] = None
    else:
        await callback.answer(text='Отправьте команду /start')


# Блок википедии
@router_ih.callback_query(Text(text=['wikipedia']))
async def process_wiki_button_press(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'wiki'
    global wiki_button_press
    wiki_button_press = await callback.message.edit_text(text=LEXICON_INFO_RU['wiki_answer'],
                                                         reply_markup=assist_keyboard)


@router_ih.message(FilterWiki(users_data))
async def process_wiki_answer(message: Message):
    wait_wiki = await message.answer(text='Пожалуйста подождите...')
    await wiki_button_press.delete()
    await wait_wiki.edit_text(text=get_wiki(message.text))
    await message.answer(text='<b>Что-то еще?</b>',
                         reply_markup=info_keyboard)
    users_data[message.from_user.id]['user_status'] = None


# Блок погоды
@router_ih.callback_query(Text(text=['open_weather']))
async def process_open_weather_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'open_weather'
    global open_weather_press_button
    open_weather_press_button = await callback.message.edit_text(text=LEXICON_INFO_RU['open_weather_answer'],
                                                                 reply_markup=assist_keyboard)


@router_ih.message(FilterOpenWeather(users_data))
async def process_open_weather_answer(message: Message):
    await open_weather_press_button.delete()
    wait_wiki = await message.answer(text='Пожалуйста подождите...')
    await wait_wiki.edit_text(text=get_weather(message.text))
    await message.answer(text='<b>Что-то еще?</b>',
                         reply_markup=info_keyboard)
    users_data[message.from_user.id]['user_status'] = None


# Блок новостей
@router_ih.callback_query(Text(text=['news']))
async def process_news_press_button(callback: CallbackQuery):
    news = news_parser()
    await callback.message.edit_text(text='4 последних новости:')
    for _ in range(4):
        await callback.message.answer(text=next(news))
    await callback.message.answer(text='<b>Что-то еще?</b>',
                                  reply_markup=info_keyboard)
    users_data[callback.from_user.id]['user_status'] = None


# Блок Анекдотов
@router_ih.callback_query(Text(text=['joke']))
async def process_joke_press_button(callback: CallbackQuery):
    joke = joke_pars()
    random.shuffle(joke)
    user_joke[callback.from_user.id] = joke
    try:
        await callback.message.edit_text(text=user_joke[callback.from_user.id][0],
                                         reply_markup=assist_joke_keyboard)
        del user_joke[callback.from_user.id][0]
    except Exception as ex:
        await callback.message.edit_text(text='Вы прочитали все анекдоты, попробуйте посмотреть позже...\n'
                                              '<b>Что-то еще?</b>',
                                         reply_markup=info_keyboard)
        print(ex)


@router_ih.callback_query(Text(text=['button_again_joke']))
async def process_joke_press_button(callback: CallbackQuery):
    try:
        await callback.message.edit_text(text=user_joke[callback.from_user.id][0],
                                         reply_markup=assist_joke_keyboard)
        del user_joke[callback.from_user.id][0]
    except Exception as ex:
        await callback.message.edit_text(text='Вы прочитали все анекдоты, попробуйте посмотреть позже...\n'
                                              '<b>Что-то еще?</b>',
                                         reply_markup=info_keyboard)
        print(ex)
