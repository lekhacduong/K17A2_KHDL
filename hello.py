Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> can_bac_2=math.sqrt(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    can_bac_2=math.sqrt(x)
NameError: name 'x' is not defined
>>> x=10
>>> can_bac_hai=math.sqrt
>>> can_bac_hai=math.sqrt(x)
>>> print("can bac hai cua",x,'=',can_bac_hai)
can bac hai cua 10 = 3.1622776601683795
>>> x=100
>>> print("can bac hai cua",x,'=',can_bac_hai)
can bac hai cua 100 = 3.1622776601683795
>>> x=int(input())
can_bac_hai=math.sqrt(x)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x=int(input())
ValueError: invalid literal for int() with base 10: 'can_bac_hai=math.sqrt(x)'
>>> x=4
>>> can_bac_hai=math.sqrt(x)
>>> print("can bac hai cua",x,'=',can_bac_hai)
can bac hai cua 4 = 2.0
print('hello')
