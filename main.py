import datetime
import json
import random

player = input("Insert your name: ")
secret = random.randint(1, 10)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}.".format(score_dict.get("player_name"),
                                                                                         str(score_dict.get("attempts")),
                                                                                         score_dict.get("date"),
                                                                                         score_dict.get("secret_number"))
    print(score_text)

wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player, "secret_number": secret, "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("So congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("You're wrong... try smaller")
    elif guess < secret:
        print("You're wrong... try bigger")

    wrong_guesses.append(guess)