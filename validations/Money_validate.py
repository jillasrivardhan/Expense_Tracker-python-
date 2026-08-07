
#===================
#money validation
#===================

def validate_money():

   while True:
      try:

         money_spent = float(input("enter amount spent:$ "))

         if money_spent < 0:

            print("can't be less than zero.pease try again")

         elif isinstance(money_spent,str):

            print("it should be interger or float value")

         else:

            return money_spent

      except ValueError:

         print("enter valid amount bro")
        
