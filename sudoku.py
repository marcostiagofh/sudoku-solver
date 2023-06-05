from datetime import datetime

def print_candidatos_celula():
    global candidatos_celula

    l = 1
    while l <= 9:
        print(candidatos_celula[l][1:4],'|',candidatos_celula[l][4:7],'|',candidatos_celula[l][7:10])
        l += 1
        
def print_freq():
    global freq_candidato_bloco
    global freq_candidato_linha
    global freq_candidato_coluna    

    n = 1
    while n <= 9:
      print(n,':')
      b = 1
      while b <= 9:
        print('bloco',b,'freq',freq_candidato_bloco[b][n])
        b += 1
      l = 1
      while l <= 9:
        print('linha',l,'freq',freq_candidato_linha[l][n])
        l += 1
      c = 1
      while c <= 9:
        print('coluna',c,'freq',freq_candidato_coluna[c][n])
        c += 1
      n += 1

def verificar_freq_1():
    print('chamada verificar_freq_1()')
    global freq_candidato_bloco
    global freq_candidato_linha
    global freq_candidato_coluna
    global sudoku
    global candidato_celula
    global index_linhas
    global index_colunas
    global celulas_percorridas

    alguma_preenchida = 0
    
    print('block processing')
    #para cada elemento na matriz preenchidos bloco        
    b1 = 1
    while b1 <= 9:
        num = 1
        while num <= 9:
            if freq_candidato_bloco[b1][num] == 1:          
                #procurar posicao do bloco atual que possui tal numero como candidato e preencher
                l = index_linhas[b1]
                l_end = l + 2
                while l <= l_end:
                    c = index_colunas[b1]
                    c_end = c + 2
                    while c <= c_end:
                        celulas_percorridas += 1
                        if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
                            fill_sudoku_cell(b1,l,c,num)
                            alguma_preenchida = 1
                        c += 1
                    l += 1
            num += 1
        b1 += 1
    
    print('line processing')
    #para cada elemento na matriz preenchidos linha
    l = 1
    while l <= 9:
        num = 1
        while num <= 9:
            if freq_candidato_linha[l][num] == 1:           
                #procurar posicao da linha atual que possui tal numero como candidato e preencher
                c = 1
                while c <= 9:
                    celulas_percorridas += 1
                    if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
                        b = int((l-1)/3) * 3 + int((c-1)/3) + 1
                        fill_sudoku_cell(b,l,c,num)
                        alguma_preenchida = 1
                    c += 1  
            num += 1                
        l += 1

    print('column processing')
    #para cada elemento na matriz preenchidos coluna
    c = 1
    while c <= 9:
        num = 1
        while num <= 9:
            if freq_candidato_coluna[c][num] == 1:          
                #procurar posicao da coluna atual que possui tal numero como candidato e preencher
                l = 1
                while l <= 9:
                    celulas_percorridas += 1
                    if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
                        b = int((l-1)/3) * 3 + int((c-1)/3) + 1
                        fill_sudoku_cell(b,l,c,num)
                        alguma_preenchida = 1
                    l += 1
            num += 1                
        c += 1

    return alguma_preenchida

