# Скопировать из файла F1 в файл F2 все строки, начинающиеся на букву «А», расположенные между строками с номерами N1 и N2.
# Определить количество слов в первой строке файла F2.
import os


def copy2file():
    with open('F1', 'r') as file1:
        N1 = int(input('Введите номер строки с которой начать вывод текста :'))
        N2 = int(input('Введите номер строки на которой закончить вывод текста :'))
        with open('F2', 'w') as file2:
            for i, line in enumerate(file1):
                if i > N1 - 1:
                    # print(i,line)
                    file2.write(line)
                    if i == N2 - 1:
                        break

        file2.close()
    file1.close()


copy2file()
