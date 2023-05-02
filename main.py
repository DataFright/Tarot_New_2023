import random
import time
import tarot_deck as td

td_keys = list(td.tarot_deck.keys())

print("Welcome to the Tarot Deck, a tool for divination and self reflection")
print("type 1 for past, 2 for present, 3 for future, 4 for career, 5 for love")
how_many = input("Enter the number associated with the spread you would like to use: \n")

print("\n")

answer = input("How many times do you want the deck shuffled? ")
print("Take some time to sit with the deck as you shuffle it")
time_answer = int(input("how long would you like to work with the deck (in seconds)? "))
time.sleep(time_answer)

for i in range(int(answer)):
    random.shuffle(td_keys)

print("\n")

question = input("What question will you ask the cards? ")

print("\n")


def past():
    random_card_past = random.choice(td_keys)
    random_int_1 = random.randint(0, 1)

    print("you asked the cards: ", question, ", and the cards said this about your past...\n")

    if random_int_1 == 1:
        print(td.tarot_deck[random_card_past]["name"], "\n", td.tarot_deck[random_card_past]["description"], "\n",
              td.tarot_deck[random_card_past]["normal reading past"])
    else:
        print(td.tarot_deck[random_card_past]["name"], "reversed", "\n", td.tarot_deck[random_card_past]["description"],
              "\n",
              td.tarot_deck[random_card_past]["upsidedown reading past"])

    td_keys.remove(random_card_past)

    print("\n")


def present():
    random_card_present = random.choice(td_keys)
    random_int_2 = random.randint(0, 1)

    print("you asked the cards: ", question, ", and the cards said this about your present...\n")

    if random_int_2 == 1:
        print(td.tarot_deck[random_card_present]["name"], "\n", td.tarot_deck[random_card_present]["description"], "\n",
              td.tarot_deck[random_card_present]["normal present"])
    else:
        print(td.tarot_deck[random_card_present]["name"], "reversed", "\n",
              td.tarot_deck[random_card_present]["description"], "\n",
              td.tarot_deck[random_card_present]["upsidedown present"])

    td_keys.remove(random_card_present)

    print("\n")


def future():
    random_card_future = random.choice(td_keys)
    random_int_3 = random.randint(0, 1)

    print("you asked the cards: ", question, ", and the cards said this about your future...\n")

    if random_int_3 == 1:
        print(td.tarot_deck[random_card_future]["name"], "\n", td.tarot_deck[random_card_future]["description"], "\n",
              td.tarot_deck[random_card_future]["normal future"])
    else:
        print(td.tarot_deck[random_card_future]["name"], "reversed", "\n",
              td.tarot_deck[random_card_future]["description"], "\n",
              td.tarot_deck[random_card_future]["upsidedown future"])

    td_keys.remove(random_card_future)

    print("\n")


def career():
    random_card_career = random.choice(td_keys)
    random_int_4 = random.randint(0, 1)

    print("you asked the cards: ", question, ", and the cards said this about your career...\n")

    if random_int_4 == 1:
        print(td.tarot_deck[random_card_career]["name"], "\n", td.tarot_deck[random_card_career]["description"], "\n",
              td.tarot_deck[random_card_career]["normal career"])
    else:
        print(td.tarot_deck[random_card_career]["name"], "reversed", "\n",
              td.tarot_deck[random_card_career]["description"], "\n",
              td.tarot_deck[random_card_career]["upsidedown career"])

    td_keys.remove(random_card_career)

    print("\n")


def love():
    random_card_love = random.choice(td_keys)
    random_int_5 = random.randint(0, 1)

    print("you asked the cards: ", question, ", and the cards said this about your love life...\n")

    if random_int_5 == 1:
        print(td.tarot_deck[random_card_love]["name"], "\n", td.tarot_deck[random_card_love]["description"], "\n",
              td.tarot_deck[random_card_love]["normal love"])
    else:
        print(td.tarot_deck[random_card_love]["name"], "reversed", "\n", td.tarot_deck[random_card_love]["description"],
              "\n",
              td.tarot_deck[random_card_love]["upsidedown love"])

    td_keys.remove(random_card_love)

    print("\n")

def theDraw():
    for i in how_many:
        for h in i:
            if h == "1":
                past()
            elif h == "2":
                present()
            elif h == "3":
                future()
            elif h == "4":
                career()
            elif h == "5":
                love()
            else:
                print("invalid input, please try again")

theDraw()

print("Go with peace for the foreknowledge you have gained may change your path for the better \n"
      "or the worse, but you will be prepared for what is to come")
