from datetime import datetime

# load the data into a list

Data = []

print(" WELCOME TO MY EXPENSE TRACKER ")

while True:

   # welcome menu 

   print(" ====== MENU =======")
   print("select any one option:")
   print("1.Add today's expense")
   print("2.View all expense")
   print("3. View total expense")
   print("4. Exit")

   user_input = int(input("Enter a choice: "))
   total = 0

   # adding the expenses

   if user_input == 1:

      #making sure user enter valid date

      while True:
         date = input("Enter date (DD-MM-YYYY): ")

         try:
          date = datetime.strptime(date, "%d-%m-%Y")
          break
         except ValueError:
          print("Invalid date. Please try again.")

      #other things user need to enter

      on_what_did_you_spend = input("on what did you spend: ").split(",")
      money_spent = float(input("enter amount spent:$ "))
      description = input("feedback on what you spent: ")

      # converting that user entered data into dictionary

      data = {
         'Date':date,
         'Item':on_what_did_you_spend,
         'money_spent':money_spent,
         'description':description
      }
      # appending into the list we made at first 

      Data.append(data)
      print("thank you we received to data")

   # showing the expenses that user made

   elif user_input == 2:
      for i in Data:
         print(i)

   # calculating the total expenses

   elif user_input == 3:
      for expense in Data:
         total += expense['money_spent']
      print(f"This is the total money you spent {total}")

   #exiting the loop

   elif user_input == 4:
      break
   
   #making sure user enter valid input

   else:
      print("enter a valid input.(Between 1 & 4)")   
