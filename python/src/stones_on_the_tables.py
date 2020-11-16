def main():
    n = int(input())
    stones = input()
    count = 0
    for i in range(n-1):
        if stones[i] == stones[i+1]:
            count+=1
    print(count)

if __name__ == '__main__':
    main()