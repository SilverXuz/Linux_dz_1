"""
Задание 2. (повышенной сложности)

Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный
режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации
(их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе.
"""

import subprocess
import string


def run_command_and_check_text(command, text_to_check, check_word=False):
    try:
        # Выполняем команду и захватываем вывод
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)

        # Если требуется режим проверки слов без знаков пунктуации
        if check_word:
            # Удалите знаки пунктуации из текста
            translator = str.maketrans('', '', string.punctuation)
            output = output.translate(translator)
            # Разбиваем вывод на слова
            words = output.split()

            # Проверяем, содержится ли слово (без знаков пунктуации) в выводе
            if text_to_check in words:
                return True
            else:
                return False
        else:
            # Проверяем, содержит ли вывод указанный текст
            if text_to_check in output:
                return True
            else:
                return False
    except subprocess.CalledProcessError:
        # Если команда завершилась с ошибкой, возвращаем False
        return False


# Пример использования для поиска текста
command = "ls /tmp"  # Замените на нужную команду
text_to_find = "example.txt"  # Замените на текст, который вы хотите найти

result = run_command_and_check_text(command, text_to_find)

if result:
    print("Текст найден в выводе команды.")
else:
    print("Текст не найден в выводе команды.")

# Пример использования для поиска слова без знаков пунктуации
command = "echo 'Hello, world!'"
word_to_find = "world"  # Замените на слово, которое вы хотите найти

result = run_command_and_check_text(command, word_to_find, check_word=True)

if result:
    print("Слово найдено в выводе команды.")
else:
    print("Слово не найдено в выводе команды.")
