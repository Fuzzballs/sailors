def greetings():
    count = input("How many crew members do we have today?: ")
    if float(count) > 1:
        names = input("Whats your name sailors?: ")
        print(f'Why hello there {names}! Welcome aboard!')
        worked = input("Are you ready to be worked?: ")
        if worked.lower() == "no":
            print("TOO BAD! ")
        else:
            print("Thats the spirit!")
    else:
        name = input("Whats your name sailor?: ")
        print(f'Welcome abourd {name}!')
        work = input("Are you ready to be worked?: ")
        if work.lower() == "no":
            print("TOO BAD!")
        else:
            print("Thats the spirite!")

   
greetings()
