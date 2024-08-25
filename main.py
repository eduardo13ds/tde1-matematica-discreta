# EDUARDO DOS SANTOS RODRIGUES
import colorama #importando biblioteca colorama para colorir os textos
from colorama import Back, Style
colorama.init(autoreset=True)


# LOCAL DE ALTERAÇÃO DO ARQUIVO ABAIXO EM f = open("nomedoarquivo.txt", "r")!
f = open("op3.txt", "r") #definindo arquivo txt com o seu caminho (apenas leitura)
lines = f.readlines() #definido lista com linhas do arquivo
f.close() #fechando arquivo para poupar recursos 

sets = [] #criando lista vazia, aonde será inserto as linhas dos arquivos txt

for line in lines: #iteração das linhas dentro do código
    set1 = line.strip().split(", ") #definindo a linha como set1, com strip e split para correta formatação e separação dos itens
    line = set(set1) #transformando set1, que antes era uma lista em um set e armazendo em line
    sets.append(line) #adicionando a linha agora em formato set na lista sets

count = 1 #iniciando contador para correta leitura posterior

print(f"{Back.MAGENTA} {Style.BRIGHT} TDE 1! CALCULADORA DE CONJUNTOS")
print(f"{Back.GREEN} {Style.BRIGHT} Prof. Andrey Cabral Meira - Matemática Discreta")
print(f"{Back.BLUE} {Style.BRIGHT} Eduardo dos Santos Rodrigues - Bacharelado em Ciência da Computação")
print()

for i, line in enumerate(lines): #iniciando a iteração da lista lines
    if line.strip() == 'U': #verificando a operação, neste caso união
        count += 1 #somando um ao contador
        conj1 = sets[count] #trazendo o conj1 que está localizado na lista sets no indice do contador - ([count])
        conj2 = sets[count + 1] #trazendo o conj2 que está localizado na lista de sets após o conj1, por isso, count + 1
        result = conj1.union(conj2) #fazendo a união dos sets com a função union
        if result == set(): #verificando se o resultado é vazio
            result = '{}' #armazenando a string '{}' como result
        print(f"União: conjunto 1: {conj1}, conjunto 2: {conj2}. Resultado: {result}\n") #imprimindo o resultado
        count += 2 #somando dois no contador da iteração para ir direto na proxima letra, por conta do padrão: a cada dois conjuntos uma operação
    elif line.strip() == 'I':
        count += 1
        conj1 = sets[count]
        conj2 = sets[count + 1]
        result = conj1.intersection(conj2)
        if result == set():
            result = '{}'
        print(f"Intersecção: conjunto 1: {conj1}, conjunto 2: {conj2}. Resultado: {result}\n")
        count += 2
    elif line.strip() == 'D':
        count += 1
        conj1 = sets[count]
        conj2 = sets[count + 1]
        result = conj1.difference(conj2) 
        if result == set():
            result = '{}'
        print(f"Diferença: conjunto 1: {conj1}, conjunto 2: {conj2}. Resultado: {result}\n")
        count += 2
    elif line.strip() == 'C':
        count += 1
        conj1 = sets[count]
        conj2 = sets[count + 1]
        conj1 = list(conj1) #transformando o conj1 em lista pois, preciso verificar a indexação, o que não é possível com sets
        conj2 = list(conj2) #transformando o conj2 em lista pois, preciso verificar a indexação, o que não é possível com sets
        result = []
        for i in range(0, len(conj1)): # iniciando iteração no range de 0 - n, n=len(conj1), isso é cada item do conjunto 1
            for j in range(0, len(conj2)): # iniciando iteração no range de 0 - n, n=len(conj2).
                temp = [item for item in conj1[i]] #adicionando o item de posição i do conj1 na lista temp
                temp.append(conj2[j]) #fazendo a inserção do item de posição j do conj2 na lista temp, agora temos temp = [conj1[i], conj2[j]]
                result.append(temp) #colocando a lista temporaria dentro do resultado
                #depois vai para a proxima letra do conj1 até encerrar
        print(f"Plano cartesiano dos conjuntos: conjunto 1: {conj1}, conjunto 2: {conj2}. Resultado: {result}\n")
