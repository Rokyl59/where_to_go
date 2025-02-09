# Описание

Проект представляет из себя демо-версию сайта-карты города Москва, на которой точками отмечены главные туристические места города, кликнув по которым, пользователь сможет посмотреть картинки этого места, а также изучить необходимую информацию о нем.

Ссылка на [сайт](https://rokyl.pythonanywhere.com/)

## Установка и настройка проекта

### Клонирование репозитория
Сначала клонируйте репозиторий с проектом на свой локальный компьютер:

```bash
git clone https://github.com/Rokyl59/where_to_go
```

### Установка Python и зависимостей

__Проверка Python__

Убедитесь, что у вас установлен Python версии 3.8 или выше. Проверить версию Python можно командой:

```bash
python --version
```

__Установка виртуального окружения__

Создайте и активируйте виртуальное окружение, чтобы избежать конфликтов с другими проектами:

```bash
python -m venv venv
source venv/bin/activate  # для Windows используйте команду venv\Scripts\activate
```

__Установка зависимостей__

Установите все необходимые библиотеки, указанные в файле `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Настройка переменных окружения
Создайте рядом с файлом `settings.py` файл `.env` и поместите в него следующие переменные окружения:

```bash
SECRET_KEY=<ваш секретный ключ>
DEBUG=True
ALLOWED_HOSTS=<>

```

* __SECRET_KEY__ - Секретный ключ должен быть большой случайной величиной, и он должен храниться в секрете. Убедитесь, что ключ, используемый в производстве, больше нигде не используется, и избегайте его фиксации в системе управления исходными текстами. Это уменьшает количество векторов, по которым злоумышленник может получить ключ.Вместо того чтобы жестко кодировать секретный ключ в модуле настроек, можно загрузить его из переменной окружения

* __DEBUG__ - Вы наверняка разрабатываете свой проект с DEBUG = True, поскольку это позволяет использовать такие удобные функции, как полная трассировка в браузере. Однако для производственной среды это очень плохая идея, поскольку при этом происходит утечка большого количества информации о вашем проекте: фрагменты исходного кода, локальные переменные, настройки, используемые библиотеки и т.д.

* __ALLOWED_HOSTS__ - Когда DEBUG = False, Django вообще не работает без подходящего значения для ALLOWED_HOSTS. Этот параметр необходим для защиты вашего сайта от некоторых CSRF-атак. Если вы используете подстановочный знак, вы должны выполнить собственную проверку HTTP-заголовка Host или иным образом убедиться, что вы не уязвимы для этой категории атак.


## Настройка базы данных

__Создание и применение миграций__

Примените миграции для настройки базы данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Наполнение сайта

Сайт принимает на вход `JSON` файл со всеми необходимыми данными о каждой из локаций, который выглядит следующим образом:

```bash
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

* Наполните сайт:

```bash
python manage.py load_place http://адрес/файла.json
```

Данные можно получить [здесь](https://github.com/devmanorg/where-to-go-places/tree/master/places).

## Запуск

```bash
python manage.py runserver
```

## Результат

![277332231-ff428108-5063-4768-bf47-2fe8b6a8a3f3](https://github.com/user-attachments/assets/c19f0b9b-c73f-44de-b0fd-f7ee20d4b0e9)




