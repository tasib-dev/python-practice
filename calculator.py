one = input("type your first number : ")
two = input("now type the second : ")
a = int(one)
b = int(two)
calc = input("now tell me,what operation do you want??? <add for addition, mul for multiple, div for divide, min for minus> ")

if calc == "add" :
 print(a + b)
elif calc == "mul" :
 print(a * b)
elif calc == "div" :
 print(a / b)
elif calc == "min" : 
 print(a - b)
else :
  print("error")    