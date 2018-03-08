def play_again():
    while True:
        answer = input("Do you want to play again (Y or N)? ").upper()
        if answer not in ["Y", "N"]:
            print("Invalid input.")
        else:
            break
    if answer == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    play_again()