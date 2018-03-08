def play_again():
    answer = ""
    while answer not in ["Y", "N"]:
        answer = input("Do you want to play again (Y or N)? ").upper()
    if answer == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    play_again()