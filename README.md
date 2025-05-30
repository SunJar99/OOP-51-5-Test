# Django Blog REST API

## Описание

REST API для простого блога на Django + DRF.

---

## Запуск через Docker

1. **Склонируйте репозиторий:**
   ```bash
   git clone <ваш-репозиторий>
   cd <ваша-папка>
   ```

2. **Постройте и запустите контейнер:**
   ```bash
   docker-compose up --build
   ```

3. **Откройте в браузере:**
   ```
   http://localhost:8000/
   ```

---

## Локальный запуск (без Docker)

1. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

4. **Создайте суперпользователя (по желанию):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

6. **Откройте в браузере:**
   ```
   http://localhost:8000/
   ```

---

## Документация API

Swagger доступен по адресу:
```
http://localhost:8000/swagger/
```

---

## Переменные окружения

- `DEBUG`
- `SECRET_KEY`

(см. `.env`)

---

## Контакты

Автор: [Ваше имя]