def naked_pair(b):
    print('chamada naked_pair(',b,')')
    global candidatos_celula
    global sudoku
    global freq_candidato_bloco
    global freq_candidato_linha
    global freq_candidato_coluna
    global celulas_percorridas
    global index_linhas
    global index_colunas

    freq = 0

    celulas_candidato_unico = []

    alteracao_candidatos = 0
    
    cells_of_presence = []
    
    #actual block processing
    l1 = index_linhas[b]
    l1_end = l1 + 2
    while l1 <= l1_end:
        c1 = index_colunas[b]
        c1_end = c1 + 2
        while c1 <= c1_end:
            celulas_percorridas += 1
            if l1 == l1_end and c1 == c1_end:
                break
            else:
                arr1 = candidatos_celula[l1][c1]
                cells_of_presence = [[l1,c1]]
                freq = 1
                l2 = l1
                c2 = c1 + 1
                while l2 <= l1_end:
                    while c2 <= c1_end:  
                        celulas_percorridas += 1
                        arr2 = candidatos_celula[l2][c2]
                        
                        if arr1 == arr2:
                            freq += 1
                            cells_of_presence.append([l2,c2])
                            
                        c2 += 1
                    c2 = index_colunas[b]
                    l2 += 1
                if freq == len(arr1) and freq > 1:
                    print(arr1,'block processing',b)
                    l = index_linhas[b]
                    l_end = l + 2
                    while l <= l_end:
                        c = index_colunas[b]
                        c_end = c + 2
                        while c <= c_end:
                            celulas_percorridas += 1
                            if [l,c] not in cells_of_presence:
                                for num in arr1:
                                    if num in candidatos_celula[l][c]:
                                        alteracao_candidatos = 1
                                        freq_candidato_bloco[b][num] -= 1 
                                        freq_candidato_linha[l][num] -= 1
                                        freq_candidato_coluna[c][num] -= 1
                                        candidatos_celula[l][c].remove(num)
                                        if len(candidatos_celula[l][c]) == 1:
                                            celulas_candidato_unico.append([b,l,c])
                            c += 1
                        l += 1
            c1 += 1
        l1 += 1
        
    #line 1 to 3 processing    
    l1 = index_linhas[b]
    l1_end = l1 + 2
    while l1 <= l1_end:
        c1 = 1
        c1_end = 9
        while c1 < c1_end:        
            celulas_percorridas += 1
            arr1 = candidatos_celula[l1][c1]
            cells_of_presence = [[l1,c1]]
            freq = 1
            l2 = l1
            c2 = c1 + 1                
            while c2 <= 9:   
                celulas_percorridas += 1
                arr2 = candidatos_celula[l2][c2]
                
                if arr1 == arr2:
                    freq += 1
                    cells_of_presence.append([l2,c2])
                    
                c2 += 1                
            
            if freq == len(arr1) and freq > 1:
                print(arr1,'line processing',l1)
                l = l1
                
                c = 1
                c_end = 9
                while c <= c_end:
                    celulas_percorridas += 1
                    if [l,c] not in cells_of_presence:
                        for num in arr1:
                            if num in candidatos_celula[l][c]:
                                alteracao_candidatos = 1
                                b = int((l-1)/3) * 3 + int((c-1)/3) + 1
                                freq_candidato_bloco[b][num] -= 1  
                                freq_candidato_linha[l][num] -= 1 
                                freq_candidato_coluna[c][num] -= 1         
                                candidatos_celula[l][c].remove(num)
                                if len(candidatos_celula[l][c]) == 1:                                    
                                    celulas_candidato_unico.append([b,l,c])
                    c += 1
            c1 += 1
        l1 += 1
        
    #column 1 to 3 processing    
    c1 = index_colunas[b]
    c1_end = c1 + 2
    while c1 <= c1_end:
        l1 = 1
        l1_end = 9
        while l1 < l1_end:
            celulas_percorridas += 1
            arr1 = candidatos_celula[l1][c1]
            cells_of_presence = [[l1,c1]]
            freq = 1
            l2 = l1 + 1
            c2 = c1
            while l2 <= l1_end:    
                celulas_percorridas += 1
                arr2 = candidatos_celula[l2][c2]
                
                if arr1 == arr2:
                    freq += 1
                    cells_of_presence.append([l2,c2])
                    
                l2 += 1                
                
            if freq == len(arr1) and freq > 1:
                print(arr1,'column processing',c1)
                l = 1
                l_end = 9
                c = c1
                while l <= l_end:
                    celulas_percorridas += 1
                    if [l,c] not in cells_of_presence:
                            for num in arr1:
                                if num in candidatos_celula[l][c]:
                                    alteracao_candidatos = 1
                                    b = int((l-1)/3) * 3 + int((c-1)/3) + 1
                                    freq_candidato_bloco[b][num] -= 1    
                                    freq_candidato_linha[l][num] -= 1
                                    freq_candidato_coluna[c][num] -= 1
                                    candidatos_celula[l][c].remove(num)
                                    if len(candidatos_celula[l][c]) == 1:
                                        celulas_candidato_unico.append([b,l,c])
                    l += 1
            l1 += 1
        c1 += 1

    for e in celulas_candidato_unico:
        b,l,c = e
        if sudoku[l][c] == 0:
            num = candidatos_celula[l][c][0]
            fill_sudoku_cell(b,l,c,num) 

    return alteracao_candidatos            

