X = {1, 3, 22, 103, 56, 90, 40, 34, 98 }
Y = {2, 6, 67, 89, 34, 3, 90, 198, 28 }
print('X|Y', X|Y )
print('X&Y', X&Y )
print('X\Y', X-Y )
print('(X\Y)|(Y\X)',(X-Y)|(Y|X))
print('(X\Y)∩(Y\X)',(X-Y)&(Y|X))