def main():
    import sys
    for line in sys.stdin.readlines():
        soln = solution(line.strip('\n'))
        print(soln)


def solution(word):
    start_point = strip_type(word)
    portion = ""
    for index, letter in enumerate(start_point):
        if letter.isupper() and index == 0:
            portion += letter.lower()
        if letter.isupper() and index != 0:
            portion += f'_{letter.lower()}'
        if letter.islower():
            portion += letter
    return portion


def strip_type(word):
    count = 0
    for i in word:
        if i.isupper():
            break
        count += 1
    return word[count:]



if __name__ == "__main__":
    main()
