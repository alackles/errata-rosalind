def main():

    worddict = {}

    with open("rosalind_ini6.txt") as f:
        wordlist = [word.strip() for word in f.readline().split(' ')]
    
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    counts = []
    for key, value in worddict.items():
        counts.append(key + " " + str(value) + "\n")

    with open("rosalind_ini6_sol.txt", "w") as f:
        for line in counts:
            f.write(line)

if __name__ == "__main__":
    main()
