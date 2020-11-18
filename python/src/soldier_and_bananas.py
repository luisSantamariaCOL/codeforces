def main():
    word = input().split(' ')
    cost_banana = int(word[0])
    initial_dollars = int(word[1])
    n = int(word[2])
    total = 0
    for i in range(1,n+1):
        total += cost_banana*i;
    must_borrow = total-initial_dollars
    if must_borrow < 0:
        print(0)
    else:
        print(must_borrow)



if __name__ == "__main__":
    main()