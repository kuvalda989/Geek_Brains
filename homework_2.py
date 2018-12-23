import csv
import json



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


with open('for_homework/info_1.txt') as f_n:
	f_n_content = csv.reader(f_n, delimiter=':')
	# obj = json.loads(f_n_content)
	f_n_write = []
	for line in f_n_content:
		f_n_write += line
	print(f_n_write)
	# obj = json.loads(f_n_write)
