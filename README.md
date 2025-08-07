# 🧮 Mini Excel

Минималистичное веб-приложение, имитирующее работу с таблицей Excel. Поддерживает редактирование строк, копирование, несколько листов, конфликты редактирования, авторизацию пользователей и админку для управления доступом.

---

## 🚀 Возможности

- 📄 Редактирование таблиц с именованными столбцами
- 🗂 Несколько листов (вкладок)
- 🔐 Авторизация пользователей (JWT)
- 🛡️ Разграничение прав доступа (чтение/запись)
- ⚠️ Разрешение конфликтов при редактировании
- 🛠 Админка для управления пользователями и листами
- 🌗 Переключение светлой/тёмной темы
- 🔍 Поиск и вставка данных из других листов

---

## 🧰 Стек технологий

| Компонент     | Технология           |
|---------------|----------------------|
| Backend       | FastAPI, SQLAlchemy  |
| База данных   | PostgreSQL           |
| Frontend      | React + TypeScript   |
| Авторизация   | JWT (python-jose)    |
| Контейнеризация | Docker + Docker Compose |
| Прокси и HTTPS | Nginx + Let's Encrypt |

---

## 📦 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/denis-on/min-exel.git
cd min-exel
```

### 2. Создай .env файл
```Env
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
POSTGRES_DB=excel_db
DATABASE_URL=postgres://user:pass@db:5432/excel_db
```

### 3. Запусти проект
```Bash
docker-compose up --build
```
## 🌐 Деплой на сервер

1. Установи Docker, Docker Compose, Nginx, Certbot
2. Настрой nginx как reverse proxy
3. Получи HTTPS-сертификат:

```Bash
sudo certbot --nginx -d yourdomain.com
```

4. Запусти проект:
```Bash
docker-compose up -d --build
```
## 📁 Структура проекта

```
mini-excel/
├── backend/           # FastAPI backend
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/          # React frontend
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── .env
├── docker-compose.yml
└── README.md
```

## 🛠 TODO
* [ ] Импорт/экспорт CSV
* [ ] История изменений строк
* [ ] Редактирование структуры столбцов
* [ ] Уведомления в реальном времени (WebSocket)

