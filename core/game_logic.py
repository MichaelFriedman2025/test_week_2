from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    sum_value = 0
    checking_how_many_a_there_are = 0
    for i in hand[0:2]:
        if i["rank"] == "A":
            checking_how_many_a_there_are += 1
        elif i["rank"].isdigit():
            sum_value += int(i["rank"])
        else:
            sum_value += 10

    if checking_how_many_a_there_are == 1:
        if 7 >= sum_value <= 10:
            sum_value += 11
    elif checking_how_many_a_there_are == 2:
        sum_value = 12

    for i in hand[2:]:
        if i["rank"] == "A":
            if 7 >= sum_value <= 10:
                sum_value += 11
            else:
                sum_value += 1
        elif i["rank"].isdigit():
            sum_value += int(i["rank"])
        else:
            sum_value += 10

    return sum_value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_1_pop = deck.pop()
    card_2_pop = deck.pop()
    player["hand"].append(card_1_pop)
    player["hand"].append(card_2_pop)
    print(f"the sum of cards of player is: {calculate_hand_value(player["hand"])}")

    card_3_pop = deck.pop()
    card_4_pop = deck.pop()
    dealer["hand"].append(card_3_pop)
    dealer["hand"].append(card_4_pop)
    print(f"the sum of cards of dealer is: {calculate_hand_value(dealer["hand"])}")

    return None


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    sum_dealer_cards = calculate_hand_value(dealer["hand"])
    while sum_dealer_cards < 17:
        card_pop = deck.pop()
        dealer["hand"].append(card_pop)
        print(f"the sum cards of the dealer is: {calculate_hand_value(dealer["hand"])}")
        sum_dealer_cards = calculate_hand_value(dealer["hand"])
    if sum_dealer_cards > 21:
        print(f"the dealer lose")
        return False
    else:
        return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while True:
        player_answer = ask_player_action()
        match player_answer:
            case "H":
                card_pop = deck.pop()
                player["hand"].append(card_pop)
                calculate_hand_player = calculate_hand_value(player["hand"])

                if calculate_hand_player > 21:
                    print(f"the sum cards of player is: {calculate_hand_player}\n"
                          f"player lose")
                    break
                else:
                    print(f"the sum cards of player is: {calculate_hand_player}\n")

            case "S":
                turn_dealer = dealer_play(deck,dealer)
                if turn_dealer:
                    calculate_hand_player = calculate_hand_value(player["hand"])
                    calculate_hand_dealer = calculate_hand_value(dealer["hand"])
                    if calculate_hand_dealer > calculate_hand_player:
                        print(f"the dealer won.")
                    elif calculate_hand_dealer < calculate_hand_player:
                        print(f"the player won.")
                    else:
                        print(f"Nobody won.")
                    print(f"the sum card of player is: {calculate_hand_player}\n"
                          f"and the sum card of dealer is: {calculate_hand_dealer}")
                break

