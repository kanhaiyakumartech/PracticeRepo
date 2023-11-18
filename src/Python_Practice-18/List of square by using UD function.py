#First of all i declered a Function

def get_square(number):
    return number * number

#Here we are using for loop and pass the list of elements

for i in [4,9,8,5]:
#Now we are calling a function
    Square_of_list  = get_square(i)
    print('Square of',i, '=',Square_of_list)