def verificar_candidatos_eliminar(b):
    print('chamada verificar_candidatos_eliminar(',b,')')
    global nao_preenchidos_bloco
    global candidatos_celula
    global sudoku
    global freq_candidato_bloco
    global freq_candidato_linha
    global freq_candidato_coluna
    global celulas_percorridas
    global index_linhas
    global index_colunas

    l1,c1 = [0,0]
    l2,c2 = [0,0]
    tipo_adj = 0 #1 p horizontal, 2 p vertical, 3 p os dois (l1 != 0 and l2 == 0)

    celulas_candidato_unico = []

    alteracao_candidatos = 0

    n = 0
    n_end = len(nao_preenchidos_bloco[b])
    while n < n_end:
        num = nao_preenchidos_bloco[b][n]
        l1,c1 = [0,0]
        l2,c2 = [0,0]
        tipo_adj = 0
        l = index_linhas[b]
        l_end = l + 2
        while l <= l_end:
            c = index_colunas[b]
            c_end = c + 2
            while c <= c_end:
                celulas_percorridas += 1
                if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
                    if tipo_adj != 0:
                            if tipo_adj == 1 and l != l1 or tipo_adj == 2 and c != c1:
                                    tipo_adj = 0
                                    c = c_end
                                    l = l_end
                                    break       
                    elif l1 != 0:
                            l2,c2 = [l,c]
                            if l2 == l1:
                                    tipo_adj = 1
                            elif c2 == c1:
                                    tipo_adj = 2
                            else:
                                    l = l_end
                                    c = c_end
                                    break                           
                    else:
                            l1,c1 = [l,c]
                c += 1
            l += 1
        if tipo_adj == 1:
            print('horizontal, linha:',l1,'num:',num)
            cn = 1
            cn_end = index_colunas[b]
            while cn < cn_end:
                celulas_percorridas += 1
                if sudoku[l1][cn] == 0 and num in candidatos_celula[l1][cn]:
                        alteracao_candidatos = 1
                        candidatos_celula[l1][cn].remove(num) 
                        bn = int((l1-1)/3) * 3 + int((cn-1)/3) + 1
                        freq_candidato_bloco[bn][num] -= 1
                        freq_candidato_linha[l1][num] -= 1
                        freq_candidato_coluna[cn][num] -= 1  
                        if len(candidatos_celula[l1][cn]) == 1:
                            celulas_candidato_unico.append([bn,l1,cn])
                cn += 1
            cn = index_colunas[b] + 3
            cn_end = 9
            while cn < cn_end:
                celulas_percorridas += 1
                if sudoku[l1][cn] == 0 and num in candidatos_celula[l1][cn]:
                    alteracao_candidatos = 1
                    candidatos_celula[l1][cn].remove(num) 
                    bn = int((l1-1)/3) * 3 + int((cn-1)/3) + 1
                    freq_candidato_bloco[bn][num] -= 1
                    freq_candidato_linha[l1][num] -= 1
                    freq_candidato_coluna[cn][num] -= 1    
                    if len(candidatos_celula[l1][cn]) == 1:
                        celulas_candidato_unico.append([bn,l1,cn])
                cn += 1
        if tipo_adj == 2:
            print('vertical, coluna:',c1,'num:',num)
            ln = 1
            ln_end = index_linhas[b]
            while ln < ln_end:
                celulas_percorridas += 1
                if sudoku[ln][c1] == 0 and num in candidatos_celula[ln][c1]:
                    alteracao_candidatos = 1
                    candidatos_celula[ln][c1].remove(num) 
                    bn = int((ln-1)/3) * 3 + int((c1-1)/3) + 1
                    freq_candidato_bloco[bn][num] -= 1
                    freq_candidato_linha[ln][num] -= 1
                    freq_candidato_coluna[c1][num] -= 1
                    if len(candidatos_celula[ln][c1]) == 1:
                        celulas_candidato_unico.append([bn,ln,c1])
                ln += 1
            ln = index_linhas[b] + 3
            ln_end = 9
            while ln < ln_end:
                celulas_percorridas += 1
                if sudoku[ln][c1] == 0 and num in candidatos_celula[ln][c1]:
                    alteracao_candidatos = 1
                    candidatos_celula[ln][c1].remove(num) 
                    bn = int((ln-1)/3) * 3 + int((c1-1)/3) + 1
                    freq_candidato_bloco[bn][num] -= 1
                    freq_candidato_linha[ln][num] -= 1
                    freq_candidato_coluna[c1][num] -= 1
                    if len(candidatos_celula[ln][c1]) == 1:
                        celulas_candidato_unico.append([bn,ln,c1])
                ln += 1
        n += 1

    for e in celulas_candidato_unico:
        b,l,c = e
        if sudoku[l][c] == 0:
            num = candidatos_celula[l][c][0]
            fill_sudoku_cell(b,l,c,num)     

    return alteracao_candidatos            

