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


