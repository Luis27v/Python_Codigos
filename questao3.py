def main():
	count = 0
	evens = 0
	odds = 0
	total = 0

	largest = None
	second_largest = None

	while True:
		try:
			n = int(input())
		except EOFError:
			break
		except ValueError:
			print("Entrada inválida. Digite um inteiro.")
			continue


		if n == -1:
			break

		count += 1
		total += n
		if n % 2 == 0:
			evens += 1
		else:
			odds += 1

		# Atualiza maior e segundo maior durante a leitura
		if largest is None:
			largest = n
		elif n > largest:
			second_largest = largest
			largest = n
		elif n != largest:
			if second_largest is None or n > second_largest:
				second_largest = n

	print(f"Quantidade de números digitados: {count}")
	print(f"Quantidade de números pares: {evens}")
	print(f"Quantidade de números ímpares: {odds}")

	if largest is None:
		print("Maior valor: N/A")
	else:
		print(f"Maior valor: {largest}")

	if second_largest is None:
		print("Segundo maior valor: N/A")
	else:
		print(f"Segundo maior valor: {second_largest}")

	print(f"Soma de todos os valores: {total}")


if __name__ == '__main__':
	main()

