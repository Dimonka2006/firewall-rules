import shutil
import subprocess

# Список путей к файлам, которые нужно скопировать
files_to_copy = ['var/log/secure', 
                 'var/log/secure-20240512',
                  'var/log/secure-20240519',
                  'var/log/secure-20240526', 
                  'var/log/secure-20240602']

# Путь к каталогу, куда будут скопированы файлы
dst = 'home/programfid/app/works'

# Создание каталога, если он еще не существует
if not os.path.exists(dst):
    os.makedirs(dst)

# Копирование каждого файла из списка
for file in files_to_copy:
    shutil.copy(file, dst)

# Добавление всех полномочий file_admin.sh

# Путь к файлу .sh
script_path = 'file_admin.sh'

# Запуск скрипта .sh
subprocess.call([script_path])

#f = open('secure', 'r')