def main():
    username = input()
    char_list = []
    for i in username:
        if i not in char_list:
            char_list.append(i)
    is_even(len(char_list))

def is_even(number):
    if number % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    main()