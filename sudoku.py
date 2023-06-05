from datetime import datetime

def verificar_candidatos_eliminar(b):
	print('chamada verificar_candidatos_eliminar(',b,')')
	global nao_preenchidos_bloco
	global candidatos_celula
	global sudoku
	global freq_candidato_bloco

	l1,c1 = [0,0]
	l2,c2 = [0,0]
	tipo_adj = 0 #1 p horizontal, 2 p vertical
	
	n = 0
	n_end = len(nao_preenchidos_bloco[b])
	while n < n_end:
		num = nao_preenchidos_bloco[b][n]
		l1,c1 = [0,0]
		l2,c2 = [0,0]
		tipo_adj = 0
		l = int((b-1)/3) * 3  + 1
		l_end = l + 2
		while l <= l_end:
			c = ((b-1)%3) * 3 + 1
			c_end = c + 2
			while c <= c_end:
				if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
					if tipo_adj != 0:
							if tipo_adj == 1 and l == l1:
									cn = 1
									cn_end = ((b-1)%3) * 3 + 1
									while cn < cn_end:
											if sudoku[l][cn] == 0 and num in candidatos_celula[l][cn]:
													candidatos_celula[l][cn].remove(num) 
													bn = int((l-1)/3) * 3 + int((cn-1)/3) + 1
													freq_candidato_bloco[bn][num] -= 1
											cn += 1
									cn = ((b-1)%3) * 3 + 1 + 3
									cn_end = 9
									while cn < cn_end:
											if sudoku[l][cn] == 0 and num in candidatos_celula[l][cn]:
													candidatos_celula[l][cn].remove(num) 
													bn = int((l-1)/3) * 3 + int((cn-1)/3) + 1
													freq_candidato_bloco[bn][num] -= 1
											cn += 1
							elif tipo_adj == 2 and c == c1:
									ln = 1
									ln_end = int((b-1)/3) * 3  + 1
									while ln < ln_end:
											if sudoku[ln][c] == 0 and num in candidatos_celula[ln][c]:
													candidatos_celula[ln][c].remove(num) 
													bn = int((ln-1)/3) * 3 + int((c-1)/3) + 1
													freq_candidato_bloco[bn][num] -= 1
											ln += 1
									ln = int((b-1)/3) * 3  + 1 + 3
									ln_end = 9
									while ln < ln_end:
											if sudoku[ln][c] == 0 and num in candidatos_celula[ln][c]:
													candidatos_celula[ln][c].remove(num) 
													bn = int((ln-1)/3) * 3 + int((c-1)/3) + 1
													freq_candidato_bloco[bn][num] -= 1
											ln += 1
							else:
								l,c = [l_end,c_end]
								break 
					elif l1 != 0:
							l2,c2 = [l,c]
							if l2 == l1:
									tipo_adj = 1
							if c2 == c1:
									tipo_adj = 2
					else:
							l1,c1 = [l,c]
				c += 1
			l += 1
		n += 1

