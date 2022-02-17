A = [1, 2, 3, 4, 5]

for x in A:
	print(x, end='\t')
	x+=1			#x = x + 1 = 2: x сылается на новый объект - 2
	print(x)

print(A) #Масив не поменяет значений
#Числа - неизменяемый тип

for k in range(len(A)):
	A[k] = A[k]*A[k]
	print(f'{k}\t{A[k]}')

print(A) #При доступе к элементам массива по индексу, массив поменяет значения


#Заполнение массива
A = [0]*1000
top = 0
x = int(input()) # 1, 2, 3, 4, 5
while x != 0:
	A[top] = x
	top += 1
	x = int(input())

print(A)

for k in range(4, -1, -1):
	print(A[k])
import random

N = 5
A = [0]*N
B = [0]*N
for k in range(N):
	A[k] = random.randint(0,9)#int(input())

print(A)

#Копирование массива
for k in range(N):
	B[k] = A[k]

print(B)
C = A

print(A is C) #TRUE
print(A is B) #False
A[0] = 777 #Изменяется А и С, но не В
print(C[0])
#Для создания нового списка нужно вызвать явно конструктор списка list:

C = list(A)
print(A is C) #False

#Линейный поиск в массиве

def array_search(A:list, N:int, x:int):
	""" Осуществляет поиск числа х в массиве А
		от 0 до N-1 включительно.
		Возвращает индекс элемента х в массиве А.
		Если элемента нет - возвращает -1.
		Если в массиве несколько одинаковых элементов,
		равных х, то вернуть индекс первого оп счету.

	"""
	for k in range(N):
		if A[k] == x:
			return k

	return -1



def test_array_search():
	A1 = [1, 2, 3, 4, 5]
	# A1 = [i for i in range(6)]
	m = array_search(A=A1, N=5, x=8)
	if m == -1:
		print('#test1 - ok')
	else:
		print('#test1 - fail')


	A2 = [-1, -2, -3, -4, -5]
	# A1 = [i for i in range(6)]
	m = array_search(A=A2, N=5, x=-3)
	if m == 2:
		print('#test2 - ok')
	else:
		print('#test2 - fail')


	A3 = [10, 20, 30, 10, 10]
	# A1 = [i for i in range(6)]
	m = array_search(A=A3, N=5, x=10)
	if m == 0:
		print('#test3 - ok')
	else:
		print('#test3 - fail')


test_array_search()


#Алгоритм обращения массива
def invert_array(A:list, N:int):
	for k in range(N//2):
		A[k], A[N-k-1] = A[N-k-1], A[k]

def test_invert_array():
	A1 = [1, 2, 3, 4, 5]
	print(A1)
	invert_array(A1, 5)
	print(A1)
	if A1 == [5, 4, 3, 4, 1]:
		print('#test1 - ok')
	else:
		print('#test1 - fail')


	A2 = [0, 0, 0, 0, 0, 0, 0, 10]
	print(A2)
	invert_array(A2, 8)
	print(A2)
	if A == [10, 0, 0, 0, 0, 0, 0, 0]:
		print('#test2 - ok')
	else:
		print('#test2 - fail')


test_invert_array()

# Циклический сдвиг
A = [1, 2, 3, 4, 5]
N = len(A)-1
#Влево
# tmp = A[0]
# for k in range(N):
# 	A[k] = A[k+1]
# A[N] = tmp
# print(A)

#Вправо
tmp = A[N]
for k in range(N,-1,-1):
	A[k] = A[k-1]
A[0] = tmp
print(A)

#Решето Эратосфена
N = 100
A = [True]*N
A[0] = A[1] = False
for k in range(2,N):
	if A[k]:
		for m in range(2*k, N, k):
			A[m] = False

for k in range(N):
	print(k,'-','простое' if A[k] else "составное")







