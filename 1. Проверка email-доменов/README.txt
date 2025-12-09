Инструкция по запуску
Требования:
Python 3.6 или выше
Установленная библиотека dnspython
Установка:
bash
pip install dnspython
Способ 1: Запуск с аргументами командной строки
bash
python email_domain_checker.py test1@gmail.com test2@example.com test3@nonexistentdomain.xyz
Способ 2: Интерактивный ввод
bash
python email_domain_checker.py
Затем введите email-адреса по одному на строке. Для завершения ввода нажмите Enter дважды или Ctrl+D.
Способ 3: Чтение из файла
bash
python email_domain_checker.py $(cat emails.txt)
Или в Linux/Mac:
bash
cat emails.txt | xargs python email_domain_checker.py
Пример вывода:
text
Проверка MX-записей доменов
----------------------------------------

Проверка 3 email-адресов...

test@gmail.com: домен валиден
test@example.com: домен валиден
test@nonexistentdomain.xyz: домен отсутствует

Результаты сохранены в файл: email_check_results.txt
Особенности скрипта:
Проверяет корректность формата email-адреса
Проверяет существование домена через DNS-запись A
Проверяет наличие MX-записей
Обрабатывает таймауты и ошибки DNS
Сохраняет результаты в файл email_check_results.txt
Поддерживает ввод разными способами
