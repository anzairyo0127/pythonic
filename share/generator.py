
value = [len(i) for i in open('sample.txt')]
print(value)
it = (len(i) for i in open('sample.txt'))
print(next(it))
print(next(it))

roots = ((i, i**0.5) for i in it)
print(next(roots))
