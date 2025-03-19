### README (Russian)

#### Название проекта
**Простой Telegram-бот**

#### Описание
Этот проект представляет собой Telegram-бота, написанного на Python с использованием библиотеки `telebot`. Бот отвечает на команды `/start`, `/help`, `/joke` и реагирует на текстовые сообщения, такие как "привет", "как дела" и "пока". При команде `/joke` бот отправляет случайную шутку из заранее заданного списка.

#### Требования
- Python 3.x
- Библиотека `telebot` (`pip install pyTelegramBotAPI`)
- Файлы конфигурации:
  - `config.py` с переменной `BOT_TOKEN` (токен вашего бота от @BotFather)
  - `messages.py` с текстовыми сообщениями (`start_message`, `help_message`)
  - `jokes.py` с массивом `KNOWN_JOKES` (список шуток)

#### Установка
1. Установите Python на ваш компьютер.
2. Установите библиотеку `telebot`:
   ```bash
   pip install pyTelegramBotAPI
   ```
3. Создайте файлы:
   - `config.py`:
     ```python
     BOT_TOKEN = "ваш_токен_бота"
     ```
   - `messages.py`:
     ```python
     start_message = "Привет! Я простой бот."
     help_message = "Используй команды: /start, /help, /joke"
     ```
   - `jokes.py`:
     ```python
     KNOWN_JOKES = ["Шутка 1", "Шутка 2", "Шутка 3"]
     ```
4. Сохраните основной код в файл, например, `bot.py`.

#### Использование
1. Запустите бота:
   ```bash
   python bot.py
   ```
2. Откройте Telegram и найдите вашего бота по его имени.
3. Используйте команды:
   - `/start` — приветственное сообщение.
   - `/help` — помощь по командам.
   - `/joke` — случайная шутка.
4. Напишите "привет", "как дела" или "пока" для дополнительных ответов.

#### Автор
Создано с помощью Grok 3 от xAI на основе кода пользователя.

---

### README (English)

#### Project Name
**Simple Telegram Bot**

#### Description
This project is a Telegram bot written in Python using the `telebot` library. The bot responds to commands `/start`, `/help`, `/joke` and reacts to text messages like "hello", "how are you", and "bye". When the `/joke` command is used, the bot sends a random joke from a predefined list.

#### Requirements
- Python 3.x
- `telebot` library (`pip install pyTelegramBotAPI`)
- Configuration files:
  - `config.py` with a `BOT_TOKEN` variable (your bot token from @BotFather)
  - `messages.py` with text messages (`start_message`, `help_message`)
  - `jokes.py` with an array `KNOWN_JOKES` (list of jokes)

#### Installation
1. Install Python on your computer.
2. Install the `telebot` library:
   ```bash
   pip install pyTelegramBotAPI
   ```
3. Create the following files:
   - `config.py`:
     ```python
     BOT_TOKEN = "your_bot_token"
     ```
   - `messages.py`:
     ```python
     start_message = "Hello! I'm a simple bot."
     help_message = "Use commands: /start, /help, /joke"
     ```
   - `jokes.py`:
     ```python
     KNOWN_JOKES = ["Joke 1", "Joke 2", "Joke 3"]
     ```
4. Save the main code in a file, e.g., `bot.py`.

#### Usage
1. Run the bot:
   ```bash
   python bot.py
   ```
2. Open Telegram and find your bot by its name.
3. Use the commands:
   - `/start` — welcome message.
   - `/help` — command help.
   - `/joke` — random joke.
4. Type "hello", "how are you", or "bye" for additional responses.
