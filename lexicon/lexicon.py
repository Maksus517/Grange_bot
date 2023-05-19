LEXICON_RU: dict[str, str] = {
    '/start': '📋 /help - справка о боте\n\n'
              '📚 /info_resources - информационные ресурсы\n\n'
              '📇 /assist_user - вспомогательные функции\n\n'
              '🎮 /games - игры\n\n'
              '📲 /support - обратная связь\n\n'
              '⬇️ Все команды так же доступны в Меню',

    '/help':  '✅ Бот сделан на основе ИИ, в простом общении может отвечать на любые вопросы.\n'
              '✅ Так же у бота есть свой функционал, он доступен при отправке соответствующей команды, '
              'все команды так же доступны в Меню в нижней, левой части экрана.\n'
              '✅ Проект постоянно развивается, появляется новый функционал, улучшается его работа, '
              'все это делается для удобства использования бота.\n\n'
              '❗️ Вы так же можете поучаствовать в развитии бота, оставив отзыв, комментарий или предложение '
              'по развитию функционала проекта\n📲 /support',

    '/info_resources':  '<b>✅ Тут вы можете получать различную информацию, узнать погоду за окном, '
                        'прочитать свежие новости и многое другое.</b>\n\n'
                        '<b>⬇️ Ниже представлен список сервисов, выберите нужный вам:</b>',

    '/assist_user': '✅ Вы можете воспользоваться одной из функций, просто нажав на кнопу:',

    '/games': 'В процессе разработки',

    '/support': '✅ Ты вы можете поддержать проект, оставить свой отзыв, комментарий, '
                'предложения по улучшению проекта, его расширению',

    'wiki':   '🔍 Википедия',

    'open_weather': '⛅ Погода',

    'message_mp3': '🔊 Преобразовать текст в mp3',

    'translator': '📝 Перевод текста',

    'news': '📺 Новости',

    'joke': '😆 Анекдоты',

    'message_mp3_answer': '🖊 Введите текст, который необходимо преобразовать в голосовой формат',

    'button_no_info': '❌ Выход',

    'no_text': 'ℹ️ Если будут нужны какие-то функции, воспользуйтесь кнопкой "Menu"',

    'button_back': '🔙 Назад'
}


LEXICON_INFO_RU: dict[str, str] = {
    'back_press_button': '❓ Хотите воспользоваться чем-то еще?'
}


LEXICON_WIKI_RU: dict[str, str] = {
    'wiki_press_button': '❓ Что вы хотите узнать?\n'
                         'Введите текст:',

    'leave_here_wiki_press_button': '❓ Хотите узнать что-то еще?',

    'wiki_answer_state': 'Пожалуйста подождите секундочку...',

    'wiki_answer_no_found': '🚫 К сожалению не удалось найти информацию о',

    'wiki_error_answer': '❗️ <b>Вы находитесь в блоке "Википедия"</b>\n'
                         'Если хотите еще узнать какую-либо информацию из Википедии нажмите кнопку <b>"Еще!"</b>.\n'
                         'Что бы выйти в информационный блок нажмите кнопку <b>"Назад"</b>.\n'
                         'Если хотите завершить работу с информационным блоком нажмите кнопу <b>"Выход"</b>'
}


LEXICON_WEATHER_RU: dict[str, str] = {
    'open_weather_press_button': '🌇 Выберите название города. Если вашего города нет в списке, напишите его в чат',

    'leave_here_open_weather': '🌃 Хотите узнать погоду в другом городе?',

    'open_weather_state': 'Пожалуйста подождите...',

    'city_no_found': '🚫 Вы ввели некорректное название города...\n'
                     '❓ Хотите попробовать еще?',

    'open_weather_error_answer': '❗️ <b>Вы находитесь в блоке "Погода"</b>\n'
                                 'Что бы узнать погоду в другом городе нажмите кнопку <b>"Продолжить"</b>\n'
                                 'Что бы выйти в информационный блок нажмите кнопку <b>"Назад"</b>.\n'
                                 'Если хотите завершить работу с информационным блоком нажмите кнопу <b>"Выход"</b>'
}


