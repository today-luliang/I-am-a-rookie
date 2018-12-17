Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(s):
	if s == [1,2,3,4,5]:
		for value in s:
			s = s + value
			return s

		
>>> s == [1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s == [1,2,3,4,5]
NameError: name 's' is not defined
>>> add(s)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    add(s)
NameError: name 's' is not defined
>>> def add(s):
	for value in s:
		s = s + value
		if s == []:
			return s

		
>>> s == [1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s == [1,2,3,4,5]
NameError: name 's' is not defined
>>> s=[1,2,3,4,5]
>>> add(s)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    add(s)
  File "<pyshell#15>", line 3, in add
    s = s + value
TypeError: can only concatenate list (not "int") to list
>>> def add(s):
	if s == []:
		sum = 0
		for value in s:
			sum = sum + value
			return sum

		
>>> s=[1,2,3,4,5]
>>> add(s)
>>> add(sum)
>>> s=[]
>>> add(s)
>>> sum([1,2,3,4,5])
15
>>> def add(s):
	s=0
	for value in s:
		s = s + value

		
>>> add(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    add(1,2,3,4,5)
TypeError: add() takes 1 positional argument but 5 were given
>>> def add(s):
	s=0
	for value in s:
		s = s + value
		return s

	
>>> add([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    add([1,2,3,4,5])
  File "<pyshell#43>", line 3, in add
    for value in s:
TypeError: 'int' object is not iterable
>>> def add(n):
	sum=0
	for value in n:
		sum = value + sum
		return sum

	
>>> add([1,2,3,4,5])
1
>>> n=[1,2,3,4,5]
>>> for value in n:
	print(value)

	
1
2
3
4
5
>>> n=[1,2,3,4,5]
>>> sum=0
>>> for value in n；
SyntaxError: invalid character in identifier
>>> n=[1,2,3,4,5]
>>> sum=0
>>> for value in n:
	sum = sum + value

	
>>> print(sum)
15
>>> def add(n):
	sum=0
	for value in n:
		sum = value + sum
		return sum

	
>>> add([1,2,3,4,5])
1
>>> add([1,2,3,4,5,6])
1
>>> def add(list):
	a=0
	for fruit in list:
		a=a+fruit
	return a

>>> add([1,2,3,4,5,6])
21
>>> def add(s):
    sum=0
    for value in s:
        sum = value + sum
        return sum

>>> add([1,2,3,4,5])
1
>>> def add(s):
    sum=0
    for value in s:
        sum = value + sum
    return sum

>>> add([1,2,3,4,5])
15
>>> def add(s):
	if s=[]
	
SyntaxError: invalid syntax
>>> def add(s):
	if s=[]:
		
SyntaxError: invalid syntax
>>> def add(s):
	if s = []:
		
SyntaxError: invalid syntax
>>> def add(s):
	if s == []:
		return(None,None)
	else:
		max = s[0]
		for i in s:
			if max > i:
				max = i
	return[max,index(max)]

>>> add([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    add([1,2,3,4,5])
  File "<pyshell#106>", line 9, in add
    return[max,index(max)]
NameError: name 'index' is not defined
>>> ef add(s):
	if s == []:
		return(None,None)
	else:
		max = s[0]
		for i in s:
			if i > max:
				max = i
				
SyntaxError: invalid syntax
>>> def add(s):
	if s == []:
		return(None,None)
	else:
		max = s[0]
		for i in s:
			if i > max:
				max = i
	return[max,index(max)]

>>> s=[1,2,3,4,5]
>>> add(s)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    add(s)
  File "<pyshell#111>", line 9, in add
    return[max,index(max)]
NameError: name 'index' is not defined
>>> def add(s):
	if s == []:
		return(None,None)
	else:
		max = s[0]
		for i in s:
			if i > max:
				max = i
	return[max,s.index(max)]

>>> s=[1,2,3,4,5]
>>> add(s)
[5, 4]
>>> def add(s):
	if s == []:
		return(None,None)
	else:
		max = s[0]
		for i in s:
			if i > max:
				max = i
	return max

>>> add([1,2,3,4,5])
5
>>> 
