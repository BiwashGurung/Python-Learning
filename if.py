# IF CONDITION

var1 = 100
if var1:
    print ("1 - Got a true expression value")
    print(var1)


var2 = 0
if var2>10:
    print("2 - Got a true expression value")  
    print(var2)  
print("Good Bye")


# IF...ELIF...ELSE
var = 100
if var == 200:
    print("Its 200")
elif var == 150:
    print("Its 150")
elif var == 100:
    print("Its 100")
else:
    print("Its none of above")
print("Good Bye!")                

#While Loop example
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("Good Bye!")    



#range()
for var in list(range(5)):
    print(var)

# List Iteration
fruits = ['banana','apple','mango']
for fruit in fruits:
    print('Current fruit:', fruit)

# Iterating by Sequence Index
fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print('Current fruit:',fruits[index])

#Break Statement
count = 0
while count < 10:
    count += 1
    if count == 5:  
        break
    print("inside loop", count)
print("out of while loop")     


#Coninue Statement
ctr = 0
for ctr in range(10):
    ctr = ctr + 1
    if  ctr == 5:
        print("5 is skipped")
        continue
        print("This won't be printed too.")
    print('Number is' + str(ctr))
print('Out of loop') 


#pass Statement
for letter in 'Python':
    if letter == 'h':
        pass
    else:
        print ('Current Letter:', letter)
print ("Good BYE" )       

