Инструкция по настройке:
1. Создание Telegram бота:
Найти в Telegram @BotFather
Отправить /newbot
Следовать инструкциям, получить токен бота
2. Получение Chat ID:
Добавить бота в приватный чат
Отправить любое сообщение боту
Перейти по ссылке: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
Найти chat.id в JSON-ответе
3. Настройка в n8n:
Шаг 1: Создать credentials для Telegram:
В ноде "Send to Telegram" нажать "Add Credentials"
Выбрать "Telegram Bot API"
Ввести:
Name: telegramBot (или любое другое)
Access Token: токен бота от BotFather
Шаг 2: Обновить параметры:
В ноде "Read Text File": указать полный путь к вашему файлу (например: C:\files\message.txt или /home/user/message.txt)
В ноде "Send to Telegram": указать ваш Chat ID
4. Запуск:
Сохранить workflow
Нажать "Execute Workflow"
Проверить, что сообщение пришло в Telegram
