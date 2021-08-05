#Abre o arquivo resultado do job dataproc Hadoop
filein = open('resultado_part-00000','r', encoding='utf-8')

#Cria o Arquivo com o resultado final
fileout = open('resultado.txt','w')

#Lê somente as 10 primeiras linhas, visto que o arquivo já vem com as palavras e as quantidades delas 
#em ordem decrescente
x=1
#Escrevendo Cabeçalho 
fileout.writelines('######## 10 PALAVRAS MAIS CITADAS NO LIVRO ######## \n \n')
for linha in filein:
    #Transforma cada linha e escreve a linha formatada no arquivo resultado.txt
    newline = linha.replace('(', '')
    newline = newline.replace(')', '')
    newline = newline.replace("'", "").split(',')
    conteudo = str(x) +'. '+str(newline[0]).strip()+' --> '+str(newline[1]).strip()+'\n'
 
    #Desconsidera alguma contagem de caracter em branco
    if newline[0] != '':
            fileout.writelines(conteudo)
            x += 1

    #Sai quando ler as 10 primeriras linhas
    if x>10:
        break
        
#Fechas os arquivos
filein.close()
fileout.close()

