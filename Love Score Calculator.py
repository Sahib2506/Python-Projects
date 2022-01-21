print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner's name? \n")

#Concatenating both and converting into lower case.
name_concatenation = (name1 + name2).lower()

#Counting how many time each alphabet appears for true
t = name_concatenation.count("t")
r = name_concatenation.count("r")
u = name_concatenation.count("u")
e = name_concatenation.count("e")

#Summing up the Score for True and converting it into string
true_score = str(t+r+u+e)

#Counting how many time each alphabet appears for love
l = name_concatenation.count("l")
o = name_concatenation.count("o")
v = name_concatenation.count("v")
e = name_concatenation.count("e")

#Summing up the Score for Love and converting it into string
love_score = str(l+o+v+e)

#Concatenating true and love score and converting it into interger.
True_Love_Score  = int(true_score + love_score)

#Giving Some Condtions for output.
if True_Love_Score <= 10 or True_Love_Score >= 90:
  print(f"Your score is {True_Love_Score}, you go together like coke and mentos.")

elif True_Love_Score >=40 and  True_Love_Score <= 50:
  print(f"Your score is {True_Love_Score}, you are alright together.")

else:
  print(f"Your score is {True_Love_Score}")

