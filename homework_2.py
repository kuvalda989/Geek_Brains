import csv
import json
import re
import os



''' 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
 Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
 Проверить работу программы через вызов функции write_to_csv().'''

# with open('for_homework/info_1.txt', encoding='cp1251') as f_n:
# 	f_n_reader = csv.reader(f_n)
# 	for row in f_n_reader:
# 		print(row)


# with open('for_homework/info_1.txt', encoding='cp1251') as f_n:
# 	f_n_reader = csv.reader(f_n)
# 	f_n_readers = next(f_n_reader)
# 	print('Headers: ', f_n_readers)
# 	for row in f_n_reader:
# 		print(row)


def get_data(file, enc):
	with open(file, encoding=enc) as f_n:
		f_n_reader = csv.reader(f_n, delimiter=':')
		os_prod_list = []
		os_name_list = []
		os_code_list = []
		os_type_list = []
		main_data = []
		for row in f_n_reader:
			#я понимаю, что ниже еще можно все скомпановать, но чет откровенно лень:) и так нифига не успеваю
			if re.search('Изготовитель системы', ' '.join(row)):
				os_prod_list += row
				print(type(os_prod_list))
				main_data.append(os_prod_list)
			elif re.search('Название ОС', ' '.join(row)):
				os_name_list += row
				main_data.append(os_name_list)
			elif re.search('Код продукта', ' '.join(row)):
				os_code_list += row
				main_data.append(os_code_list)
			elif re.search('Тип системы', ' '.join(row)):
				os_type_list += row
				main_data.append(os_type_list)
		return main_data
def write_to_csv(data):
	with open('data_' + file, 'w') as d:
		csv_data = csv.writer(d, quoting=csv.QUOTE_MINIMAL, delimiter=':')
		for l in data:
			print(type(l))
			csv_data.writerow(l)
	return data


# os.chdir('for_homework')
# files = os.listdir()
# print(files)
# for file in files:
# 	if file.startswith('info'):
# 		func = get_data(file, 'cp1251')
# 		write_to_csv(func)
# print(func)



# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:

# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.




import json

def write_order_to_json(item, quantity, price, buyer, data):
	data_dict = {'item':item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'data': data}
	with open('orders.json', 'a') as j_f:
		json.dump(data_dict, j_f, sort_keys=True,indent='    ')


json_func = write_order_to_json('snickers', 3, 13.22, 'unknown', 'nothing')
json_func = write_order_to_json('mars', 5, 6777, 'Dmitry', 'at 4:44')




# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:

# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.



import yaml

def write_order_to_yaml(list, int, dict):
	with open('order_yaml.yml', 'a') as y_f:
		yaml.dump(list, y_f, default_flow_style=False)
		yaml.dump(int, y_f, default_flow_style=False)
		yaml.dump(dict, y_f, allow_unicode = True,default_flow_style=False)


data_list = ['test', 1233, 'third item']
data_int = 10
data_dict = {'€':100, 'Ⓟ':'unknown simbol', '☊':'something'}

yaml_func = write_order_to_yaml(data_list, data_int, data_dict)
