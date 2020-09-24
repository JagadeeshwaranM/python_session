#mutable - Byte array, List, Set, Dictionary
#Immutable - String, Tuple

# print(type(4))
# print(type(4.0))
# print(type(-4))
# print(type(1j))
# print(float(5))
# print(float(44.555555555))
# print(float('44'))
# print(7.6+8.7)
# print(round(7.6+8.7))
# print(round(7.6+8.7,1))
# print(round(1.1+1.1+1.1,1) == 3.3)
#--------------------------------
# a=7.0
# b=11.0
# c=7
# d=11

# print(a + b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(c/d)
# # power
# print(c**2)
# #reminder
# print(d%c)
#-------------------------------------
# a=3
# b=5
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(type(True))
# print(bool(28))
# print(bool(-2.7))
# print(bool(0))
# print(bool('Jagadeesh'))
# print(bool(" "))
# print(bool("."))
# print(bool(""))
# print(str(False))
# print(int(True))
# print(5 + True)
# print(5 * True)
# print(5 * False)
#-------------------------------------------- Sequence Type - String
# welcome = "Hello World"
# print(welcome)
# print(welcome[0])
# print(welcome[-11])
# print(welcome[-1])
#-------------------------------------------- Bytes Type
# s='abcd'
# print(len(s))
# print(s[0])
# b=b'abc'
# print(type(b))
# print(len(b))
# print(b[0])
# a=b'abc'
# b='abc'
# d=bytes(b,encoding='utf-8')
# print(a)
# print(d)
#-------------------------------------------- Bytes Type
#mutable - you can change it
#immutable - you can't change it -  String, bytes
# s='abcd'
# print(s[0])
# s[0]='1'
# # Gives error as we can't change s[0] as it is immutable type

# x=b'abcd'
# print(x[0])
# print(x[1])
# x[0]='1'

#------------------------------------------- String

# s='abcd'
# s += 'efgh'
# print(s)
# print(s)
#
# s='abcd'
# s='efgh'
# print(s)
# a='123'
# print(a[0])
# print(a)
# a='453'
# print(a[0])
# print(a)
#------------------------------------------- Byte Array
# a=bytearray('abcd','utf-8')
# print(a)
#--------------------------------
# a=bytearray('abcd','utf-8')
# print(a[0])
# a[0]=65
# print(a[0])
# print(a[-1])
# print(a[1:4])
# print(a.startswith(b'a'))
###############--------------------------LIST Datatype MUTABLE
# a=[12,'demo',12.2]
# print(a)
# print(a[0])
# a[0]=24
# print(a)
# a.append('jagadeesh')
# print(a)
# a[0]='twelve'
# print(a)
# del a[0]
# print(a)
# print(a[0:2])
# print(a[0:])
# a=[]
# a.append(12)
# print(a)

###############--------------------------TUPLE Datatype IMMUTABLE
# a=(12,23)
# print(a)
# b=(12,23,'Jaga')
# print(b)
# print(b[0])
#b[0]=11  -----------------------------gives error
# print(b)
# len(b)
# print(b[0:2])

#---------------------------- Slicing in List and String
# my_list = [0,1,2,3,4,5,6,7,8,9]
# print(my_list[0])
# print(my_list[5])
# print(my_list[-1])
# print(my_list[-10])
# print(my_list[0:6])
# print(my_list[3:8])
# print(my_list[-7:-2])
# print(my_list[1:9])
# print(my_list[1:])
# print(my_list[:-1])
# print(my_list[:])
#
# print((my_list[2:-1:2])) -------------------- using step func
# print(my_list[-1:2:-1])
# print(my_list[-2:1:-2])
# print(my_list[::-2])
# print(my_list[::-1])


# sample_url = "http://coreyms.com"
# print(sample_url)
# print(sample_url[::-1])
# print(sample_url[-4:])
# print(sample_url[-3:])
# print(sample_url[7:])
# print(sample_url[7:-4])


#--------------------------------Collection and Mappings types in Python
# Range Type and function, set type and dictionary
# a=list(range(6))
# print(a)
# b=list(range(2,6))
# print(b)
# c=tuple(range(6))
# print(c)
# d=tuple(range(2,6))
# print(d)
# e=list(range(0,11,2))
# print(e)
############ give empty list
# e=list(range(11,2))
# print(e)
# e=list(range(-2,-11,2))
# print(e)
###########corrected
# e=list(range(11,20))
# print(e)
# e=list(range(-2,-11,-2))
# print(e)

##################set elements  Order does not matter and data needs to be unique
# a={1,'s',7.8}
# print(a)
# b=set([1,'B',6.9,1])
# print(b)
# b.add(5)
# print(b)
# c=set()
# print(c)
# print(dir(c))
# My_set = {1,'s',7.8}
# print(len(My_set))
# for a in My_set:
#     print(a)
# c={1,2,3,4}
# print(c)
# d=set([1,2,3,4])
# print(d)
# e=set()
# e.add(5)
# for a in e:
#     print(a)
# e.update([6,3])
# print(e)
# e.remove(5)
# print(e)
# # for a in e:
# #     print(a)
# e.discard(6)
# print(e)
# e.discard(10)
# print(e)
# e.pop()
# print(e)

# a={1,2,3,4}
# b={1,5,4,6}
# c={9,10}
# print(a|b)
# print(a.union(b,c))
# a={1,2,3,4}
# b={1,5,4,6}
# print(a&b)
# print(a.intersection(b))
# a={1,2,3,4}
# b={1,2,7,8}
# print(a-b)
# print(a.difference(b))

#############-------------------- Frozen set A frozen set is a set whose values cannot be modified
# a={1,2,3}
# print(type(a))
# b=frozenset(a)
# print(type(b))
# print(b)
#############-------------------- Dictionary Type
# a={'john':150,'mac':200}
# print(a['john'])
# a['john']=900
# print(a)
# del a['mac']
# print(a)
# print(a.keys())
#####################
# a=[]
# print(type(a))
# print(a)
# b=set()
# print(type(b))
# print(b)
# c=set([])
# print(type(c))
# print(c)
# d=tuple()
# print(type(d))
# print(d)
# e={}
# print(type(e))
# print(e)
# f=()
# print(type(f))
# print(f)
a=[]
b={}
c=()
d=set()
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# a.append([3,6,7,8])
# print(a)

# b={'key1':'geeks', 'key2':'for'}
# b.update({'key3':'geeks'})
# print(b)
# b['key3']='jack'
# print(b)


# d.add('a')
# print(d)
# d.update(('b','c','d'))
# print(d)
# d.add('a')
# d.add('b')
# d.update('c')
# d.add('d')
# print(d)