def fill_sudoku_cell(b,l,c,num):
	print('chamada fill_sudoku_cell(',b,',',l,',',c,',',num,')')
	global sudoku
	global pendentes
	global passos
	global freq_candidato_bloco
	global linha
	global coluna
	global bloco
	global nao_preenchidos_bloco
	global candidatos_celula
	global preenchidos_linha
	global preenchidos_coluna
	global preenchidos_bloco

	sudoku[l][c] = num
	#print_sudoku(sudoku)
	print('sudoku[',l,'][',c,'] = ',num)
	pendentes -= 1
	if pendentes == 0:
		print('passo ',passos)
		print_sudoku(sudoku)
		final_program = datetime.now()
		print(f"Time program:{final_program-initial_program}")
		exit()
	
	linha[num][l] = 1
	coluna[num][c] = 1
	bloco[num][b] = 1
	nao_preenchidos_bloco[b].remove(num)
	n1 = 0
	n1_end = len(candidatos_celula[l][c])
	while n1 < n1_end:
		num1 = candidatos_celula[l][c][n1]
		freq_candidato_bloco[b][num1] -= 1
		n1 += 1
	freq_candidato_bloco[b][num] = 0
	candidatos_celula[l][c] = []
	preenchidos_linha[l] += 1
	preenchidos_coluna[c] += 1
	preenchidos_bloco[b] += 1

	l1 = int((b-1)/3) * 3  + 1
	l1_end = l1 + 2
	while l1 <= l1_end:
		c1 = ((b-1)%3) * 3 + 1
		c1_end = c1 + 2
		while c1 <= c1_end:
			if sudoku[l1][c1] == 0 and num in candidatos_celula[l1][c1]:
				candidatos_celula[l1][c1].remove(num)
			c1 += 1
		l1 +=1

	c1 = 1
	while c1 <= 9:
		if sudoku[l][c1] == 0 and num in candidatos_celula[l][c1]:
			b1 = int((l-1)/3) * 3 + int((c1-1)/3) + 1
			freq_candidato_bloco[b1][num] -= 1
			candidatos_celula[l][c1].remove(num)			
		c1 += 1

	l1 = 1
	while l1 <= 9:
		if sudoku[l1][c] == 0 and num in candidatos_celula[l1][c]:
			b1 = int((l1-1)/3) * 3 + int((c-1)/3) + 1
			freq_candidato_bloco[b1][num] -= 1
			candidatos_celula[l1][c].remove(num)			
		l1 += 1

	b1 = 1 
	while b1 <= 9:
		if freq_candidato_bloco[b1][num] == 1:
			l1 = int((b1-1)/3) * 3  + 1
			l1_end = l1 + 2
			while l1 <= l1_end:
				c1 = ((b1-1)%3) * 3 + 1
				c1_end = c1 + 2
				while c1 <= c1_end:
					if sudoku[l1][c1] == 0 and num in candidatos_celula[l1][c1]:
						fill_sudoku_cell(b1,l1,c1,num)
						
						c1 = c1_end
						l1 = l1_end							
					c1 += 1
				l1 += 1
		b1 += 1
	'''
	l1 = 7
	l1_end = 9
	while l1 <= l1_end:
		c1 = 1
		c1_end = 3
		while c1 <= c1_end:
			print(candidatos_celula[l1][c1])
			c1 += 1
		l1 += 1
	print(freq_candidato_bloco[5][2])'''

	if preenchidos_linha[l] == 8 or preenchidos_coluna[c] == 8 or preenchidos_bloco[b] == 8:
		check_8filled_group_autofill_9(b,l,c)

	if len(nao_preenchidos_bloco[b]) >= 2:
		verificar_candidatos_eliminar(b)

