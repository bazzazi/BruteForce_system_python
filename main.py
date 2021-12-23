import random , pyautogui

password = pyautogui.password('Enter your password')
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
guess_pass = []
while list(password) != guess_pass:
    guess_pass = random.choices(alphabet, k=len(password))
    print(f"<==================== {guess_pass} ====================>")
    if list(password) == guess_pass:
        print("\n****************************")
        print(f"your password is {''.join(guess_pass)}")
        print("****************************")
