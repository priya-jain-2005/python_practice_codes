from random import randint

tables = {2: {"allotted": 0},
          3: {"allotted": 0},
          4: {"allotted": 0},
          5: {"allotted": 0},
          6: {"allotted": 0}}
# print(table[2]["allotted"])


class CustomerGroup:
    def __init__(self):
        self.size = 2,
        self.wait_time = 0,
        self.allotted = 0,
        self.left = 0
        self.eat_time = 0

    def __repr__(self):
        return f"CustomerGroup('{self.size}','{self.allotted}','{self.eat_time}')"


arrive = {}
leave = {}
count = 1
tables_allotted = {}
Customer_group_not_allotted = []
while True:
    Customer_group_size = int(input("Enter customer group size, enter 0 if there are no more customers :: "))
    if not Customer_group_size:
        break
    if Customer_group_size == 1 or Customer_group_size > 6:
        print("enter a group size between 2 and 6")
        continue
    obj = CustomerGroup()
    obj.size = Customer_group_size
    # arrive["G"+str(count)] = Customer_group_size
    # print(arrive)
    count += 1
    '''
    for key in sorted(tables):
        if key >= Customer_group_size and tables[key]["allotted"] == 0:
            tables[key]["allotted"] = Customer_group_size
            tables_allotted[key] = tables[key]["allotted"]
            obj.allotted = key
            obj.eat_time = randint(20, 100)
            print("Table " + str(key) + " is allotted to this group!!")
            print(obj)
            break
        if tables.keys() == tables_allotted.keys():
            if tables[key]["allotted"]:
                vacant_seats = key - tables[key]["allotted"]
                if vacant_seats >= Customer_group_size:
                    tables[key]["allotted"] += Customer_group_size
                    obj.allotted = key
                    obj.eat_time = randint(20, 100)
                    print("Table " + str(key) + " is allotted to this group!!")
                    print(obj)
                    
    '''
    if not obj.allotted:
        Customer_group_not_allotted.append(obj)
    print(Customer_group_not_allotted)















