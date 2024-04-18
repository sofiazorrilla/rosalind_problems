## Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

## Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

file_path = "test_data/test_gc_content.fasta"

def calc_max_gc(file_path):

    with open(file_path, "r") as file:
            fasta = file.readlines()

    result = {}
    gc = 0
    length = 0

    for seq in fasta:
        
        if seq[0] == ">":
            id = seq[1:].strip()
            gc = 0
            length = 0

        else:
            seq = seq.strip()
            length += len(seq)
            
            for i in seq:
                if i == "G" or i == "C":
                    gc += 1

            result[id] = gc/length*100     

    max_key = max(result, key=result.get)

    print(max_key)
    print(result[max_key])

    #return max_key, result[max_key]
    return result

calc_max_gc(file_path)



