import random


def build_standard_deck() -> list[dict]:
    list_of_all_cards = []
    list_of_suit = ["H","C","D","S"]
    list_of_cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in range(13):
        for suit in list_of_suit:
            list_of_all_cards.append({"rank":list_of_cards[i],"suit":suit})

    return list_of_all_cards


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps:
        i_index = random.randint(0,51)
        j_index = random.randint(0,51)
        if deck[i_index] != deck[j_index]:
            if deck[j_index]["suit"] == "H":
                if j_index % 5 == 0:
                    deck[i_index],deck[j_index] = deck[j_index],deck[i_index]
                    swaps -= 1
            if deck[j_index]["suit"] == "C":
                if j_index % 3 == 0:
                    deck[i_index],deck[j_index] = deck[j_index],deck[i_index]
                    swaps -= 1
            if deck[j_index]["suit"] == "D":
                if j_index % 2 == 0:
                    deck[i_index],deck[j_index] = deck[j_index],deck[i_index]
                    swaps -= 1
            if deck[j_index]["suit"] == "S":
                if j_index % 7 == 0:
                    deck[i_index],deck[j_index] = deck[j_index],deck[i_index]
                    swaps -= 1
    return deck





