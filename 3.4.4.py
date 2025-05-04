# Leap year validator code
# IF num % 4 == 0 && (num % 100 != 0 || num % 400 == 0)
while True:
    yr = int(input("Enter year: "))

    if (yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)):
        print("leap")
    else:
        print('noleap')