def fill_sudoku_cell(b,l,c,num):
    print('chamada fill_sudoku_cell(',b,',',l,',',c,',',num,')')
    global sudoku
    global pendentes
    global freq_candidato_bloco
    global freq_candidato_linha
    global freq_candidato_coluna
    global linha
    global coluna
    global bloco
    global nao_preenchidos_bloco
    global candidatos_celula
    global celulas_preenchidas
    global celulas_percorridas
    global index_linhas
    global index_colunas

    celulas_preenchidas += 1
    sudoku[l][c] = num
    #print_sudoku(sudoku)
    print('sudoku[',l,'][',c,'] = ',num)
    pendentes -= 1
    if pendentes == 0:
        print('celulas percorridas:',celulas_percorridas,'celulas preenchidas:',celulas_preenchidas)
        print_sudoku(sudoku)
        final_program = datetime.now()
        print('Time program:',final_program-initial_program)
        exit()

    linha[num][l] = 1
    coluna[num][c] = 1
    bloco[num][b] = 1
    nao_preenchidos_bloco[b].remove(num)
    freq_candidato_bloco[b][num] = 0
    freq_candidato_linha[l][num] = 0
    freq_candidato_coluna[c][num] = 0
    for num1 in candidatos_celula[l][c]:
        freq_candidato_bloco[b][num1] -= 1
        freq_candidato_linha[l][num1] -= 1
        freq_candidato_coluna[c][num1] -= 1        
    candidatos_celula[l][c] = []

    celulas_candidato_unico = []

    
    l1 = index_linhas[b]
    l1_end = l1 + 2
    while l1 <= l1_end:
        c1 = index_colunas[b]
        c1_end = c1 + 2
        while c1 <= c1_end:
            celulas_percorridas += 1
            if sudoku[l1][c1] == 0 and num in candidatos_celula[l1][c1]:
                freq_candidato_bloco[b][num] -= 1
                freq_candidato_linha[l1][num] -= 1
                freq_candidato_coluna[c1][num] -= 1
                candidatos_celula[l1][c1].remove(num)
                if len(candidatos_celula[l1][c1]) == 1:
                    celulas_candidato_unico.append([b,l1,c1])
            c1 += 1
        l1 += 1


    c1 = 1
    while c1 <= 9:
        celulas_percorridas += 1 
        if sudoku[l][c1] == 0 and num in candidatos_celula[l][c1]:
            b1 = int((l-1)/3) * 3 + int((c1-1)/3) + 1
            freq_candidato_bloco[b1][num] -= 1
            freq_candidato_linha[l][num] -= 1
            freq_candidato_coluna[c1][num] -= 1
            candidatos_celula[l][c1].remove(num)
            if len(candidatos_celula[l][c1]) == 1:
                celulas_candidato_unico.append([b1,l,c1])
        c1 += 1

    l1 = 1
    while l1 <= 9:
        celulas_percorridas += 1
        if sudoku[l1][c] == 0 and num in candidatos_celula[l1][c]:
            b1 = int((l1-1)/3) * 3 + int((c-1)/3) + 1
            freq_candidato_bloco[b1][num] -= 1
            freq_candidato_linha[l1][num] -= 1
            freq_candidato_coluna[c][num] -= 1
            candidatos_celula[l1][c].remove(num)
            if len(candidatos_celula[l1][c]) == 1:
                celulas_candidato_unico.append([b1,l1,c])
        l1 += 1

    for e in celulas_candidato_unico:
        b,l,c = e
        if sudoku[l][c] == 0:
            num = candidatos_celula[l][c][0]
            fill_sudoku_cell(b,l,c,num) 

    #print_candidatos_celula()
  

