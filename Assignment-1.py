#Q1. Create one variable containing following type of data:

#(i) string
var_str="string_datatype"

#(ii) list
var_list=["list","data","type"]

#(iii) float
var_flot=2.56

#(iv) tuple
var_tuple=('tuple_datatype',2.58)

#Q2. Given are some following variables containing data:
#(i) var1 = ‘ ‘
var1=''
print(type(var1))  #output will be string

#(ii) var2 = ‘[ DS , ML , Python]’
var2 ='[DS,ML,Python]'
print(type(var2))  #Output will be string

#(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
var3 =['DS','ML','Python']
print(type(var3))   #output will be list

#(iv) var4 = 1.
var4=1
print(type(var4))   #output will be int

#Q3. Explain the use of the following operators using an example:

#(i) /
#Explanation:- / opertaor is used to divide numbers
#for example:
a=4
b=2
print("The division of a & b is ",a/b) #output will be 2

#(ii) %
#Explantion:- % i.e Modulus is used to find the Remainder
x=6
y=3
print("the modulus of the x & y is ",x/y) #output will be 0

#(iii) //
#Explantion:- // i.e floor division is used to find the quotient value not in flot but in a intiger
#In other words it give the less or closest number to the Quotient.
#for example:- 
x1=24
y1=7
print("The floor division of the x1 & y1 is ",x1//y1) # The output will be 3

#(iv) ** 
#Explantion:- ** i.e Exponential is used to multiply the same number multiple time's.
#for example:- 
x2=2
print('The exponential of the x2 is ',x2**2) #the output will be 4

#Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
#element and its data type.
list1=["string",52,('cricket','football',69),["apple","mango"],52.45,["banana","pineapple"],2,True,['list','type']]
for elements in list1:
    print(elements,"-->",type(elements))


#Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
#times it can be divisible.
A=int(input("Enter number: "))
B=int(input("Enter number: "))
while A%B==0:
    print(int(A/B),"times it get Divisible")
    break
else:
    print("A/B is not purely Divisible")
    print(f"But the Answer of {A}/{B} is ",A/B)

#Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
#divisible by 3 or not.
list_25=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for elements in list_25:
    if elements%3==0:
       print(elements,"Element is Divisible by 3")
    else:
       print(elements,"Element is not Divisible by 3")


#Q7. What do you understand about mutable and immutable data types? Give examples for both showing
#this property.
#Answer: 
#(1) Mutable datatype --> Mutable datatype are those datatype which we can Modify after declaration 
# for example: I'm taking the example of list, as list is mutable datatype
fruit=["apple","banana","pineapple"]
print(fruit)
fruit.append("lichi") 
#After modification:
print(fruit)

#Immutable Datatype--> Immutable datatype are those datatype which we can not Modify after declaration 
# for example: we are taking the example of "Tuple", as tuple is a immuble datatype.
fruit=("apple","banana","pineapple")
#Before Modification it will print.
print(fruit)
fruit.append("lichi") 
#After modification it will not get executed, it will show error.
print(fruit)