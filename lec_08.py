#Генерация всех перестановок
"""
{1,  2,  3, ..., N} - числа
1-я позиция: N-вариантов
2-я позиция: (N-1) - вариантов
...
(N-1) позиция: 2 - варианта
N-я позиция: 1 - вариант
Количество перестановок = N*(N-1)*...*2*1 = N!

----------------------------------------------
Упрощенная задача: N <= 10
Все числа от 00..0 до N-1...N-1
Рекурентное решение:
N - основание системы счисления
M - длина числа(количество цифр)
prefix - 
"""
# Для произвольной системы счисления
# def generate_numbers(N:int,M:int,prefix=None):
# 	""" Генерирует все числа (с лидирующими нулями)
# 		в N-ричной системе счисления (N<=10) длины М.
# 	"""
# 	prefix = prefix or [] #Если prefix==None, создастся [] пустой список
# 	if M == 0:
# 		print(prefix)
# 		return
# 	for digit in range(N):
# 		prefix.append(digit)
# 		generate_numbers(N, M-1, prefix)
# 		prefix.pop()
		
# generate_numbers(N=3,M=3)

# Вариант 1
#Только для двоичной системы счисления
# #Более простой ваиант:
# def gen_bin(M, prefix=""):
# 	if M == 0:
# 		print(prefix)
# 		return
# 	gen_bin(M-1, prefix+"0")
# 	gen_bin(M-1, prefix+"1")

# gen_bin(5)
# #---------------------------------


# # Вариант 2
# def gen_bin(M, prefix=""):
# 	if M == 0:
# 		print(prefix)
# 		return
# 	for digit in '0', '1':
# 		gen_bin(M-1, prefix+digit)

# gen_bin(3)

def find(number:int, numbers):
		""" Ищет number в numbers и возвращает True если number есть в numbers
			False - если number нет в numbers
		"""
		for num in numbers:
			if number == num:
				return True
		return False

# Перестановки
def generate_permutations(N:int, M:int=-1, prefix=None):
	"""Генерирует все перестановки N чисел в M позициях
		начиная с префикса prefix
	"""
	# M = M if M != -1 else N		# по умолчанию N чисел в N позициях
	M = N if M == -1 else M			# по умолчанию N чисел в N позициях
	prefix = prefix or []
	if M == 0:
		print(*prefix, end=', ', sep='')
		return
	for number in range(1, N+1):
		if find(number, prefix):
			continue
		prefix.append(number)
		generate_permutations(N, M-1, prefix)
		prefix.pop()

generate_permutations(5)
#--------------------------------------------------------------

# Рекурентные сортироки

# Быстрая сортировка Тони Хоара
"""	На случайной выборке скорость сортировки W(N*log(2)N)
	Сортирует хорошо на выборках до O(N^2)
	Сортирующее действие віполняется на прямом ходу рекурсии
	Может быть реализована без дополнительной памяти
	Относится к алгоритмам разделяй и властвуй

	A0 =	4  2  6  3  1  4  5
	A[0]=4 - баръерный элемент: возникает три групы элементов:
			 те кто больше, равны, меньше барьерного элемента:

	1) 2  3  1
	2) 4  4			- тех кто равны, сортировать не надо
	3) 6  6

	A1 = 2  3  1  4  4  6  5
"""


# Сортировка слиянием
""" На любой выборке скорость сортировки O(N*log(2)N)
	Сортирующее действие віполняется на обратном ходу рекурсии
	Требует запоминать сколько же элеметов, сколько их в масиве O(N)

	A0 =	4  2  6  3  1  4  5
	первая часть массива: от 0 до N//2 не включительно
	вторая часть массива: от N//2 включительно до N не включительно

	# A1 = 2  4  6 | 1  3  4  5
	В1 = [2, 4, 6]
	B2 = [1, 3, 4, 5]

	Дальше сравниваем 
	0: B1[0] и B2[0] = 2 и 1: 2>1 --> записываем 1 в новый массив
	1: B1[0] и B2[1] = 2 и 3: 2<3 --> дописываем 2 в масив
	2: B1[1] и B2[1] = 4 и 3: 4>3 --> дописиваем 3 в массив
	3: B1[1] и B2[2] = 4 и 4: 4==4 --> дописиваем 4 в массив
	4: B1[2] и B2[2] = 6 и 4: 6>4 --> дописиваем 4 в массив
	5: B1[2] и B2[3] = 6 и 5: 6>5 --> дописиваем 5 в массив
	6: B1[2] - больше чем любой элемент из отсортированого массива
				просто добавляем B1[2] в конец отсортированого массива


	А_sorted = [1,  2,  3,  4,  4,  5,  6]

"""