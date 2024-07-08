my_set = set(input("Please enter a set (e.g 123456): "))
restart = 'yes'
while restart == 'yes':
    option = input("Please Select \n 1 for Union \n 2 for Intersection \n")

    if option == '1':
        second_set = set(input("Please enter second set (e.g 123456): "))
        my_set = my_set.union(second_set)
        print(f'Union: {my_set}')

    elif option == '2':
        second_set = set(input("Please enter second set (e.g 123456): "))
        my_set = my_set.intersection(second_set)
        print(f'Intersection: {my_set}')

    else:
        print("Invalid Input")

    inp = (input("Do You Want to Continue? (Yes/No) ")).lower()
    if inp != 'yes':
        restart = 'no'

