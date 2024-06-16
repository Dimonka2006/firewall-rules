

#filename = input("Enter correct file name")
#inputfile = "filename"

inputfile = "secure"
outputfile = "work.txt"

myfile = open(inputfile, 'r', encoding='utf-8')
myfile2 = open(outputfile, 'w', encoding='utf-8') 
for line in myfile:
    if "invalid" in line:
        #print(str(line))
        myfile2.write(str(line))
            

myfile.close()
myfile2.close()


import re
from collections import defaultdict

# Путь к исходному текстовому файлу
source_file = 'work.txt'

# Путь к новому текстовому файлу, куда будут сохранены уникальные IP-адреса
output_file = 'logfile.txt'

# Словарь для хранения уникальных IP-адресов
unique_ips = defaultdict(bool)

# Открытие исходного файла для чтения
with open(source_file, 'r', encoding='utf-8') as file:
    # Чтение содержимого файла
    content = file.read()

# Закрытие исходного файла
file.close()

# Регулярное выражение для поиска IPv4 адресов
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# Поиск всех совпадений в содержимом файла
for match in ip_pattern.finditer(content):
    # Получение найденного IP-адреса
    ip = match.group()
    
    # Проверка, является ли IP-адрес уникальным
    if not unique_ips[ip]:
        # Добавление IP-адреса в список уникальных IP-адресов
        with open(output_file, 'a+') as out_file:
            out_file.write(f'{ip}\n')
        unique_ips[ip] = True
        print("generatad logfile.txt")

# Закрытие нового файла
out_file.close()

import subprocess

# Путь к файлу с IP-адресами, каждый адрес на новой строке
ip_file = 'logfile.txt'

# Путь к файлу, куда будут сохранены команды iptables
rules_file = 'rules.txt'

# Открываем файл для записи команд iptables
with open(rules_file, 'w') as rules_file_obj:
    # Открываем файл с IP-адресами для чтения
    with open(ip_file, 'r') as ip_file_obj:
        # Читаем все строки файла с IP-адресами
        for line in ip_file_obj:
            # Удаляем символ новой строки в конце каждой строки
            ip = line.strip()
            
            # Формируем команду iptables
            command = f'iptables -A INPUT -s {ip} -j DROP'
            
            # Записываем сформированную команду в файл с правилами
            rules_file_obj.write(f'{command}\n')
            print("Generatad rules.txt")
