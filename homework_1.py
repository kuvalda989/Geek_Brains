#First exercise 

words_1 = ['разработка', 'сокет', 'декоратор']

for word in words_1:
	print('==================Primary word')
	print(word)
	print(type(word))
	print('================Encoding str to bytes')
	byte_word = bytes(word, 'utf-8')
	print(byte_word)
	print(type(byte_word))
	print('================Decoding bytes to str')
	word_utf = byte_word.decode('utf-8')
	print(word_utf)

# Second exercise
words_2 = [b'class', b'function', b'method']


for word in words_2:
	print('==================Primary word')
	print(word)
	print(type(word))
	print(len(word))

#Third exercise 
# words_3 = [b'attribute', b'класс', b'function', b'type'] <===  b'класс' невозможно записать


#Fourth exercise

words_4 = ['attribute', 'класс', 'protocol', 'standart']

for word in words_4:
	print('\n\n==================Primary word')
	print(word)
	print('================Encoding str to bytes')
	word_byte = word.encode()
	print(word_byte)
	print('================Decoding bytes to str')
	word = word_byte.decode()
	print(word)


#Fifth exercise


import subprocess

hosts = ['google.com', 'youtube.com', 'yandex.ru']
# args = ['ping', '-c 1', hosts]
for host in hosts: 
	args = ['ping', '-c 1', host]
	subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
	for line in subproc_ping.stdout:
		print(line.decode('cp866'))



#sixth exercise

with open('test_file.txt', 'w', encoding='cp866') as file:
	words=['сетевое программирование', ' сокет', ' декоратор']
	for word in words:
		file.write(word)

import sys
print('====================Default coding')
print(sys.getfilesystemencoding())

with open('test_file.txt', 'rb') as file:
	print(file.read().decode('cp866'))


with open('test_file.txt', 'rb') as file:
	try:
		print(file.read().decode('utf-8'))
	except UnicodeDecodeError as r:
		print(r)




