# 🚨 TharinduRamanayake 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

truelove = str(true) + str(love)
int_truelove = int(truelove)

if (int_truelove < 10) or (int_truelove > 90):
    print (f"Your score is {truelove}, you go together like coke and mentos.")

elif (int_truelove >= 40) and (int_truelove <= 50):
    print (f"Your score is {truelove}, you are alright together.")

else:
    print (f"Your score is {truelove}.")
