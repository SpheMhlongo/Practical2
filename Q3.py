#!/usr/bin/python3

def pow(base, exponent):
	answer = base
	for i in range(exponent-1):
		answer *= base
	return answer

def pow2(base, exponent):
	if exponent == 0:
		return 1
	return base * pow2(base, exponent-1)

print(pow(4, 5))
print(pow2(4, 5))