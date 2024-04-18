### Problema: obtener el complemento de una secuencia de ADN

test_file_path = "test_data/rosalind_revc_1_dataset.txt"

# with es una forma util de abrir archivos sin tenerlos que cerrar de nuevo
with open(test_file_path,"r") as file:
    sequence = file.read().strip()

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
        

str_complement = ''.join(complement)



print(''.join(complement))
