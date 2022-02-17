"""У рекурсии дожжен быть:
	-рекурентный случай
	-крайний случай
	
	Глубина рекурсии - количество вызовов функции
"""
# def matryoshka(n):
# 	if n == 1:
# 		print('Матрёшечка')
# 	else:
# 		print("Верх матрешки n=", n)
# 		matryoshka(n-1)
# 		print("Низ матрешки n=", n)

# matryoshka(5)
# import graphics as gr
# import time
# window = gr.GraphWin('Fractal Rectangle', 600, 600)
# alpha = 0.166
# def fractal_rectangle(A, B, C, D, deep=30):
# 	if deep < 1:
# 		return
# 	# gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
# 	# gr.Line(gr.Point(*B), gr.Point(*C)).draw(window) 
# 	# gr.Line(gr.Point(*C), gr.Point(*D)).draw(window) 
# 	# gr.Line(gr.Point(*D), gr.Point(*A)).draw(window) --s>
# 	for M, N in (A, B), (B, C), (C, D), (D, A):
# 		gr.Line(gr.Point(*M), gr.Point(*N)).draw(window) 
# 	#A1x = (1-alpha)*Ax + alpha*Bx
# 	A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
# 	B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
# 	C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
# 	D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)

# 	fractal_rectangle(A1, B1, C1, D1, deep-1)


# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))
# time.sleep(1000)
# # x = input()
#--------------------------------------------------------------------

# import graphics as gr
# import time
# window = gr.GraphWin('Fractal Hexagon', 600, 600)
# alpha = 0.166
# def fractal_rectangle(A, B, C, D, E, F, deep=30):
# 	if deep < 1:
# 		return
# 	# gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
# 	# gr.Line(gr.Point(*B), gr.Point(*C)).draw(window) 
# 	# gr.Line(gr.Point(*C), gr.Point(*D)).draw(window) 
# 	# gr.Line(gr.Point(*D), gr.Point(*A)).draw(window) --s>
# 	for M, N in (A, B), (B, C), (C, D), (D, E), (E, F), (F, A):
# 		gr.Line(gr.Point(*M), gr.Point(*N)).draw(window) 
# 	#A1x = (1-alpha)*Ax + alpha*Bx
# 	A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
# 	B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
# 	C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
# 	D1 = (D[0]*(1-alpha) + E[0]*alpha, D[1]*(1-alpha) + E[1]*alpha)
# 	E1 = (E[0]*(1-alpha) + F[0]*alpha, E[1]*(1-alpha) + F[1]*alpha)
# 	F1 = (F[0]*(1-alpha) + A[0]*alpha, F[1]*(1-alpha) + A[1]*alpha)

# 	fractal_rectangle(A1, B1, C1, D1, E1, F1, deep-1)


# fractal_rectangle((100, 100), (300, 0), (500, 100), (500, 400),(300, 500), (100, 400))
# time.sleep(1000)
# # x = input()
#---------------------------------------------------------------------------------------------------

#Факториал
"""	n! = (n-1)!*n
	f(n) = 1, n <= 1
	f(n) = f(n)*n, n>1
"""
# def factorial(n:int):
# 	assert n >= 0, "Факториал отрицательных неопределён"
# 	if n == 0:
# 		return 1
# 	else:
# 		return factorial(n-1)*n

# print(factorial(1))
#----------------------------------
# def fibonachi(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	return fibonachi(n-2) + fibonachi(n-1)

# print(fibonachi(8))
#-----------------------------------------

#Алгоритм Евклида
#Наибольшое кратное A i B - 
#Поиск наибольшого общего делителя A i B

#Grand common divisor(GCD) - #Наибольший общий делитель
"""	НОД(a,b) = НОД(a-b, b)
	gsd(a,b) = a, a = b
	gsd(a,b) = gcd(a-b,b), a > b
	gsd(a,b) = gcd(a,b-a), a < b

#-------------VAR2------------------
	НОД(a,b) = НОД(b, a%b)
	gsd(a,b) = a, a = b
	gsd(a,b) = gcd(a-b,b), a > b
	gsd(a,b) = gcd(a,b-a), a < b

"""
#Наибольший общий делитель var1
# def gcd(a, b):
# 	if a == b:
# 		return a
# 	elif a > b:
# 		return gcd(a-b, b)
# 	else: #a<b
# 		return gcd(a, b-a)

# print(gcd(12, 16))
# #Наибольший общий делитель var 2
# def gcd(a, b):
# 	if b == 0:
# 		return a
# 	else:
# 		return gcd(b, a%b)

# print(gcd(12,16))
# #Наибольший общий делитель var3
# def gcd(a, b):
# 	return a if b == 0 else gcd(b, a%b)

# print(gcd(12,16))
#---------------------------------------------------

""" Быстрое возведение в степень, n>0
Обычное:
a^n = a*a*a*...*a, n-раз

Рекурентное:
a^n = a^(n-1)*a
a^0 = 1
pow(a, n) = 1, n = 0
pow(a, n) = pow(a, n-1)*a, n > 0

Если степень чётная - n = 2k:
a^2k = (a^2)^k
a6n = (a^2)^(n/2)
"""
# def pow(a:float, n:int):
# 	if n == 0:
# 		return 1
# 	else:
# 		return pow(a, n-1)*a

# """Если степень чётная - n = 2k:
# 	a^2k = (a^2)^k
# 	a^n = (a^2)^(n/2)

# 	pow(a, n) = 1, n = 0
# 	pow(a, n) = pow(a, n-1)*a, n > 0 #n - нечётное
# 	pow(a^2, n//2)					 #n - чётное
# """
# #Быстрое возведение в степень, n>0
# def fast_pow(a:float, n:int):
# 	if n == 0:
# 		return 1
# 	elif n%2 == 1:				#нечётные
# 		return fast_pow(a, n-1)*a
# 	else:						#чётные
# 		return fast_pow(a**2, n//2)

# # print(pow(2,995))
# #print(fast_pow(2,995))


"""Ханойские башни

|	|	|
---------
k 	i 	tmp
1 	2 	3
 k + i + tmp = 1 + 2 + 3 = 6
 tmp = 6 - k - i

 Перекладываем из столбца К на столбец tmp пирамидку размером (n-1)
 Из k-того столбца на і-тый столбец перекладываем n-ый блин
 Потом перекладываем пирамидку (n-1) на і-тый столбец
"""