import random
user_choice=int(input("enter your choice:type0 is rock,type1 is paper,type2 is scissor"))
list=["rock","paper","scissor"]
computer_choice=random.randint(0,2)
if user_choice>=3 or user_choice<0:
	print(f"invalid number")
else:
	print(f"you choice is {list[user_choice]}")
	print(f"computer choice is  {list[computer_choice]}")
	if computer_choice==user_choice:
		print("it is draw")
	elif computer_choice==0 and user_choice==2:
		print("you lose")
	elif computer_choice==2 and user_choice==0:
		print("you win")
	elif computer_choice >user_choice:
		print("you lose")
	elif computer_choice <user_choice:
		print("you win")
