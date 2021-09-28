# Recursive_Reverse String
def reverse(string: str):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


print(reverse(string='LosAngeles'))


# simple Reverse
#string = input(f'string::')
#rev = ''
# for i in string:
#rev = rev+i
# print(f'{rev}')


# stingManupulation_Method
# string='Angel'
# print(string[::-1])
