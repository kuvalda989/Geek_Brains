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


