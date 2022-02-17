flag = False
print(type(flag))

# n = int(input())
n = 5
for i in range(n):
	x = int(input())
	# if x%10==0
	# 	flag = True
	flag = (x%10==0) or flag
#-------------------------------

flag = True
n = int(input())
for i in range(n):
	x = int(input())
	flag =(flag and x%10==0)

#Вложенные и последовательные if:
x = int(input())

if x%2==0:
	print('yes')
if x%3==0:
	print('yes')
#-----------------
if x==1:
	print('one')
if x==2:
	print('two')
#=>
if x==1 or x==2:
	print('yes')
#---------------

if x%2==0:
	if x%3==0:
		print('делится на 6')

#=>

if x%2==0 and x%3==0:
	print('делится на 6')
else:
	print('не делится на 6')

#Каскадные условные конструкции
#Если число (-ꝏ,0) - A
#Если число [0,5) - B
#Если число [5,10) - С
#Если число [5,+ꝏ) - D
x = 10
if x<0:
	print('A')
elif x<5: #x>=0
	print('B')
elif x<10: #x>=5
	print('C')
# elif x>= 10:
# 	print('D')
else:
	# print('imposible')
	raise Exception('imposible')

#-----------------------------
#Определить в какой четверти находится число(x;y)
#2|1
#---
#3|4

if y>0:
	if x>0:
		print('1')
	else:
		print('2')
else:
	if x<0:
		print('3')
	else:
		print('4')
#---------------------------