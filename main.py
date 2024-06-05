'''
Programa que encuentra la raíz cuadrada aproximada de un número determinado utilizando 
el método de bisección. El método de bisección es una técnica para encontrar las raíces
de una función de valor real. Funciona reduciendo un intervalo donde se encuentra la raíz
cuadrada hasta que converge a un valor dentro de una tolerancia especificada.
'''

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
	# Si es menor que 0, no se puede calcular ninguna raiz cuadrada de valor real
	if square_target < 0:
		raise ValueError('Square root of negative number is not defined in real numbers')
	if square_target == 1:
		root = 1
		print(f'The square root of {square_target} is 1')
	elif square_target == 0:
		root = 0
		print(f'The square root of {square_target} is 0')
	else:
		low = 0
		high = max(1, square_target)
		root = None
		for _ in range(max_iterations):
			mid = (low + high) / 2
			square_mid = mid**2
			if (square_mid - square_target) < tolerance:
				root = mid
				break
			elif square_mid < square_target:
				low = mid
			else:
				high = mid
		if root is None:
			print(f"Failed to converge within {max_iterations} iterations.")
		else:   
			print(f'The square root of {square_target} is approximately {root}')
	return root


def main():
	try:
		number = float(input('Ingrese un número: '))
		square_root_bisection(number)
	except:
		print('<<< Entrada no válida >>>')
		main()


# If the program is run (instead of imported), run the main:
if __name__ == '__main__':
	main()

