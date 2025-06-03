# Função de operador, abrindo arquivo txt para salvar os cálculos nele
with open('mmc.txt', 'a+') as arquivo:
	# Função para escolher a operação matemática
	def operador ():
		print('\n')
		legenda_operadores={'ADIÇÃO':'+','SUBTRAÇÃO':'-','MULTIPLICAÇÃO':'*','DIVISÃO':'/'}
		for i, lista_operadores in enumerate(legenda_operadores):
			print(i, 'Para', lista_operadores, 'use este sinal: ', legenda_operadores[lista_operadores])
		operação=input('Por favor, escolha o tipo de operação que desejas: ')
		if operação == ('+'):
			return (operação)
		elif operação == '-':
			return (operação)
		elif operação == '/':
			return (operação)
		elif operação == '*':
			return (operação)
		else:
			repetição=input('Digite uma operação válida: ')
			if repetição == '+':
				return (repetição)
			elif repetição == '-':
				return (repetição)
			elif repetição == '/':
				return (repetição)
			elif repetição == '*':
				return (repetição)
			else:
				repetição2=input('Digite uma operação válida: +, -, *, /')
				if repetição2 == '+':
					return (repetição2)
				elif repetição2 == '-':
					return (repetição2)
				elif repetição2 == '/':
					return (repetição2)
				elif repetição2 == '*':
					return (repetição2)
				else:
					return('Erro, por favor reinicie a operação')

	# Função da calculadora
	def calculadora():
		calc_1=float(input('Qual o primeiro número do cálculo? '))
		calc_2=float(input('Qual o segundo número do cálculo? '))

		for cálculo in operador():
			if cálculo == "+":
				resultado1=calc_1 + calc_2
				print('\nMMC-SOMA\n')
				print('{} + {} ='.format(calc_1, calc_2), resultado1, '\n', file=arquivo)
				print('{} + {} ='.format(calc_1, calc_2), resultado1, '\n')
			elif cálculo == "-":
				resultado2=calc_1 - calc_2
				print('\nMMC-Subtração\n')
				print('{} - {} ='.format(calc_1, calc_2), resultado2, '\n', file=arquivo)
				print('{} - {} ='.format(calc_1, calc_2), resultado2, '\n')
			elif cálculo == "*":
				resultado3=calc_1 * calc_2
				print('\nMMC-Multiplicação\n')
				print('{} * {} ='.format(calc_1, calc_2), resultado3, '\n', file=arquivo)
				print('{} * {} ='.format(calc_1, calc_2), resultado3, '\n')
			elif cálculo == "/":
				resultado4=calc_1 / calc_2
				print('\nMMC-Divisão\n')
				print('{} / {} ='.format(calc_1, calc_2), resultado4, '\n', file=arquivo)
				print('{} / {} ='.format(calc_1, calc_2), resultado4, '\n')
	calculadora()
