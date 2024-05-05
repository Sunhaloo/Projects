import time

user_time = int(input("Please Enter The Time: "))

for x in range(user_time, 0, -1):
    # Modulus = Remainder
    seconds = x % 60
    # Modulus 60 because will not want placeholder in print go above 60
    mins = int(x / 60) % 60
    # Hours can go beyond 60 Hours; Hence no Modulus 60
    hours = int(x / 3600)
    print(f"{hours:02}:{mins:02}:{seconds:02}")
    time.sleep(1)

    if x == -1:
        print("Exiting")
        exit()
