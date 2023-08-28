# Question 1

def hello_name(user_name):
    """Display username"""
    print("Hello " + user_name.title() + "!")

hello_name('Daniel')


# Question 2

def odd_numbers():
    """Display odd numbers between 1 and 100"""
    for i in range(1,101,2):
        print(i)

odd_numbers()


# Question 3

def max_num_list(a_list):
    """Display max number in the list"""
    max_num = max(a_list)
    return max_num

test = max_num_list([1, 3, 4, 5, 7, 8, 9])
print(max_num_list([1, 3, 4, 5, 7, 8, 9]))


# Question 4

def leap_year(a_year):
    """Display if a year is leap year"""
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')

leap_year(2000)


# Question 5

def is_consecutive(a_list):
    """Display if all numbers are consecutive"""
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)

is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9])