#fancy way to print sudoku puzzle cells
def print_sudoku(sudoku):
    l = 1
    while l <= 7:
        print(sudoku[l][1:4],'\t',sudoku[l][4:7],'\t',sudoku[l][7:10])
        print(sudoku[l+1][1:4],'\t',sudoku[l+1][4:7],'\t',sudoku[l+1][7:10])
        print(sudoku[l+2][1:4],'\t',sudoku[l+2][4:7],'\t',sudoku[l+2][7:10])
        print('\n')
        l += 3

#original state of puzzle chosen, 0-cells are the empty ones
sudoku_easy = [ \
[], \
[0,   0,0,0,   0,0,5,   7,8,0], \
[0,   0,1,2,   0,6,0,   0,4,0], \
[0,   0,5,0,   2,0,0,   1,0,0], \
\
[0,   0,0,7,   0,0,9,   0,0,0], \
[0,   0,6,0,   0,0,1,   0,0,0], \
[0,   5,0,0,   3,7,0,   9,0,0], \
\
[0,   3,0,4,   0,0,8,   0,2,5], \
[0,   2,7,0,   0,0,0,   8,9,0], \
[0,   1,0,0,   0,0,0,   3,0,0] \
]

sudoku_hard = [ \
[], \
[0,   0,7,0,   0,0,8,   0,6,0], \
[0,   1,0,0,   0,0,0,   0,0,5], \
[0,   0,0,0,   9,0,1,   0,0,0], \
\
[0,   3,0,9,   0,0,0,   8,0,0], \
[0,   0,0,0,   0,3,0,   0,0,0], \
[0,   0,0,5,   0,0,0,   2,0,1], \
\
[0,   0,0,0,   8,0,5,   0,0,0], \
[0,   7,0,0,   0,0,0,   0,0,6], \
[0,   0,8,0,   3,0,0,   0,2,0] \
]

sudoku_hardest = [ \
[], \
[0,   0,7,0,   2,5,0,   4,0,0], \
[0,   8,0,0,   0,0,0,   9,0,3], \
[0,   0,0,0,   0,0,3,   0,7,0], \
\
[0,   7,0,0,   0,0,4,   0,2,0], \
[0,   1,0,0,   0,0,0,   0,0,7], \
[0,   0,4,0,   5,0,0,   0,0,8], \
\
[0,   0,9,0,   6,0,0,   0,0,0], \
[0,   4,0,1,   0,0,0,   0,0,5], \
[0,   0,0,7,   0,8,2,   0,3,0] \
]

#choose a puzzle to solve
sudoku = sudoku_hardest

print_sudoku(sudoku)    

initial_program = datetime.now()
    
