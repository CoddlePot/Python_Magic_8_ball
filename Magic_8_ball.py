import random
import time

filename = "8ball.txt"

try:
    with open(filename, "r") as f:
        data = f.read()
except FileNotFoundError:
    data = ""

if data:
    predictions = data.split("\n")  # splits based on line
else:
    predictions = []

list_range = len(predictions)
print(predictions)
print(list_range)

answer = random.randint(1, list_range)
print("THE MAGIC 8-BALL\n")
print("_____________(8)_____________\n")

while True:
    print("Ask a question!")
    input("Press Enter to shake the ball!\n_____________________________")
    time.sleep(.25)
    print("\n*SHAKE*\n")
    time.sleep(.25)
    print("*SHAKE*\n")
    time.sleep(.25)
    print("*SHAKE*\n")
    time.sleep(.5)
    if answer == 1:
        print(predictions[0], "\n")
        print(answer)
    elif answer == 2:
        print(predictions[1], "\n")
        print(answer)
    elif answer == 3:
        print(predictions[2], "\n")
        print(answer)
    elif answer == 4:
        print(predictions[3], "\n")
        print(answer)
    elif answer == 5:
        print(predictions[4], "\n")
        print(answer)
    elif answer == 6:
        print(predictions[5], "\n")
        print(answer)
    elif answer == 7:
        print(predictions[6], "\n")
        print(answer)
    elif answer == 8:
        print(predictions[7], "\n")
        print(answer)
    elif answer == 9:
        print(predictions[8], "\n")
        print(answer)
    elif answer == 10:
        print(predictions[9], "\n")
        print(answer)
    elif answer == 11:
        print(predictions[10], "\n")
        print(answer)
    elif answer == 12:
        print(predictions[11], "\n")
        print(answer)
    elif answer == 13:
        print(predictions[12], "\n")
        print(answer)
    elif answer == 14:
        print(predictions[13], "\n")
        print(answer)
    elif answer == 15:
        print(predictions[14], "\n")
        print(answer)
    elif answer == 16:
        print(predictions[15], "\n")
        print(answer)
    elif answer == 17:
        print(predictions[16], "\n")
        print(answer)
    elif answer == 18:
        print(predictions[17], "\n")
        print(answer)
    elif answer == 19:
        print(predictions[18], "\n")
        print(answer)
    elif answer == 20:
        print(predictions[19], "\n")
        print(answer)
    print("_____________(8)_____________\n")
    answer = random.randint(1, list_range)
    continue
