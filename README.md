# polls_api_test
## Запуск

- Клонируйте репозиторий

```bash
git clone https://github.com/olegush/polls_api_test.git
cd polls_api_test
```

- Переименуйте env.txt в .env

- Соберите и запустите проект
```bash
docker-compose up --build
```

- Откройте http://127.0.0.1:8000/admin с правами суперпользователя: admin/pwd12345

## Функционал администратора

- Добавьте [опросы](http://127.0.0.1:8000/admin/polls/poll/), [вопросы](http://127.0.0.1:8000/admin/polls/question/) и [ответы](http://127.0.0.1:8000/admin/polls/answer/) к ним.
- Результаты опросов будут [здесь](http://127.0.0.1:8000/admin/polls/vote/)

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


  