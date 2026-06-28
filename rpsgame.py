import random
Rock='r'
scissors='s'
paper='p'
values={Rock:'🪨',paper:'📃',scissors:'✂️'}
choices=(tuple(values.keys()))
def  get_user_choice():
   while True:
      user_choice=input("Enter your choice (r/p/s) :").lower()
      if user_choice  in choices:
       return user_choice
      else:
        print('Invalid Choice')

def determinent(user_choice,computer_choice):
   print(f'you choose{values[user_choice]}')
   print(f'computer choose {values[computer_choice]}')

def winner(user_choice,computer_choice):
   if user_choice==computer_choice:
     print("it's tie")
   elif ((user_choice==paper and computer_choice == Rock) or
      (user_choice==scissors and computer_choice==paper) or
       (user_choice==Rock and computer_choice==scissors)):
       print("you won")
   else:
      print("you loss")
      
def player():
      while True:
           user_choice=get_user_choice()

           computer_choice=random.choice(choices)
           determinent(user_choice,computer_choice)
           winner(user_choice,computer_choice)
  
           should_continue=input("want to continue (y/n) :")
           if(should_continue=='n'):
            break
           
player()