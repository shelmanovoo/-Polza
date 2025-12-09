#!/usr/bin/env python3
"""
Скрипт для проверки MX-записей доменов email-адресов
"""

import dns.resolver
import sys
import re

def validate_email_format(email):
    """Проверка формата email-адреса"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_mx_records(domain):
    """Проверка MX-записей для домена"""
    try:
        # Проверяем существование домена через запись A
        try:
            dns.resolver.resolve(domain, 'A')
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return "домен отсутствует"
        
        # Проверяем MX-записи
        mx_records = dns.resolver.resolve(domain, 'MX')
        
        if len(mx_records) == 0:
            return "MX-записи отсутствуют или некорректны"
        
        # Проверяем, что есть хотя бы одна валидная MX-запись
        valid_mx = False
        for mx in mx_records:
            if mx.exchange.to_text() and mx.preference >= 0:
                valid_mx = True
                break
        
        if valid_mx:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
            
    except dns.resolver.NoAnswer:
        return "MX-записи отсутствуют или некорректны"
    except dns.resolver.Timeout:
        return "ошибка: таймаут при запросе"
    except Exception as e:
        return f"ошибка: {str(e)}"

def main():
    """Основная функция"""
    print("Проверка MX-записей доменов")
    print("-" * 40)
    
    # Вариант 1: Чтение email-адресов из аргументов командной строки
    if len(sys.argv) > 1:
        emails = sys.argv[1:]
    # Вариант 2: Ввод через stdin
    else:
        print("Введите email-адреса (по одному на строку). Для завершения введите пустую строку:")
        emails = []
        while True:
            try:
                email = input().strip()
                if not email:
                    break
                emails.append(email)
            except EOFError:
                break
    
    if not emails:
        print("Ошибка: не указаны email-адреса для проверки")
        print("\nИспользование:")
        print("  Способ 1: python email_domain_checker.py email1@example.com email2@test.org")
        print("  Способ 2: python email_domain_checker.py (и ввести адреса с клавиатуры)")
        return
    
    print(f"\nПроверка {len(emails)} email-адресов...\n")
    
    results = []
    for email in emails:
        email = email.strip()
        
        if not email:
            continue
            
        if not validate_email_format(email):
            print(f"{email}: неверный формат email-адреса")
            results.append(f"{email}: неверный формат email-адреса")
            continue
        
        domain = email.split('@')[1]
        status = check_mx_records(domain)
        
        result = f"{email}: {status}"
        print(result)
        results.append(result)
    
    # Сохраняем результаты в файл
    with open("email_check_results.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    
    print(f"\nРезультаты сохранены в файл: email_check_results.txt")

if __name__ == "__main__":
    # Проверяем наличие необходимой библиотеки
    try:
        import dns.resolver
    except ImportError:
        print("Ошибка: требуется установить библиотеку dnspython")
        print("Установите её командой: pip install dnspython")
        sys.exit(1)
    
    main()