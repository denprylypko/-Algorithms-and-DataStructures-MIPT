""" Сортировка слиянием
	Устойчивость сортировки:
	Устойчивая сортировка - сортировка, которая не меняет порядок равных элемметов
"""

#Слияние отсортированых массивов в один
# def merge(A:list, B:list):
# 	C = [0]*(len(A)+len(B)) #n - index C #i - index A, k - index B
# 	i = k = n = 0
# 	while i < len(A) and k < len(B):
# 		if A[i] <= B[k]:
# 			C[n] = A[i]
# 			i += 1
# 			n += 1
# 		else:
# 			C[n] = B[k]
# 			k += 1
# 			n += 1
# 	while i < len(A):
# 		C[n] = A[i]
# 		i += 1
# 		n += 1
# 	while k<len(B):
# 		C[n] = B[k]
# 		k += 1
# 		n += 1
# 	return C


# #Рекурентная(Рекурсивная) функция:
# def merge_sort(A:list):		#сортирует этот же массив, а !не возвращает новый
# 	#крайний случай
# 	if len(A) <= 1:
# 		return
# 	middle = len(A)//2
# 	L = [A[i] for i in range(0, middle)]
# 	R = [A[i] for i in range(middle, len(A))]
# 	merge_sort(L)
# 	merge_sort(R)
# 	C = merge(L,R)
# 	for i in range(len(A)):
# 		A[i] = C[i]


# import random
# arr = [8,11,1,15,-4,9, 11, 134,14,16,901, 5, 2]#[random.randint(0,9) for i in range(10)]
# print(arr)
# merge_sort(arr)
# print(arr)

#-----------------------------------------------------------------------------------------

#Сортировка Тони Хоара (Quick Sort)
""" Первый элемент - барьерный
"""
# def hoar_sort(A:list): #Сортирует по ссылке
# 	#крайний случай
# 	if len(A) <= 1:
# 		return 		# return None
# 	barrier = A[0]
# 	L = []
# 	R = []
# 	M = []
# 	for x in A:
# 		if x < barrier:
# 			L.append(x)
# 		elif x == barrier:
# 			M.append(x)
# 		else:	# x > barrier
# 			R.append(x)
# 	hoar_sort(L)
# 	hoar_sort(R)
# 	k = 0
# 	for x in L + M + R:
# 		A[k] = x
# 		k += 1
# 	# for i in range(len(A)):
# 	# 	A[i] = A1[i]
# 	# hoar_sort(A1)


# arr = [8, 11, 1, 15, -4, 9, 11, 134, 14, 16, 91, 5, 2, 0]#[random.randint(0,9) for i in range(10)]
# hoar_sort(arr)
# print(arr)
#--------------------------------------------------------------------------------------------------

#проверка упорядочености массива за О(п)
# def check_sorted(A, ascending=True):
# 	"""Проверка отсортированости за O(len(A))"""
# 	flag = True
# 	for i in range(0, N-1):
# 		s = 2*int(ascending) -1
# 		if s*A[i] > s*A[i+1]:
# 			flag = False
# 			break
# 	return flag

#----------------------------------------------------------------
#Бинарный поиск в массиве - массив отсортирован
""" A = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 7, 7, 7, 7]
	left_bound - левая граница: >= -1
	right_bound - правая граница: <=len(A)
	middle = (left_bound + right_bound) //2
	if middle < searched:
		left = middle
"""
	
