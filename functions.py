# #--------------------List comprehension, Iterators & Generators
# #--------------------List comprehension
# x=[6, 3, 1]
# y = [i **2 for i in x]
# print(y)
#
# #----------------------same logic with for loop
# x=[6,3,1]
# z=[]
# for i in x:
#     y= i ** 2
#     z.append(y)
# print(z)
#
#
# x=[1,2,3]
# y=[i*i for i in x]
# print(y)
#
# x=[1,2,3]
# y=[]
# for i in x:
#     z=i*i
#     y.append(z)
# print(y)

#-----------------------------Iterator

# x=[1,2,3]
# iter1=iter(x)
# print(type(iter1))
# for i in iter1:
#     print(i)
#
# x=[1,2,3]
# iter1=iter(x)
# print(next(iter1))

# x=[1,2,3]
# iter1=iter(x)
# while True:
#     try:
#         print(next(iter1))
#     except StopIteration:
#         break

#------------------------------Generators

# def sum(a,b):
#     return a+b

def generator_123():
    yield  1
    yield  2
    yield  3
gen1=generator_123()
print(type(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

for i in gen1:
    print(i)