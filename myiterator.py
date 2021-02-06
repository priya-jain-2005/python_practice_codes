class Employee:
    ''' demonstrating Iterator by creating an iterable class Employee '''
    def __init__(self):
        self.emp_no = 0
        self.emp_sal = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.emp_no<5:
            self.emp_no +=1
            self.emp_sal += 5000
            return [self.emp_no,self.emp_sal]
        else:
            raise StopIteration


emp = Employee()
emp_iter = iter(emp)
print(next(emp_iter))
print(next(emp_iter))
print("IN LOOP")
for i in emp_iter:
    print(i)

'''when we use for loop to traverse through the iterable objects then internally it calls __iter__ 
and __next__ for that object'''
'''To prevent the iteration to go on forever, we can use the StopIteration statement.'''
'''
OUTPUT:
[1, 5000]
[2, 10000]
IN LOOP
[3, 15000]
[4, 20000]
[5, 25000]
'''