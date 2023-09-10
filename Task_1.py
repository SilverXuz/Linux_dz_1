"""
Задание 1.

Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и
False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать
не нужно.
"""

import subprocess


def run_command_and_check_text(command, text_to_check):
    try:
        # Выполняем команду и захватываем вывод
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)

        # Проверяем, содержит ли вывод указанный текст
        if text_to_check in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        # Если команда завершилась с ошибкой, возвращаем False
        return False


# Пример использования:
command = "ls /tmp"  # Замените на нужную команду
text_to_find = "example.txt"  # Замените на текст, который вы хотите найти

result = run_command_and_check_text(command, text_to_find)

if result:
    print("Текст найден в выводе команды.")
else:
    print("Текст не найден в выводе команды.")
