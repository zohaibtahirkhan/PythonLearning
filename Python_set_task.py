my_set = set(input("Please enter a set (e.g 123456): "))
restart = 'yes'


def my_intersection(set_1, set_2):
    resultant = set()
    for i in set_1:
        if i in set_2:
            resultant.add(i)
    return resultant


def my_union(set_1, set_2):
    for i in set_2:
        set_1.add(i)
    return set_1


while restart == 'yes':
    option = input("Please Select \n 1 for Union \n 2 for Intersection \n")

    if option == '1':
        second_set = set(input("Please enter second set (e.g 123456): "))
        my_set = my_union(my_set, second_set)
        print(f'Union: {my_set}')

    elif option == '2':
        second_set = set(input("Please enter second set (e.g 123456): "))
        my_set = my_intersection(my_set, second_set)
        print(f'Intersection: {my_set}')

    else:
        print("Invalid Input")

    inp = (input("Do You Want to Continue? (Yes/No) ")).lower()
    if inp != 'yes':
        restart = 'no'

