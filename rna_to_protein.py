### Translate RNA string to protein

import pandas as pd

file = "codon_table.txt"

codonTable = pd.read_table(file, delim_whitespace=True, header=None)

codonDict = {}

for i in range(0,7,2):
    for j in range(0,16):
        codonDict[codonTable.iloc[j][i]] = codonTable.iloc[j][i+1]
    
with open("test_data/rna_string.txt","r") as file:
    rnaString = file.readline()

proteinString = ''

for i in range(0,len(rnaString),3):
    codon = rnaString[i:i+3]

    if (codonDict[codon] != "Stop") & (codon in codonDict.keys()):
        proteinString += codonDict[codon]
    
    if (codonDict[codon] == "Stop"):
        break


with open("output_data/output_rna_to_protein.txt", "w") as file:
    file.write(proteinString)
