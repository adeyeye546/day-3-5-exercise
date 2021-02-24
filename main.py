# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedstring = name1 + name2

lowercasestr = combinedstring.lower()

t = lowercasestr.count("t")
r = lowercasestr.count("r")
u = lowercasestr.count("u")
e = lowercasestr.count("e")

true = t+r+u+e
l = lowercasestr.count("l")
o = lowercasestr.count("o")
v = lowercasestr.count("v")
e = lowercasestr.count("e")
love = l+o+v+e
totalsum = str(true) + str(love)
newtotal = int(totalsum)
print(totalsum)
if newtotal < 10 or newtotal > 90:
  print(f"Your score is {newtotal}, you go together like coke and mentos.")
elif newtotal >= 40 and newtotal <= 50:
  print(f"Your score is {newtotal}, you go together like coke and mentos.")
else:
  print(f"Your score is {newtotal}")

