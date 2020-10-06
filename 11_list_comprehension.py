#list comprehension
import pdb
pdb.set_trace()
#--------------------List comprehension
# Using for loop
my_list = []
for x in range(10):
    my_list.append(x * 2)
print(my_list)

#same using list comprehension
comp_list = [x * 2 for x in range(10)]
print(comp_list)

#Another best example
comp_list = [x ** 2 for x in range(7) if x % 2 == 0]
print(comp_list)


nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]
nums_letters2 = [[n,n*2] for n in nums]
print(nums_letters)
print(nums_letters2)

iter_string = "some text"
comp_list = [x for x in iter_string if x !=" "]
print(comp_list)

