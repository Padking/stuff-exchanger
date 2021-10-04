# Stuff Exchange
Командный проект № 2 курса от Devman

## Описание

Бот-посредник в обмене вещей

## Особенности

* позволяет добавить вещь для обмена,
* осуществляет поиск и подбор вещи к обмену,
* предлагает пользователю оценить вещь,
* выполняет [приоритезацию](https://github.com/Padking/stuff-exchanger/wiki#%D0%9F%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F),
* высылает _username'ы_ 2-ум совпавшим в желании обменяться пользователям.

### Начало работы

* Получить токен у [@BotFather](https://t.me/botfather),
* Настроить управление ботом через интерфейс [@BotFather](https://t.me/botfather):
    - присвоить имя боту,
    - указать список [команд](https://github.com/Padking/stuff-exchanger#%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

### Структура проекта

- скрипт бота `bot.py` предназначен для ...:
    + 

- модуль `bots_helper.py` ...:
    + 

- модуль `entities_worker.py` ...:
    + 

- модуль `storage_worker.py` ...:
    + 

### Типовой сценарий использования

  Отправить команду `/add_stuff` для добавления вещи к обмену:
  ![add_stuff](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/add_stuff.png)
  
  
  Добавить фото вещи:

  ![add_stuffs_photo](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/add_stuffs_photo.png)


  Добавить название вещи:

  ![add_stuffs_name](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/add_stuffs_name.png)
  

  Поиск вещи:

  ![search_stuff](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/search_stuff.png)


  Оценивание вещи:

  ![stuffs_assesment](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/stuffs_assesment.png)


  Обмен вещи:

  ![exchange_stuff](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/exchange_stuff.png)


  Совпадение желаний пользователей:

  ![users_matching](https://github.com/Padking/stuff-exchanger/blob/master/screenshots/users_matching.png)


## Сценарии использования

### Ограничения общие
- Команды, пригодные для работы с ботом, доступны в телеграм-интерфейсе чата с ботом,
- Пользователь, начинающий работу с ботом, должен иметь _username_ - так он сможет держать связь с потенциальным продавцом,
- текст, отмеченный в сценариях большими буквами.

### № 1
Процесс добавления вещи в хранилище:
- отправить команду `/add_stuff`. В ответ получить сообщение о порядке действий для добавления вещи;
- отправить фото вещи, нажав значок "скрепка", без указания подписи к фото;
- ВСЛЕД ЗА ПРЕДЫДУЩИМ СООБЩЕНИЕМ, отправить название вещи;

### № 2
#### Ограничения
- чтобы просматривать вещи других Пользователей, [донор](https://github.com/Padking/stuff-exchanger/wiki#%D0%9F%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F) должен добавить
    хотя бы одну вещь в [хранилище](https://github.com/Padking/stuff-exchanger/wiki#%D0%9F%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F),
- в хранилище должно быть больши или равно одного Пользователя (не считая [акцептора](https://github.com/Padking/stuff-exchanger/wiki#%D0%9F%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F))
- не оценивать несколько раз подряд вещь, присылаемую на однократную посылку команды `/search_stuff`

Процесс поиска вещи в хранилище и выдачи для потенциального обмена:
* часть 1-я (без оценивания):
    - отправить команду `/search_stuff`. В ответ получить фото с названием вещи и клавиатурой для оценивания.
    - повторно отправить команду `/search_stuff`, если вещь не подлежит оценке
* часть 2-я (с оцениванием):
    - отправить команду `/search_stuff`. В ответ получить фото с названием вещи и клавиатурой для оценивания.
    - оценить вещь, нажав на одну из 2-ух предлагаемых кнопок с надписями: _like_ или _dislike_

### № 3
Процесс приоритезации:
- отправить команду `/exchange_stuff`. В ответ получить сообщение о наличии приоритетного донора.

### № 4
Процесс поиска совпадений желаний:


## Требования к окружению

* Python 3.x,
* Linux/Windows,
* ПеО.

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [pydantic[dotenv]](https://pydantic-docs.helpmanual.io/usage/settings/#dotenv-env-support).

#### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`TELEGRAM_BOT_TOKEN`| Токена телеграм-бота |-|
|`TELEGRAM_GOODS_PHOTO_DIR`| Каталог, в котором создаётся _/photos_ для хранения фото, присланных боту |-|
|`USERS_OBJ_FIELDS`| Поля `User` |`["user_id", "username", "goods", "assesments"]`|
|`ASSESMENTS_OBJ_FIELDS`| Поля `Assesment` |`["user_id", "good_id", "sign"]`|
|`SHELVE_FILENAME`| Название хранилища |-|
|`BOTS_START_CMD`| Название команды боту |start|
|`BOTS_ADD_STUFF_CMD`| Название команды боту |add_stuff|
|`BOTS_SEARCH_CMD`| Название команды боту |search_stuff|
|`BOTS_EXCHANGE_CMD`| Название команды боту |exchange_stuff|
|`BOTS_HELP_CMD`| Название команды боту |help|

### Установка

1. Общая часть:
- Клонирование проекта,
- создание каталога виртуального окружения (ВО)*,
- связывание каталогов ВО и проекта,
- установка зависимостей,
```bash
git clone https://github.com/Padking/stuff-exchanger.git
cd stuff-exchanger
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

### Пример запуска
```bash
$ python bot.py
INFO:aiogram:Bot: Mediator [@stuffexchanger8_bot]
WARNING:aiogram:Updates were skipped successfully.
INFO:aiogram.dispatcher.dispatcher:Start polling.
```


\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
