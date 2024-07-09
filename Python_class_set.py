class Intersection:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def result(self):
        resultant = set()
        for i in self.set1:
            if i in self.set2:
                resultant.add(i)
        print(f'Intersection: {resultant}')


class Union:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def result(self):
        for i in self.set2:
            self.set1.add(i)
        print(f'Union: {self.set1}')


my_set = set(input("Please enter a set (e.g 123456): "))
restart = 'yes'

while restart == 'yes':
    option = input("Please Select \n 1 for Union \n 2 for Intersection \n")

    if option == '1':
        second_set = set(input("Please enter second set (e.g 123456): "))
        set_union = Union(my_set, second_set)
        set_union.result()

    elif option == '2':
        second_set = set(input("Please enter second set (e.g 123456): "))
        set_intersection = Intersection(my_set, second_set)
        set_intersection.result()

    else:
        print("Invalid Input")

    inp = (input("Do You Want to Continue? (Yes/No) ")).lower()
    if inp != 'yes':
        restart = 'no'
