#While / While Else loops - a while loop executes as long as an user-specified condition is evaluated as True; the "else" clause is optional
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("Out of the while loop. x is now greater than 10")
#result of the above "while" block
#1 2 3 4 5 6 7 8 9 10
#Out of the while loop. x is now greater than 10



#If / For / While Nesting
x = "Cisco"
if "i" in x:
    if len(x) > 3: #if nesting
        print(x, len(x))
 #Cisco 5 #result of the above block

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2: #for nesting
        print(i*j)
#10 20 30 20 40 60 30 60 90 #result of the above block

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:  #while nesting
        print(z)
        z += 1
#5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10	#result of the above block

for number in range(10):
    if 5 <= number <= 9: #mixed nesting
        print(number)
#5 6 7 8 9 #result of the above block
