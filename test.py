# Don't you want me like I want you, baby?
# Don't you need me like I need you now?
# Sleep tomorrow, but tonight, go crazy
# All you gotta do is just meet me at the

# inputText = input("Hi, do you know the lyrics of APT? ")
# print(f"\n\n {inputText} \n\nAPT APT APT APT APT APT APT APT APT APT APT APT!")
# print("APT APT APT APT APT APT APT APT APT APT APT APT!")
# print("APT APT APT APT APT APT APT APT APT APT APT APT!")

# x = float(input("x: "))
# y = float(input("y: "))
# print(f"x + y = {x / y:.2f}")

import random
import time

x = random.randint(1, 10)
num = int(input("input num: "))

if num == x:
  print("you are korek!")
elif num > x:
  print("number too high")
elif num < x:
  print("number too low")

time.sleep(1)
print("random int: ", x)

