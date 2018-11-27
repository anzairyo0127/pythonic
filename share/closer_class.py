numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        else:
            return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
print(sorter.found)
