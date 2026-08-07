
#===================
#item validation
#===================

def validate_item():
  while True:
  
    on_what_did_you_spend = str(input("What did you spend on: ")).strip()

    if on_what_did_you_spend:
        return on_what_did_you_spend

    else:
        print("Please enter an item.")
