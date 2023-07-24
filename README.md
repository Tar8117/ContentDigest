# Микросервис для формирования дайджеста контента

Микросервис, который формирует дайджесты контента для пользователей на 
основе их подписок и популярности постов. Дайджест представляет собой выборку 
постов из различных источников, на которые подписан пользователь.

## Запуск:
Склонируйте репозиторий:

```bash
git@github.com:Tar8117/ContentDigest.git
```

Создайте и активируйте venv:

Linux:
```bash 
python3 -m venv venv
```
```bash 
source venv/bin/activate
```
Windows:
```bash 
python -m venv venv
```
```bash 
source venv\Scripts\activate
```

Установите зависимости из файла `requirements.txt`:
```bash 
pip install -r requirements.txt
```

Выполните миграции:
```bash 
python manage.py makemigrations
python manage.py migrate
```


Загрузите данные в БД из файла `data.json` находясь в корневой директории:
```bash 
python manage.py loaddata data.json
```

Запустите сервер:
```bash 
python manage.py runserver
```

Теперь можете воспользоваться приложением  `postman` и отправить
`GET-запрос` на эндпоинт `create_digest/<int:user_id>/`, а именно
на `http://127.0.0.1:8000/create_digest/2/` и получить дайджест, сформированный
на основе подписок пользователя и популярности постов.

P.S. Сейчас в БД только два пользователя, но вы можете создать пользователей,
добавить посты, источники, добавить подписку и проверить формирование 
дайджеста.

Для этого создайте суперпользователя:
```bash 
python manage.py runserver
```

И перейдите в `http://127.0.0.1:8000/admin/`
