import re

# Регулярное выражение для IP-адресов с нулевым четвёртым октетом
zero_fourth_octet_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.0\b')


# Функция для обработки IP-адресов
def process_ip_addresses(input_file, file_with_zero_octet, file_with_other_octets):
    with open(input_file, 'r') as infile, \
            open(file_with_zero_octet, 'w') as outfile_zero, \
            open(file_with_other_octets, 'w') as outfile_other:

        zero_octet_count = 0
        other_octet_count = 0

        # Чтение строк файла
        for line in infile:
            ip = line.strip()  # Убираем пробелы и символы новой строки
            if zero_fourth_octet_pattern.search(ip):
                outfile_zero.write(ip + '\n')
                zero_octet_count += 1
            else:
                outfile_other.write(ip + '\n')
                other_octet_count += 1

        # Возвращаем количество строк в каждом файле
        return zero_octet_count, other_octet_count


# Входные и выходные файлы
input_file = 'ip_address.txt'
file_with_zero_octet = 'zero_octet_ips.txt'
file_with_other_octets = 'other_ips.txt'

# Обрабатываем файл
zero_count, other_count = process_ip_addresses(input_file, file_with_zero_octet, file_with_other_octets)

# Выводим результаты
print(f"Количество строк с нулевым четвертым октетом: {zero_count}")
print(f"Количество остальных строк: {other_count}")
