# Book Service API

REST API для книжного магазина на FastAPI с PostgreSQL.

## Стек технологий

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 (async)
- Alembic
- Pydantic v2
- JWT аутентификация

## Структура проекта

```
app/
├── main.py           # Точка входа
├── config.py         # Настройки
├── database.py       # Подключение к БД
├── models.py         # SQLAlchemy модели
├── schemas.py        # Pydantic схемы
├── crud.py           # Функции работы с БД
├── security.py       # JWT и хеширование паролей
├── dependencies.py   # FastAPI зависимости
└── routers/
    ├── auth.py       # Аутентификация
    ├── books.py      # Книги
    ├── authors.py    # Авторы
    └── orders.py     # Заказы
```

## Быстрый старт

### С Docker (рекомендуется)

```bash
# Клонировать репозиторий
git clone https://github.com/prettypaperjet/BookService.git
cd BookService

# Создать .env файл
cp .env.example .env

# Запустить контейнеры
docker-compose up --build
```

API будет доступен по адресу: http://localhost:8000

Swagger UI: http://localhost:8000/docs

### Локально (без Docker)

```bash
# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt

# Настроить переменные окружения
cp .env.example .env
# Отредактировать .env, указав DATABASE_URL для локальной PostgreSQL

# Применить миграции
alembic upgrade head

# Запустить сервер
uvicorn app.main:app --reload
```

## API Endpoints

### Аутентификация

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | /auth/register | Регистрация пользователя |
| POST | /auth/login | Вход (получение JWT токена) |

### Книги

| Метод | Endpoint | Описание | Доступ |
|-------|----------|----------|--------|
| GET | /books | Список книг (пагинация, фильтрация) | Все |
| GET | /books/{id} | Информация о книге | Все |
| POST | /books | Добавить книгу | Admin |
| PATCH | /books/{id} | Обновить книгу | Admin |
| DELETE | /books/{id} | Удалить книгу | Admin |

### Авторы

| Метод | Endpoint | Описание | Доступ |
|-------|----------|----------|--------|
| GET | /authors | Список авторов | Все |
| GET | /authors/{id} | Автор с его книгами | Все |
| POST | /authors | Создать автора | Admin |

### Заказы

| Метод | Endpoint | Описание | Доступ |
|-------|----------|----------|--------|
| POST | /orders | Оформить заказ | Авторизованные |

## Примеры запросов

### Регистрация

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "email": "user@example.com", "password": "secret123"}'
```

### Вход

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "secret123"}'
```

### Получение списка книг

```bash
curl http://localhost:8000/books?limit=10&offset=0
```

### Создание заказа

```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"book_id": 1, "quantity": 2}'
```

## Тестирование

```bash
# Установить зависимости для тестов
pip install -r requirements.txt

# Запустить тесты
pytest
```

## Миграции

```bash
# Создать новую миграцию
alembic revision --autogenerate -m "description"

# Применить миграции
alembic upgrade head

# Откатить последнюю миграцию
alembic downgrade -1
```
