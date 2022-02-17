x = 0b1011 		#2
y = 0o0732		#8	
z = 0xFA03		#16

t = int('Z3F', base=36)
print(t)

x = 127
print(bin(x))
print(oct(x))
print(hex(x))

#Первод числа в систему исчичсления
base = 7
# x = int(input())
x = 8
s =''
while x>0:
	digit = x%base
	s += str(digit)
	# print(digit, end='')
	x//=base
print(s[::-1])

#Однопроходные алгоритмы		[]
# подсчкет			n			0			n+=1
# сумма				s			0			n+=x
# произведение		p			1 			p*=x
# максимум			m			- 			m1=max(m0, x)	if x>m: m = x
# поиск числа		flag		False		f = f or x==x0
#-----------------------------------------------------------------------------