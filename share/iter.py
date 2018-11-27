def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        persent = 100 * value / total
        result.append(persent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('my_numbers.txt')
percentages = normalize(visits)
print(percentages)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        persent = 100 * value / total
        result.append(persent)
    return result


percentages = normalize_defensive(visits)
print(percentages)
