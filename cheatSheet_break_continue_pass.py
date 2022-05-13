#Break, Continue, Pass
list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break #stops the execution here, ignores the print statement below and completely quits THIS "for" loop; however, it doesn't quit the outer "for" loop, too!
        print(i * j)
    print("Outside the nested loop")

#result of the above block
#40
#Outside the nested loop
#50
#Outside the nested loop
#60
#Outside the nested loop

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            continue #ignores the rest of the code below for the current iteration, then goes up to the top of the loop (inner "for") and starts the next iteration
        print(i * j)
    print("Outside the nested loop")

#result of the above block
#40
#120
#Outside the nested loop
#50
#150
#Outside the nested loop
#60
#180
#Outside the nested loop

for i in range(10):
    pass #pass is the equivalent of "do nothing"; it is actually a placeholder for when you just want to write a piece of code that you will treat later



#Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines of code in the program
try:
    print(4/0) #in the "try" clause you insert the code that you think might generate an exception at some point
except ZeroDivisionError:
    print("Division Error!") #specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!") #executed if the code inside the "try" block raises NO exceptions
finally:
    print("I don't care if an exception was raised or not!") #executed whether the code inside the "try" block raises an exception or not

#result of the above block
#Division Error!
#I don't care if an exception was raised or not!
