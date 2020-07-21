# First = input("Hello What is your First Name? ")
# Last = input("Hello what is your Last Name? ")
# Answer= input("Hello" + First + Last)

counter = 0
for i in range(3) :
  counter += 1 
  print(counter)

for x in range(20):
  if x > 10:
    print("greater than", x)
  elif x == 10:
    print("x is 10", x)
  else:
    print("less than 10", x)
  