# -*- coding: utf-8 -*-
'''
Description:    This is the template of a python program.
Author:         Du Ning
Date:           2022.01.16
'''

# Import the libs and modules
import    time
import    os

# Define the global constent values, use CAPITALIZED letters
MAX_NUMBER = 100
MIN_NUMBER = 0

# Define the global variable values, use lower letters
int_number = 0
float_number = 0.001
name_string= "peter"
color_list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
number_list = [1, 2, 3, 4, 5]
color_tuple = ('red', 'green', 'blue', 'yellow', 'white', 'black')
number_tuple = (1, 2, 3, 4, 5)
color_dict = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple', 'orange': 'orange'}
string_set = set('abracadabra')
color_set = set(('red', 'green', 'blue', 'yellow', 'white', 'black'))

def print_constent_variable_values():
    print ("***Printing the constent and variable values:***")
    print ("MAX_NUMBER is: ", MAX_NUMBER)
    print ("MIN_NUMBER is: ", MIN_NUMBER)
    print ("")
    print ("float_number is: ", float_number)
    print ("The type of float_number is: ", type(float_number))
    int_number = int(input ("Please input an integer number: "))
    print ("int_number is: ", int_number)
    print ("The type of int_number is: ", type(int_number))
    print ("")
    print ("name_string is: ", name_string)
    print ("The type of name_string is: ", type(name_string))
    print ("")
    print ("color_list is: ", color_list)
    print ("number_list is: ", number_list)
    print ("The type of number_list is: ", type(number_list))
    print ("")
    print ("color_tuple is: ", color_tuple)
    print ("number_tuple is: ", number_tuple)
    print ("The type of number_tuple is: ", type(number_tuple))
    print ("")
    print ("color_dict is: ", color_dict)
    print ("The type of color_dict is: ", type(color_dict))
    print ("")
    print ("string_set is: ", string_set)
    print ("color_set is: ", color_set)
    print ("The type of color_set is: ", type(color_set))
    print ("")
    print ("***The constent and variable values print done!***")

def fish():
    print ("***Solving the fish problem:***")
    print ("A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。")
    print ("日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。")
    print ("B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。")
    print ("C、D、E依次醒来，也按同样的方法拿鱼。")
    print ("问他们至少捕了多少条鱼?")
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print (f'There are {fish} fishes!')
            break
        fish += 1
    print ("***The fish problem solved!***")

def main():
    print_constent_variable_values()
    fish()

if __name__ == '__main__':
    main()