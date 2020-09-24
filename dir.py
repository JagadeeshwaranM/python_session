import pdb
class Supermarket:

    # Function __dir()___ which list all
    # the base attributes to be used.
    def __dir__(self):
        print('check')
        return ['customer_name', 'product',
                'quantity', 'price', 'date']

    # user-defined object of class supermarket

pdb.set_trace()
my_cart = Supermarket()

# listing out the dir() method
print(dir(my_cart))