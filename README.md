# polls_api_test
## Установка

- Требуется Python 3.8 и библиотеки из requirements.txt. Лучше использовать виртуальное окружение.
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

- Создайте базу данных Postgres, пользователя и выдайте ему права

```bash
postgres=# CREATE DATABASE DB_NAME;
postgres=# CREATE USER DB_USER WITH PASSWORD 'PWD';
postgres=# GRANT ALL PRIVILEGES ON DATABASE "DB_NAME" to DB_USER;
```

- Переименуйте файл env.txt в .env и добавьте параметры подключения к Postgres

- Примените миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
- Создайте суперпользователя
```bash
python manage.py createsuperuser
```
## Функционал администратора

- Запустите сервер
```bash
python manage.py runserver
```
- Зайдите на http://127.0.0.1:8000/admin/ под созданным суперюзером
- Добавьте [опросы](http://127.0.0.1:8000/admin/polls/poll/), [вопросы](http://127.0.0.1:8000/admin/polls/question/) и [ответы](http://127.0.0.1:8000/admin/polls/answer/) к ним.

## API для пользователей
- Все активные опросы:
 GET http://127.0.0.1:8000/polls/questions/
 
- Конкретный опрос:
 GET http://127.0.0.1:8000/polls/questions/POLL_ID/

- Прохождение опроса:
POST http://127.0.0.1:8000/polls/votes/
```
{
    "user": USER_ID,
    "poll": POLL_ID,
    "question": QUESTION_ID,
    "vote_answers": [ANSWER_ID_1, ANSWER_ID_2], 
    "custom_answer": "CUSTOM_ANSWER_TEXT"
}
```
- Результаты опросов конкретного пользователя:
http://127.0.0.1:8000/polls/votes/USER_ID/


  