#welcomes user
print("welcome to Leo's ChatBot project, I am Bot 1!")


#variable name gets the user's name
name = input("Please state your name: ")


#variable age prints out the user's name plus asks for age
age = int(input(f"I like that name! Now, {name} please enter your age: "))


def nameAndAge():
  
   #splits user's age into groups and prints out a compliment.
   #this also includes basic functionality such as "assistance"
   if 0<age and age<=10:
       print(f"Welcome {name}. Incredible, you are so young. How may I assist you?")
   elif 10<age and age<=18:
       print(f"Welcome {name}. I miss those years. How may I assist you?")
   elif 18<age and age<=30:
       print(f"Welcome {name}. Wow, you are all grown up! How may I assist you?")
   elif 30<age and age<=50:
       print(f"Welcome {name}. What a nice age! How may I assist you?")
   elif age>50:
       print(f"Welcome {name}. Wow, you must be so wise! How may I assist you?")


  
  


def mainMenu():


   #prints options of the menu to the user
   print("\n 1. Placeholder Option 1")
   print(" 2. Placeholder Option 2")
   print(" 3. Placeholder Option 3")
   print(" 4. Exit the conversation")

   #grabs what the user wants to do
   number = int(input("Please choose a number from the options above: "))
   if number == 1:
       placeholder1 = print("unfinished")
   elif number == 2:
       placeholder2 = print("unfinished")
   elif number == 3:
       placeholder3 = print("unfinished")
   elif number == 4:
       print(f"Goodbye {name}! Have an amazing day.")








nameAndAge()
mainMenu()


  











