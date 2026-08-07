from datetime import date, datetime
import json
from month_expense import view_expense_acc_to_month
from Date_validate import validate_date
from Item_validate import validate_item
from Money_validate import validate_money
from feedback_validate import validate_feedback

print("********************* WELCOME TO MY EXPENSE TRACKER *************************")

amount_balance = 100000

while True:

#==================================
        # welcome menu 
#==================================
   print(" ============== MENU ================")
   print("select any one option:")
   print("1.Add today's expense")
   print("2.View all expense")
   print("3. View total expense")
   print("4. View total expense according to month")
   print("5. Exit")

   user_input = int(input("Enter a choice: "))
   total = 0
  
#==================================
      # adding the expenses
#==================================
   if user_input == 1:

#==================================
 #making sure user enter valid date
#==================================

      date_time = validate_date()
      

#==================================
 #other things user need to enter
#==================================
      on_what_did_you_spend = validate_item()
      money_spent = validate_money()
      description = validate_feedback()

#===================================================
# converting that user entered data into dictionary
#===================================================
      data = {
         'Date':date_time,
         'Item':on_what_did_you_spend,
         'money_spent':money_spent,
         'description':description
      }

#=====================================================
# appending into the list we made at first using json
#=====================================================
      try:
         with open('demo.json','r') as f:
            Data = json.load(f)
      except (FileNotFoundError,json.JSONDecodeError):
         Data = []

      Data.append(data)

      with open('demo.json','w') as f:
         json.dump(Data,f,indent=4)

      print("********************** THANK YOU WE RECEIVER YOUR DATA *********************************")

#=====================================
# showing the expenses that user made
#=====================================
   elif user_input == 2:
   
      with open('demo.json','r') as f:
         content = json.load(f)
      print(content)

#==================================
# calculating the total expenses
#==================================
   elif user_input == 3:

      with open('demo.json','r') as f:
               content = json.load(f)

      for expense in content:
         total += expense['money_spent']
      amount_balance -= total
      print(f"This is the total money you spent: {total} and balance you have is: {amount_balance}")


#====================================
#viewing expense according to month
#====================================
   elif user_input == 4:
      view_expense_acc_to_month()
#==================================
         #exiting the loop
#==================================
   elif user_input == 5:
      break

#==================================   
#making sure user enter valid input
#==================================
   else:
      print("************ Enter a valid input.(Between 1 & 5) *****************")   
