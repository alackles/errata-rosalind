# Calculate the total weight of a protein.

def main():
    
    # Generate protein mass dictionary

    mmt = {}

    with open("ref/protein_mass.txt") as f:
        for line in f:
            mmt[line.split()[0]] = float(line.split()[1])

    with open("datafiles/rosalind_prtm.txt") as f:
        p = f.readline().strip()

    mass = sum([mmt[aa] for aa in p])
    
    print(round(mass,3))

if __name__ == "__main__":
    main()
