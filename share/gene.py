
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


text = 'Perhaps it’s more indicative of a society that simply doesn\’t allow children to be children anymore'

result = list(index_words_iter(text))

print(result)
