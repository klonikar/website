class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __str__(self):
        return 'MyClass'

    def __repr__(self):
        return 'MyClass {}'.format(self.var)

    def __eq__(self, other):
        return other.var == self.var

my_obj = MyClass(1)
print(my_obj.__hash__())
my_new_obj = MyClass(1)
print(my_new_obj.__hash__())

print(my_new_obj == my_obj)


var = {my_obj: 'my_obj'}
var[my_new_obj] = 'my_obj_2'
print(var)

print(my_obj == 1)