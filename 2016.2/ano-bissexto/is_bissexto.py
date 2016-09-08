def is_bissexto(n):
	return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0) 