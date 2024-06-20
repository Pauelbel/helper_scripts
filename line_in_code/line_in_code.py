import os

# Функция для подсчета не пустых строк в файле
def count_non_empty_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        non_empty_lines = [line for line in lines if line.strip() != '']
        return len(non_empty_lines)

# Функция для сканирования файлов и папок
def scan_directory(root_dir, exclude_dirs=[]):
    total_non_empty_lines = 0
    for dirpath, _, filenames in os.walk(root_dir):
        
        # Проверяем, нужно ли исключить текущую папку из сканирования
        if any(exclude_dir in dirpath for exclude_dir in exclude_dirs):
            continue       
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                lines_count = count_non_empty_lines(file_path)
                total_non_empty_lines += lines_count
                print(f"Файл: {file_path}, Не пустых строк: {total_non_empty_lines}")
    return total_non_empty_lines


# Задаем корневую папку для сканирования
root_directory = '/home/pavel/Repositories/Helper-Scripts/'

# Задаем список папок, которые нужно исключить из сканирования
exclude_directories = ['venv']
# Вызываем функцию для сканирования и подсчета строк
total_lines = scan_directory(root_directory, exclude_directories)
print(f'Общее количество не пустых строк в .py файлах: {total_lines}')