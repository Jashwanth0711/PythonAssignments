import random
user_num=int(input("Enter the number between 0 and 2 where rock=0,paper=1 and scissor=2:"))
computer_num=random.randint(0,2)
if(user_num>=3 or user_num<0):
    print("You have entered invalid number please enter correct number.")
else:
    print("computer_num:")
    print(computer_num)
    if(user_num==computer_num):
        print("Game is draw.")
    elif(computer_num==0 and user_num==2):
        print("computer won the game.")
    elif(computer_num==2 and user_num==0):
        print("user won the game.")
    elif(computer_num>user_num):
        print("computer won the game.")
    elif(computer_num<user_num):
        print("user won the game.")
