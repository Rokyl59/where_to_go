# Описание
Проект представляет из себя демо-версию сайта-карты города Москва, на которой точками отмечены главные туристические места города, кликнув по которым, пользователь сможет посмотреть картинки этого места, а также изучить необходимую информацию о нем.

### Установка зависимостей

```
pip install -r requirements.txt
```

### Переменные окружения
Создайте рядом с файлом `settings.py` файл `.env` и поместите в него следующие переменные окружения:

```bash
SECRET_KEY=<secret_key из настроек>
DEBUG=True
```

### Наполнение сайта

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

Наполните сайт:

```bash
python manage.py load_place http://адрес/файла.json
```

Данные можно получить [здесь](https://github.com/devmanorg/where-to-go-places/tree/master/places).

### Запуск

```bash
python manage.py runserver
```



