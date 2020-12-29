secret_word = "Merry Christmas"
tries = 0
user_guess = ""
while user_guess != secret_word:
    if tries % 2 == 0:
        print("It's a Christian holiday, come on hoe,, guesss!!")

    if user_guess == "Halloween":
        print("I know you didn't just say Halloween")

    if tries == 3:
        print("Whatever happened to the 3rd one being the charm lol")

    tries += 1
    user_guess = input("Enter your guess ;) : ")

if tries > 0:
    print('You found the answer, now take a shot!!')