LEXICON_JOKE_RU: dict[str, str] = {
    'joke_no_found': '⬇️ Вы прочитали все анекдоты, попробуйте посмотреть позже...\n'
                     '❓ <b>Что-то еще?</b>'
}


LEXICON_MENU_RU: dict[str, str] = {
    '/help': '📋 Справка о работе бота',

    '/info_resources': '📚 Информационные ресурсы',

    '/assist_user': '📇 Вспомогательные функции',

    '/games': '🎮 Игры',

    '/support': '📲 Обратная связь'
}


LEXICON_ADMIN_RU: dict[str, str] = {
    '/admin': 'Вы вошли в админ панель',

    'deleted_menu': 'Удалить кнопку меню',

    'no_button_admin': 'Выйти из админ панели',

    'no_text': 'Вы выши из админ панели'
}


LEXICON_SUPPORT_RU: dict[str, str] = {
    'comment': '✍️ Оставить отзыв, пожелание',

    'button_comment_data_base': '👇 Написать тут',

    'button_comment_to_mail': '✉️ Написать на почту',

    'comment_data_base': '🖊 Напишите текст или нажмите кнопку "Назад"',

    'comment_press_button': '✅ Вы можете отправить отзыв о работе бота, '
                            'какие-либо предложения по развитию его функционала, и т.д.',

    'error_comment_developers': '❗️ Вы находитесь в блоке <b>"Отзывы"</b>.\n'
                                'Вы можете отправить отзыв на почту, оставить еге тут '
                                'или выйти, нажав на соответствующие кнопки ниже:',

    'comment_save': '✅ Спасибо за отзыв!\n'
                    '⬇️ Можете воспользоваться другими функциями:',

    'button_support_project': '🤝 Поддержать проект'
}

LEXICON_TRANSLATOR_RU: dict[str, str] = {
    'translator_press_button': '👇 Выберите язык с которого будем переводить:',

    'language_choice_one': '👇 Выберите язык на который будем переводить:',
    
    'input_text_translator': '🖊 Введите текст для перевода:',

    'unwrap_language_translator': '⤵️ Развернуть',

    'collapse_language_translator': '⤴️ Свернуть',

    'again_translator_press_button': '❓ Хотите перевести что-то еще?',

    'again_translator_button': '✅ Еще!',

    'again_translator_error': 'Что-то пошло не так, попробовать еще раз?'
}

LEXICON_GAMES_RU: dict[str, str] = {
    'arcade_games': '🕹 Аркады',

    'rpg_games': '🌄 Ролевые игры'
}


LEXICON_ARCADE_GAMES_RU: dict[str, str] = {
    'arcade_games_choice': 'в какую игру хотите сыграть?',
    'rpg_games_choice': 'В разработке...',
    'knb_game': '🤜🤛 Камень, ножницы, бумага',
    'guess_number_game': 'Угадай число',
    'KNB_button': 'Камень, ножницы, бумага',
}

LEXICON_KNB_GAME_RU: dict[str, str] = {
    'knb_press_button': 'Отлично!\n\n Делайте свой выбор!',
    'rock': '✊ Камень',
    'paper': '🖐 Бумага',
    'scissors': '✌️ Ножницы',
    'button_knb_again': '✅ Сыграть еще!',
    'statistics_knb': 'Статистика',
    'bot_choice': 'Мой выбор',
    'bot_won': 'Я победил!\n\nСыграем еще?',
    'user_won': 'Ты победил! Поздравляю!\n\nДавай сыграем еще?',
    'nobody_won': 'Ничья!\n\nПродолжим?',
    'kmb_game_error': 'Сейчас мы играем, если хотите выйти нажмите кнопку "Назад"'
}
