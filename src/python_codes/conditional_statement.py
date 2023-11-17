name = "Tony Star"
#Find function :-we can find single character or sub string of index position

print (name.find("Tony"))

#Replace function:- we can replace one single character or sub string
print (name.replace("Tony","kanhaiya"))
#Now our name of variable is gave priviouse values
print (name)
#in Function:-it is use for find out in a variable any particular  character or sub string are present ot not
name="Tiger"


print ('T' in name)
#_______________Operator_,ARITHEMATIC OPERATOR_:- + ,-,*,/,//_____________________
print (4+6)
#___Comparsion-Operator:-___<,>,<=,>=,==,!=
print (5>=9)
#~~~~~~~~~~~~~~Lgical-Operator:- or(|),and (&)
print ("last line")
print (5>2 & 5>9)
print (4 >1 and 4<8)
print (3<8 | 8>3)
#not operator:-Not (!)
print (6!=9)
print (not 8 == 8)

#~~~~~~~~~~~~~~if,else statement~~~~~~~~~~~~~~~
age=10
if age >18 :
    print ("you are eligible for vote")
else:
    print ("Not eligible for vote")

#**************elif-condition*************
age =4
if age >18 :
    print ("You are eligible for Voting")
elif age <18 and age>5:
    print ("You are in School")
else:
    print ("You are a Child")
