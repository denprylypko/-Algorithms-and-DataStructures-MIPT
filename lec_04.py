def hello():
	print('hello world')


hello()
f = hello 	#ссылка на hello()
f()

#Функции с параметрами
def hello(name='Human'):
	print('hello', name)

hello('John') 	#hello John
hello('Alice') 	#hello Alice
hello()  	  		#hello Human

def max2(x,y):
	if x>y:
		return x
	return y
result = max2(13,25)
print(result)


def max3(x,y,z):
	return max2(x, max2(y,z))
result = max3(5,13,25)
print(result)

print(max3('ab', 'abc', 'abd'))
#Duck typing - утиная типизация

#Именнованые параметры
def hello_separated(name='Human', separator ="-"):
	print('Hello', name, sep=separator)

hello_separated('Alice') 			#Hello-Alice
hello_separated(separator='***') 	#Hello***Human

'''
Стек вызова (граф вызова): main->А()->B()->C()->D()

call-stack
|	 |
|  C |
|  B |
|  A |
|main|
|____|
'''
#-------------------------------

# import graphics as gr

# def built_house(window, upper_left_corrner, width):
# 	"""Функция, которая рисует дом"""
# 	height = calculate_height(width)

# window = gr.GraphWin('Russian game', 100,100)
# built_house(window, gr.Point(100,100), 100)
# print('Урра! Дом построен!')


def is_simple_number(x):
	""" Определяет, является ли число простым.
		x - целое положительное число.
		Если простое, то возвращает True, иначе - Faslse.
	"""
	divisor = 2
	while divisor < x:
		if x%divisor == 0:
			return False
		divisor += 1
	return True
print(2**31 - 1)
print(is_simple_number(13))

def fuctorize_number(x):
	""" Раскладывает число на моножетили.
		Печатает их  на экран.
		x - целое положительное число.
	"""
	divisor = 2
	while x > 1:
		if x%divisor == 0:
			print(divisor, end='\t')
			x //= divisor
		else:
			divisor += 1
print(fuctorize_number(25))


# розклад числа на прості множники
a = 336 	#int(input())
i = 2
print('Число\tМножник')
while True:
	if(a%i == 0):
		a = a/i
		print(a, '\t', i)
		if(a == 1):
			break
	else:
		i += 1