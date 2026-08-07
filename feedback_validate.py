
#=======================
#description validation
#=======================


def validate_feedback():

   while True:
       description = input("feedback on what you spent: ")

       if description:
         return description
       elif isinstance(description,int):
          print("type a description bro not money!!")
       else:
          print("type something bro")