#variable declaring
linha = [[]] #relation of presence of each digit on each of the lines from 1 to 9
coluna = [[]] #relation of presence of each digit on each of the columns from 1 to 9
bloco = [[]] #digits already filled on each block
nao_preenchidos_bloco = [[]] #digits left to fill on each block
candidatos_celula = [[]]    #number candidates for each cell
pendentes = 81 #current number of empty cells; at the end, should be zero
freq_candidato_bloco = [[]]
freq_candidato_linha = [[]]
freq_candidato_coluna = [[]]
celulas_percorridas = 0
celulas_preenchidas = 0

index_linhas  = [0,1,1,1,4,4,4,7,7,7]
index_colunas = [0,1,4,7,1,4,7,1,4,7]

#in some variables, we use lists ranging from 0 to 9, so we can index 1 to 9, instead of 0 to 8, which would be confusing
l = 1
while l <= 9:
    linha.append([0,0,0,0,0,0,0,0,0,0])
    coluna.append([0,0,0,0,0,0,0,0,0,0])
    nao_preenchidos_bloco.append([1,2,3,4,5,6,7,8,9])   
    bloco.append([0,0,0,0,0,0,0,0,0,0]) 
    freq_candidato_bloco.append([0,0,0,0,0,0,0,0,0,0])
    freq_candidato_linha.append([0,0,0,0,0,0,0,0,0,0])
    freq_candidato_coluna.append([0,0,0,0,0,0,0,0,0,0])
    l += 1

#fill variables with pre-filled cells info
l = 1
while l <= 9:
    c = 1
    lista1 = [[]]
    while c <= 9:
        lista1.append([])
        if sudoku[l][c] != 0:
            pendentes -= 1
            num = sudoku[l][c]
            linha[num][l] = 1 #print('linha[',num,'][',l,'] = 1')
            coluna[num][c] = 1 #print('coluna[',num,'][',c,'] = 1')
            b = int((l-1)/3) * 3 + int((c-1)/3) + 1
            
            bloco[num][b] = 1 #print('bloco[',num,'][',b,'] = 1')
            nao_preenchidos_bloco[b].remove(num) #print(nao_preenchidos_bloco[b])           
        c += 1
    candidatos_celula.append(lista1)
    l += 1  

lista_candidato_unico = []
#now we list possible candidates for each non-filled cell
b = 1
while b <= 9:
    l = index_linhas[b]
    l_end = l + 2
    while l <= l_end:
        c = index_colunas[b]
        c_end = c + 2           
        while c <= c_end:
            celulas_percorridas += 1
            if sudoku[l][c] == 0:
                #print('b:',b,'l:',l,'c:',c,sudoku[l][c])
                n = 0
                n_end = len(nao_preenchidos_bloco[b])
                while n < n_end:
                    num = nao_preenchidos_bloco[b][n]
                    if linha[num][l] == 0 and coluna[num][c] == 0:
                        candidatos_celula[l][c].append(num)                     
                        freq_candidato_bloco[b][num] += 1
                        freq_candidato_linha[l][num] += 1
                        freq_candidato_coluna[c][num] += 1
                    n += 1              
                if len(candidatos_celula[l][c]) == 1:
                  lista_candidato_unico.append([b,l,c])
            c += 1
        l += 1  
    b += 1 

#print_candidatos_celula()
#print_freq()

for e in lista_candidato_unico:
    b,l,c = e
    if sudoku[l][c] == 0:
        num = candidatos_celula[l][c][0]
        fill_sudoku_cell(b,l,c,num)

alguma_preenchida = 1        
while alguma_preenchida:
    alguma_preenchida = verificar_freq_1()

a3 = 0
#here below, we rule out some cell candidates, based on the presence of that candidate number on same line or same column
while pendentes > 0: 
    b = 1
    while b <= 9:        
        a1 = verificar_candidatos_eliminar(b)
        a2 = naked_pair(b)
        if a1+a2+a3 > 0:
          a3 = verificar_freq_1()
        
        b += 1   

print_sudoku(sudoku)
#print_candidatos_celula()