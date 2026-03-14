print("Welcome to our restaurant, this is our menu:")
print("------------------")
print("|1. Cheeseburger |")
print("|2. Pizza        |")
print("|3. Fish         |")
print("|4. Steak        |")
print("------------------")


bill=0
price=input("Would you like to see the prices? [y/n]: ")


if price.lower()=="y":
    print("Cheeseburger: 12.99$")
    print("Pizza: 9.99$")
    print("Fish: 11.99$")
    print("Steak: 14.99$")
print("What would you like to order")
choice=int(input("Enter a number: "))


if choice==1:
   bill+=12.99
elif choice==2:
    bill+=9.99
elif choice==3:
    bill+=11.99
elif choice==4:
    bill+=14.99


amount=int(input("How many would you like? "))
bill=bill*amount
choice_drink=input("Would you like a drink? [y/n]?")


if choice_drink.lower()=="y":
    print("------------------")
    print("|1.Ayryan: 1.99$ |")
    print("|2.Beer:   2.99$ |")
    print("|3.Water:  0.99$ |")
    print("------------------")
    drink=int(input("Pick a number: "))


    if drink==1:
        bill+=1.99
    elif drink==2:
        bill+=2.99
    elif drink==3:
        bill+=0.99


elif choice_drink.lower()=="n":
    more=input("would you like to order anything else? [y/n]: ")
    if more.lower()=='y':
      print("------------------")
      print("|1. Cheeseburger |")
      print("|2. Pizza        |")
      print("|3. Fish         |")
      print("|4. Steak        |")
      print("------------------")
      more_food=int(input("Pick a number: "))


      if more_food==choice:
          print("Cant pick food you already got earlier")
      elif (more_food!=choice) and (more_food==1):
          bill+=12.99
      elif(more_food!=choice) and (more_food==2):
          bill+=9.99
      elif(more_food!=choice) and (more_food==3):
          bill+=11.99
      elif(more_food!=choice) and (more_food==4):
          bill+=14.99
    elif more.lower()=='n':
        print("Okay thank you!")
drinks_amount=int(input("How many drinks would you like: "))
if drink==1:
        bill+=1.99*drinks_amount
elif drink==2:
        bill+=2.99*drinks_amount
elif drink==3:
        bill+=0.99*drinks_amount

        
bill= round(bill, 2)
print("Time to pay")
print(f"Your bill is: {bill}$")
