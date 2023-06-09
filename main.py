import random
import time
import tarot_deck as td

td_keys = list(td.tarot_deck.keys())
count = 0


def get_reading(reading_type, question):
    random_card = random.choice(td_keys)
    random_int = random.randint(0, 1)
    global count
    count += 1

    print(f"you asked the cards: {question}, and the cards said this about your {reading_type}...\n")

    if random_int == 1:
        print(
            f"{td.tarot_deck[random_card]['name']} normal\n{td.tarot_deck[random_card]['description']}\n{td.tarot_deck[random_card][f'normal {reading_type}']}")
    else:
        print(
            f"{td.tarot_deck[random_card]['name']} reversed\n{td.tarot_deck[random_card]['description']}\n{td.tarot_deck[random_card][f'upsidedown {reading_type}']}")

    td_keys.remove(random_card)
    print("\n")


def theDraw(how_many, question):
    reading_types = {
        "1": "past",
        "2": "present",
        "3": "future",
        "4": "career",
        "5": "love",
    }

    for i in how_many:
        if i in reading_types:
            get_reading(reading_types[i], question)
        elif i == " ":
            pass
        else:
            print(f"\n{i} is an invalid input, please try again\n")


def main():
    print("Welcome to the Tarot Deck, a tool for divination and self reflection\n\n"
          "This deck is based on the Rider-Waite tarot deck, and is a 78 card deck\n"
          "The deck is split into 22 major arcana cards and 56 minor arcana cards\n"
          "Type in the numbers associated with the spread you would like to use\n"
          "type 1 for past, 2 for present, 3 for future, 4 for career, 5 for love or type all for all")
    how_many = input("Enter the number associated with the spread you would like to use: \n").lower()
    if how_many == "all":
        how_many = "12345"

    print("\n")

    answer = input("How many times do you want the deck shuffled? \n")
    print("Take some time to sit with the deck as you shuffle it")
    time_answer = int(input("how long would you like to work with the deck (in seconds)? \n"))
    time.sleep(time_answer)

    for i in range(int(answer)):
        random.shuffle(td_keys)

    print("\n")

    question = input("What question will you ask the cards? ")

    print("\n")

    theDraw(how_many, question)

    print(f"{count} cards have been drawn, you have {len(td_keys)} cards left in the deck \n"
          "Go in peace with the foreknowledge you have gained. It may change your path for the better \n"
          "or the worse, but will you be prepared for what is to come?")


if __name__ == "__main__":
    main()
