#Iterators - an object which allows a programmer to traverse through all the elements of a collection
my_list = [1, 2, 3, 4, 5, 6, 7]

my_iter = iter(my_list) #iter() returns an interator object

next(my_iter) #in Python 2 and 3, it returns the elements of a sequence one by one; raises StopIteration when the sequence is exhausted
