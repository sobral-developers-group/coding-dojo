def FizzBuzz(number):
	if number%15 == 0:
		return 'FizzBuzz'
	if number%3 == 0:
		return 'Fizz'
	if number%5 == 0:
		return 'Buzz'
	else:
		return number	

def FizzBuzzAll(interval):
	return [FizzBuzz(x) for x in range(1, interval+1)]

for i in FizzBuzzAll(100):
	print(i)
