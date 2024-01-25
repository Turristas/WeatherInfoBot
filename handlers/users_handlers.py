from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()  # Инициализируем роутер уровня модуля


@router.message(CommandStart())  # Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nДавай я подскажу погоду?\n\n'
        'Чтобы получить данные о погоде отправь город\n'
        'Например - <u>Dubai</u> или <u>Великий Устюг</u>\n\n'
        'Список команд - слева кнопка <b>Меню</b>\n'
        'Справка - отправьте команду /help',
        parse_mode='HTML'
    )


@router.message(Command(commands='help'))  # Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        f'раздел help на доработке '
    )


@router.message(Command(commands='support'))  # Этот хэндлер будет срабатывать на команду "/support"
async def process_help_command(message: Message):
    await message.answer(
        f'раздел support на доработке '
    )


@router.message(Command(commands='setup'))  # Этот хэндлер будет срабатывать на команду "/setup"
async def process_help_command(message: Message):
    await message.answer(
        f'раздел setup на доработке '
    )


@router.message(Command(commands='info'))  # Этот хэндлер будет срабатывать на команду "/info"
async def process_help_command(message: Message):
    await message.answer(
        f'Наш бот предоставляет актуальные данные о погоде в различных городах мира. '
        f'Просто укажите название города, и бот предоставит подробный прогноз погоды, '
        f'включая температуру, влажность, скорость ветра и другие важные параметры. '
        f'Получите мгновенный доступ к погодной информации без лишних усилий!'
    )


@router.message(F.content_type == 'photo')  # Этот хэндлер будет срабатывать на тип контента "photo"
async def process_send_photo(message: Message):
    await message.answer(text='Вы отправили фотографию, и, на данный момент,'
                              ' я не могу определить местоположение по фотографии. '
                              'Тем не менее, видно ваше старание, что заслуживает похвалы')


@router.message(F.content_type == 'voice')  # Этот хэндлер будет срабатывать на тип контента "voice"
async def process_send_voice(message: Message):
    await message.answer(text='Вы прислали voice, здесь пока нет распознавания голоса или изображения, '
                              'но мы учтем ваши пожелания.\n'
                              'Больше предложений отправляйте автору и создателю этого бота')


@router.message(F.content_type == 'video')
async def process_send_video(message: Message):
    await message.answer(text='Вы прислали видео, здесь пока нет распознавания голоса или изображения, '
                              'но мы учтем ваши пожелания.\n'
                              'Больше предложений отправляйте автору и создателю этого бота')
