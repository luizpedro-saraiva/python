nota = int (input("Digite a nota do aluno: "))

# Verifica se a nota está fora do intervalo permitido
if nota < 0 or nota > 10:
    print("Erro: A nota deve ser entre 0 e 10.")
else:
    
    if nota >= 8:
        print ("Nota Excelente")

    elif nota >=6: 
     print ("Nota Boa")

    else: 
        print ("Nota Ruim")