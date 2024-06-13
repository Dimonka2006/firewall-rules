import shutil
import os


# Путь к каталогу, куда будут скопированы файлы
dst = 'home/programfid/app/works'

# Создание каталога, если он еще не существует
if not os.path.exists(dst):
    os.makedirs(dst)
    
# Список путей к файлам, которые нужно скопировать
files_to_copy = ['var/log/secure', 
                 'var/log/secure-20240512',
                  'var/log/secure-20240519',
                  'var/log/secure-20240526', 
                  'var/log/secure-20240602']


# Копирование каждого файла из списка
for file in files_to_copy:
    shutil.copy(file, dst)

# Изменение владельца файла или каталога, добавление прав
os.chown(dst, 'programfid', 'programfid')
os.chmod(dst, 0o755)

from os import listdir
from os.path import isfile, join

# Список всех файлов и папок в директории
files_and_folders = [f for f in listdir(dst) if isfile(join(dst, f))]

# Функция для изменения прав доступа и владельца
def change_permissions_and_owner(path):
    try:
        # Изменяем права доступа
        os.chmod(dst, 0o755)
        print("Изменены права доступа для {}".format(dst))
        
        # Изменяем владельца
        os.chown(dst, 'programfid', 'programfid')
        print("Владелец изменен для {}".format(dst))
    except Exception as e:
        print("Произошла ошибка при изменении прав доступа или владельца для {}: {}".format(path, e))

# Перебираем все файлы и папки
for file_or_folder in files_and_folders:
    file_or_folder_path = join(dst, file_or_folder)
    change_permissions_and_owner(file_or_folder_path)

