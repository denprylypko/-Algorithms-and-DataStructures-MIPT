#Lecture 1
x = "hello"
print(type(x))

x = 1+3+3*2
print(type(x))

#Обмен переменных значениями через 1 доп. переменную:
a = 2
b = 5

tmp = a
a = b
b = tmp

#Обмен переменных значениями через 2 доп. переменных:
a = 2
b = 5

tmp1 = b
tmp2 = a
a = tmp1
b = tmp2

#Каскадное присваивание
x=y=z=0
#Множественное присваивание:
x,y,z = 1,2,3

#Обмен переменных значениями через кортеж:
tmp1, tmp2 = b, a
a, b = tmp1, tmp2

#Или просто:
a,b = b, a

arr = [11, 12, 13, 14, 15, 16, 17 ,18, 19 , 20]
# a = (i**2 for i  in range (1,5))
a = (i**2 for i  in arr)
b = (i for i  in arr)

for i,j in zip(a,b):
	print(f'{i}+{j} = {(i+j)%10}')


print(-11//10) #-2 -> -20//10 == -2 
print(-11%10)  #9  -> -11%10 == 20 +(-11) == 9

#------------------------------------------
x = 3
# x = int(input('input x: '))
while x>0:
	y = x
	while y>0:
		print(y)
		y -= 1
	x -= 1

# if условие:
# 	оператор_1
# else:
# 	оператор_2

for x in range(1,10,1):
	print(x**2)

range(start, stop, step) #range(1,10,1) [1;10)
#-------------------------------------------------
