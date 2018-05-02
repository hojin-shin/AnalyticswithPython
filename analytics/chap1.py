#!/usr/bin/env python3

'''
Foundation for analytics with Python 
Lesson1))
'''
    
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21 : {0}".format(string1_list1))
print("Output #22 : FIRST PIECE : {0} SECOND PIECE : {1} THIRD PIECE :{2}"\
      .format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2= "Your, deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23 : {0}".format(string2_list))
print("Output #24 : {0} {1} {2}".format(string2_list[1], string2_list[5], string2_list[-1]))
      
print("Output #25 : {0}".format(','.join(string2_list)))
     
string3 = " Remove  unwanted characters    from this string.\t\t      \n"
print("output #26 : string3 : {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27 : lstrip : {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28 : rstrip : {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29 : strip : {0:s}".format(string3_strip))
      
