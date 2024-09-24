import os
import shutil


# 1. Перейти в каталог pz11 и вывести список всех файлов в этом каталоге.
def list_files_in_pz11():
    os.chdir('pz11')  # Переход в каталог pz11
    print("Файлы в каталоге pz11:")
    for root, dirs, files in os.walk('.'):
        for file in files:
            print(file)
    os.chdir('..')  # Возвращаемся обратно в корень


# 2. Перейти в корень проекта, создать папку test, и тестовые файлы переместить.
def move_files_and_create_structure():
    if not os.path.exists('test'):
        os.mkdir('test')
    if not os.path.exists('test/test1'):
        os.mkdir('test/test1')

    # Перемещаем файлы из pz6 в test
    shutil.move('pz6/pz6_1.py', 'test/pz6_1.py')
    shutil.move('pz6/pz6_2.py', 'test/pz6_2.py')

    # Перемещаем файл из pz7 в test/test1 и переименовываем
    shutil.move('pz7/pz7_1.py', 'test/test1/test.txt')

    # Выводим размеры файлов в папке test
    print("\nРазмеры файлов в папке test:")
    for root, dirs, files in os.walk('test'):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"{file}: {os.path.getsize(file_path)} байт")


# 3. Найти файл с самым коротким именем в pz11 и вывести его
def find_shortest_filename_in_pz11():
    os.chdir('pz11')
    files = []
    for root, dirs, files_in_dir in os.walk('.'):
        files.extend(files_in_dir)

    shortest_file = min(files, key=len)
    print(f"\nСамый короткий файл в pz11: {os.path.basename(shortest_file)}")
    os.chdir('..')


# 4. Открыть PDF файл через os.startfile()
def open_pdf():
    os.chdir('reports')
    os.startfile('pz6.pdf')  # Открываем отчет в формате PDF
    os.chdir('..')


# 5. Удалить файл test.txt
def delete_test_file():
    test_file_path = 'test/test1/test.txt'
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
        print("\nФайл test.txt был успешно удален.")
    else:
        print("\nФайл test.txt не существует.")


# Выполнение всех шагов
list_files_in_pz11()
move_files_and_create_structure()
find_shortest_filename_in_pz11()
open_pdf()
delete_test_file()
