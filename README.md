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


## Подключен GitHub Actions
после команды 

```commandline
git push
```
* проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final;
* сборка и доставка докер-образа для контейнера web на Docker Hub;
* автоматический деплой проекта на боевой сервер;
* отправка уведомления в Telegram о том, что процесс деплоя успешно завершился.

![example workflow](https://github.com/maxahist/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# url проекта
51.250.27.210


### Авторы проекта
* https://github.com/maxahist
* https://github.com/Egor5061
* https://github.com/Aenika

