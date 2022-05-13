#strings

#user input and saving user input into a variable
input("Enter what you want to be printed out: ")
usr_input= input("This program will save your input. Enter what you want to be printed out: ")

#int,float,string,bool
varOne=112415461#int
varTwo=2.6435653#float
varThree="Hello"#string
var__False=False#boolean

switch_C="Cisco"
switch_A="Arista"
switch_J="Juniper"
switch_N="$$$Nokia"
switch_H="Huawei"
switch_E="Ecrisson"
switch_M="   Motorola     "
switches="Cisco Arista Juniper Nokia Huawei Ecrisson Motorola"
year="1999"
#indexing notes
a="thaumaturgical"
a.index("u")# 3, the first one is indexed
a.index("i")# 10
a.startswith("T")# False
a.startswith("t")# True
switch_M.strip()# removes whitespaces
switch_N.strip("$")# removes $, removes a certain character
switches.replace(" ","") # removes the spaces, CiscoAristaJuniperNokiaHuaweiEcrissonMotorola
switches.replace(" ",", ")# Cisco, Arista, Juniper, Nokia, Huawei, Ecrisson, Motorola
"_".join(switches)# C_i_s_c_o_ _A_r_i_s_t_a_ _J_u_n_i_p_e_r_ _N_o_k_i_a_ _H_u_a_w_e_i_ _E_c_r_i_s_s_o_n_ _M_o_t_o_r_o_l_a
a.capitalize()#Capitalizes first letter of string.
a.lstrip()#Removes all leading whitespace in string.
a.rstrip()#Removes all trailing whitespace of string.
a.swapcase()#Inverts case for all letters in string.
a.title()#Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
a.isalnum()#Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
a.isalpha()#Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
a.isdigit()#Returns true if string contains only digits and false otherwise.
a.islower()#Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
a.isnumeric()#Returns true if a unicode string contains only numeric characters and false otherwise.
a.isspace()#Returns true if string contains only whitespace characters and false otherwise.
a.istitle()#Returns true if string is properly "titlecased" and false otherwise.
a.isupper()#Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
"g" in a# True
"g" not in a# False
"x" in a# False
"x" not in a# True
switch_N+year# concatenating two strings, $$$Nokia1999
switch*3# mutiplying a string, $$$Nokia$$$Nokia$$$Nokia

#string formatting
# %s string
# %x convert and int into a string

"Juniper model: %s, %d RU, IOS %f" %("EX4400", 1, 20.3)
"On the farm we have {},{},{},{}".format("goats","horses","alpaca","the cute cat felix")
"On the farm we have {3},{0},{1}, and {2}".format("goats","horses","alpacas","the cute cat felix")

string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[5:15] #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice### 10.110.8.9
string1[5:] #slice starting at index 5 up to the end of the string, 10.110.8.9 [160/5] via 10.119.254.6### 0:01:00, Ethernet2
string1[:10] #slice starting at the beginning of the string up to, but NOT including, index 10### O E2 10.11
string1[:] #returns the entire string###O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2
string1[-1] #returns the last character in the string### 2
string1[-2] #returns the second to last character in the string### t
string1[-9:-1] #extracts a certain substring using negative indexes### Ethernet
string1[-5:] #returns the last 5 characters in the string### rnet2
string1[:-5] #returns the string minus its last 5 characters### O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethe
string1[::2] #adds a third element called step; skips every second character of the string### OE 01089[6/]va1.1.5.,00:0 tent
string1[::-1] #returns string1's elements in reverse order### 2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O
