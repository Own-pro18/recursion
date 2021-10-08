import re

def verify_num():
    code = input('Enter your Country code')
    while code == "+91":
        x = input("Enter your Mobile Number")
        num_valid = re.search('^[6-9]\d{9}$', x)
        if num_valid is not None:
            print('The given number is valid India Mobile Number')
            break
        else:
            print('The given number is Invalid ')

    else:
        print('Incorrect Country code')
        x = input("Try again???'y''n'??")
        if x == 'y':
            verify_num()


verify_num()
