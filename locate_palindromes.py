# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.


# Función que devuelve la cadena complementaria

def complement(sequence):
    reverse = list(sequence)[::-1]

    complement = []

    for template in reverse:

        if template not in ["A", "T", "C", "G"]:
                raise ValueError(f"Invalid letter {template} in sequence")
        if template == "A":
            complement.append("T")
        elif template == "T":
            complement.append("A")
        elif template == "C":
            complement.append("G")
        else:
            complement.append("C")

    return ''.join(complement)

# Función que busca motivos de cierto tamaño en una cadena

def find_motiv(string, motiv):
    i = 0
    motiv_len = len(motiv)
    positions = []

    for i in range(0,len(string)):
        j = i+motiv_len
        if string[i:j]== motiv:
            positions.append(i+1)

    return positions


# Abrir archivo

with open("test_data/fasta_palindromes.txt","r") as file:
    sequences = file.readlines()

seq = [line.strip() for line in sequences[1:]]

string = ''.join(seq)

motiv_lengths = [4,6,8,10,12] # Definir cómo partir la cadena original
#string = "TCAATGCATGCGGGTCTATATGCAT" # cadena original
comp = complement(string) # cadena complementaria 5'-3'


# Calcular las posiciones de los palindromes

for i in motiv_lengths:
    j = 0
    k = 0

    while j <= len(string)-i:
        k= j+i
        #print(i,j,k, len(string)-i, len(string))
        motiv = string[j:k]
        positions = find_motiv(comp,motiv)

        if positions:
            #print(j+1," ",i)
            #print(positions)
            #print(motiv)
            for m in positions:
                #print(m,len(comp)-(m+i),m,j,i)
                if len(comp)-(m+i)+1 == j:
                    print(j+1," ",i)
                    with open('output.txt', 'a') as f:
                        f.write(f"{j+1} {i}\n")



        j += 1


