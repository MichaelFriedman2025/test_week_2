def ask_player_action() -> str:
    check = True
    answer = ""
    while check:
        answer = input("please enter the letter: 'H' for open a card,\n"
                       "                     or: 'S' for stand. \n ")

        answer = answer.upper()

        if answer == "H" or answer == "S":
            check = False

    return answer


