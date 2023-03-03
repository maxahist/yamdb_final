# Проект api_yamdb
Данный проект - для создания отзывов на произведения, через API запросы, с возможностью написать, скорректировать и читать отзыв, а также комментировать отзывы. На основе отзывов формируется рейтинг произведения

### Установка
Для корректной работы проекта:
* клонируйте репозиторий
 ```
git clone git@github.com:Aenika/api_yamdb.git

```
* создайте виртуальное окружение
```
python3 -m venv env
```
* активируйте окрудужение
```
source env/bin/activate
```
*установите все зависимости
```
pip install -r requirements.txt
```
*Проведите все миграции
```
python3 manage.py migrate
```
*Готово! Теперь можно запустить проект.
```
python3 manage.py runserver
```

###Подробно ознакомитсья с документацией проекта можно по ссылке (при запущенном проекте)
```
[python3 manage.py runserver](http://127.0.0.1:8000/redoc/)
```
### Примеры API запросов

http://127.0.0.1:8000/api/v1/auth/signup/
Регистрация нового пользователя. Обязательные поля: email, username
http://127.0.0.1:8000/api/v1/titles/
Список всех произведений, к которым пишут отзывы. POST-запрос возможен только от администратора
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
GET-запрос: получение списка всех отзывов к конкретному произведению, при POST-запросе - добавление нового отзыва.
Возможно частичное обновление отзыва по адресу:
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
Редактировать отзыв могут автор, модератор, админ
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
Список всех комментариев к отзыву, зарегистрированные пользователи могут прокомментировать отзыв.

## Шаблон наполнения .env 
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=secretkey
```

## Описание команд для запуска в контейнерах

* Запускаем контейнеры:
```commandline
docker-compose up -d --build
```
* Выполеяем миграции в контейнере web:
```commandline
docker-compose exec web python manage.py migrate
```
* Создаем суперпользователя: 
```commandline
docker-compose exec web python manage.py createsuperuser
```
* Собирам статику:
```commandline
docker-compose exec web python manage.py collect static
```

## Заполнение бызы данных
```commandline
docker-compose exec web python manage.py loaddata fixtures.json
```

### Авторы проекта
* https://github.com/maxahist
* https://github.com/Egor5061
* https://github.com/Aenika

