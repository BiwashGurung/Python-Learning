
# print('Hello World')




# Assigning Values to Variables
counter = 100
miles = 100.10
name = "Jones"
print(counter)
print(miles)
print(name)


# String
str = 'Hello World !'
print(str)  #Yo la chai complete string use garxa
print(str[0])  #Yo la chai first character of string la print garxa
print(str[2:5]) # Yo la chai charecters starting from 3rd to 5th samma lai print garxa
print(str[2:]) # Prints string starting from 3rd character
print(str + "TEST") # Prints concatenated string 
print(str * 2)# esla chai 2 times print gardincha 


# List 
List = ['hi1','hello2', 202 ,'test3','bye4', 204.5]
tinylist = [123,'dexy']

print(List) #Prints complete list
print(List[0]) #Prints first element of the list
print(List[1:3])#Prints elements stariting from 3rd eleemnt
print(tinylist * 2) #2times print garxa
print(List + tinylist)



#tuple
tuple = ('apple',434, 2.4, ' john' , 3844.45)
tinytuple = (123, 'jega')

print(tuple) #prints complete tuples
print(tuple[4]) #4th index ko value lai print gaarxa
print(tuple[1:3]) # Prnts eleemnts starting from 2nd till 3rd
print(tuple[2:]) #Print eleemnt starrting from 3rd element
print(tinytuple * 2) #Prints tuple 2 times
print(tuple + tinytuple) #prints concatented tuple


# Dictionary
dict = {}
dict ['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name':'john' , 'code': 2344, 'dept': 'sales'}

print(dict['one']) #Prints value for 'one' key
print(dict[2]) #Prints value for 2nd key
print(tinydict) #Prints complete dictionary
print(tinydict.keys()) #Prints all the keys
print(tinydict.values())#Prints all the vlaues



# FizzBUZZ 
# https://builtin.com/software-engineering-perspectives/fizzbuzz-python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(i)


hexStr = bytes.fromhex('A2f7 4509')
print(hexStr)
byteString = b'\xa2\xf7E\t'
print(byteString.hex())

bArray1 = b"XYZ"
bArray2 = bArray1.replace(b"X", b"P")
print(bArray2)

byteArray1 = b'ABBACACBBACA'
print(byteArray1.count(b'AC'))

print(byteArray1.find(b'CA'))
bArr = b'Pokhara,Kathmandu,Lekhnath,Palpa'
partList = bArr.partition(b',')
print(partList)

myByteArray = bytearray('String', 'UTF-8')
memView = memoryview(myByteArray)

print(memView[2]) #ASCII of 'r'
print(bytes(memView[1:5]))       
