while True:
  age=int(input("Enter your age: "))
  age=int(age)
  if age<3:
    print("Ticket is free")
  elif age<13:
    print("the ticket is $10")
  else:
    print("the ticket is $15")