def check_8filled_group_autofill_9(b,l,c):
	print('chamada check_8filled_group_autofill_9(',b,',',l,',',c,')')
	global sudoku
	global pendentes
	global passos
	global freq_candidato_bloco
	global linha
	global coluna
	global bloco
	global nao_preenchidos_bloco
	global candidatos_celula
	global preenchidos_linha
	global preenchidos_coluna
	global preenchidos_bloco

	while preenchidos_linha[l] == 8 or preenchidos_coluna[c] == 8 or preenchidos_bloco[b] == 8:
		if preenchidos_linha[l] == 8:
			c = 1
			while sudoku[l][c]:
				c += 1
			num = 1
			while linha[num][l]:
				num += 1
			b = int((l-1)/3) * 3 + int((c-1)/3) + 1
		elif preenchidos_coluna[c] == 8:
			l = 1									
			while sudoku[l][c]:
				l += 1
			num = 1
			while coluna[num][c]:
				num += 1
			b = int((l-1)/3) * 3 + int((c-1)/3) + 1
		else:
			l = int((b-1)/3) * 3  + 1
			l_end = l + 2
			while l <= l_end:
				c = ((b-1)%3) * 3 + 1
				c_end = c + 2
				while c <= c_end and sudoku[l][c]:												
					c += 1
				if c > c_end:
					c -= 1
				if sudoku[l][c] == 0:
					break
				l += 1
			num = 1
			while bloco[num][b]:
				num += 1
			
		fill_sudoku_cell(b,l,c,num)
	

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
sudoku = [ \
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

sudoku1 = [ \
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

print_sudoku(sudoku)	

initial_program = datetime.now()
	
#variable declaring
linha = [[]] #relation of presence of each digit on each of the lines from 1 to 9
coluna = [[]] #relation of presence of each digit on each of the columns from 1 to 9
bloco = [[]] #digits already filled on each block
nao_preenchidos_bloco = [[]] #digits left to fill on each block
candidatos_celula = [[]]	#number candidates for each cell
pendentes = 81 #current number of empty cells; at the end, should be zero
passos = 1 #number of steps
freq_candidato_bloco = [[]]
preenchidos_linha = [0,0,0,0,0,0,0,0,0,0]
preenchidos_coluna = [0,0,0,0,0,0,0,0,0,0]
preenchidos_bloco = [0,0,0,0,0,0,0,0,0,0]

#in some variables, we use lists ranging from 0 to 9, so we can index 1 to 9, instead of 0 to 8, which would be confusing
l = 1
while l <= 9:
	linha.append([0,0,0,0,0,0,0,0,0,0])
	coluna.append([0,0,0,0,0,0,0,0,0,0])
	nao_preenchidos_bloco.append([1,2,3,4,5,6,7,8,9])	
	bloco.append([0,0,0,0,0,0,0,0,0,0])	
	freq_candidato_bloco.append([0,9,9,9,9,9,9,9,9,9])
	l += 1

#fill variables with pre-filled cells info
l = 1
while l <= 9:
	c = 1
	while c <= 9:
		if sudoku[l][c] != 0:
			pendentes -= 1
			num = sudoku[l][c]
			linha[num][l] = 1 #print('linha[',num,'][',l,'] = 1')
			coluna[num][c] = 1 #print('coluna[',num,'][',c,'] = 1')
			b = int((l-1)/3) * 3 + int((c-1)/3) + 1
			preenchidos_linha[l] += 1
			preenchidos_coluna[c] += 1
			preenchidos_bloco[b] += 1
			n = 1
			while n <= 9:
				freq_candidato_bloco[b][n] -= 1
				n += 1
			bloco[num][b] = 1 #print('bloco[',num,'][',b,'] = 1')
			nao_preenchidos_bloco[b].remove(num) #print(nao_preenchidos_bloco[b])			
		c += 1
	l += 1	

#now we list possible candidates for each non-filled cell
l = 1
while l <= 9:
	lista = [[]]
	c = 1
	while c <= 9:
		b = int((l-1)/3) * 3 + int((c-1)/3) + 1
		if sudoku[l][c] == 0:
			lista.append(nao_preenchidos_bloco[b].copy())
		else:
			lista.append([])
		c += 1
	candidatos_celula.append(lista)
	l += 1	

#here below, we rule out some cell candidates, based on the presence of that candidate number on same line or same column
while pendentes > 0: 
	b = 1
	while b <= 9:
		l = int((b-1)/3) * 3  + 1
		l_end = l + 2
		while l <= l_end:
			c = ((b-1)%3) * 3 + 1
			c_end = c + 2
			while c <= c_end:
				#print('b: ',b,'l: ',l,'c: ',c)
		
				print('passo ',passos)
				if sudoku[l][c] == 0:
					b = int((l-1)/3) * 3 + int((c-1)/3) + 1
					#print('bloco: ',b,'linha: ',l,'coluna: ',c)					
					len_list = len(candidatos_celula[l][c])
					n = 0
					while n < len_list:		
						num = candidatos_celula[l][c][n]
						if num not in nao_preenchidos_bloco[b] or linha[num][l] == 1 or coluna[num][c] == 1:
							candidatos_celula[l][c].remove(num) #print('candidatos_celula[',l,'][',c,'].remove(',num,')')
							#print(candidatos_celula[l][c])	
							freq_candidato_bloco[b][num] -= 1
							len_list -= 1		
						else:
							n += 1
			  
						#if there's a moment that there's only one candidate for one cell, that's the digit to fill that cell
						if len_list == 1:
							num = candidatos_celula[l][c][0]
							fill_sudoku_cell(b,l,c,num)
							#c,l = {9,0} in my tests resetting lines and columns each time we filled a cell, makes the number of steps to solve pretty higher (almost 3x times than iterating all sudoku cells at a time)
							
							break							
									
				c += 1
				passos += 1
			l += 1	
		n = 0
		n_end = len(nao_preenchidos_bloco[b])
		while n < n_end:
			num = nao_preenchidos_bloco[b][n]
			if freq_candidato_bloco[b][num] == 1:
				l = int((b-1)/3) * 3  + 1
				l_end = l + 2
				while l <= l_end:
					c = ((b-1)%3) * 3 + 1
					c_end = c + 2
					while c <= c_end:
						if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
							fill_sudoku_cell(b,l,c,num)
			 							
							n = n_end
							c = c_end
							l = l_end							
						c += 1
					l += 1
			n += 1
		verificar_candidatos_eliminar(b)
		b += 1
	b = 1 
	while b <= 9:
		n = 0
		n_end = len(nao_preenchidos_bloco[b])
		while n < n_end:
			num = nao_preenchidos_bloco[b][n]
			if freq_candidato_bloco[b][num] == 1:
				l = int((b-1)/3) * 3  + 1
				l_end = l + 2
				while l <= l_end:
					c = ((b-1)%3) * 3 + 1
					c_end = c + 2
					while c <= c_end:
						if sudoku[l][c] == 0 and num in candidatos_celula[l][c]:
							fill_sudoku_cell(b,l,c,num)
			 							
							n = n_end
							c = c_end
							l = l_end							
						c += 1
					l += 1
			n += 1
		b += 1
print('passo ',passos)
print('\n\n')
print_sudoku(sudoku)