from readchar import readkey, key

#Program stops if the user presses the arrow up key
while True:
    print("Press any key:")
    k = readkey()
    if k == key.UP:
        break