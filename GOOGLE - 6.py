# GOOGLE CODE - 6 for inputing an list of integers from the user, pick a number multiply it to all other numbers
# other than itself and print the list doing it for all the user entered integers in a list
# u tube link  =  https://youtu.be/khTiTSZ5QZY
size_of_user_entered_list = int(input("enter size  "))
user_entered_list = [int(input("enter integer value  ")) for i in range(0, size_of_user_entered_list)]
product_list = []
for selection_from_user_entered_list in range(0, size_of_user_entered_list):
    product = 1
    for random_num_selected in range(0, size_of_user_entered_list):
        if ( selection_from_user_entered_list == random_num_selected ):
            continue
        else:
            product = product * user_entered_list[ random_num_selected ]
    product_list.append( product )
print( product_list )

