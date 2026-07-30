import json
from datetime import datetime

def view_expense_acc_to_month():
   user_input = input("enter date: ")
   datetime.strptime(user_input,'%m-%Y')
   amount = 0

   with open("demo.json",'r') as f:
     data = json.load(f)

   for expense in data:
      x = datetime.fromisoformat(expense['Date'])

      if user_input == x.strftime('%m-%Y'):
         amount += expense['money_spent']
   print(f"total amount of this month {amount}")