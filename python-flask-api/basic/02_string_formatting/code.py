name = 'Bob'
greeting = f'Hello, {name}'

print(greeting)

name = 'Ash'
greeting = f'Hello, {name}'

print(greeting)


# another way is format

name = 'Gary'
greeting = 'Hi, {}'
with_name = greeting.format(name)

print(with_name)


# formating more than one variable

longer_phrase = 'Hello, {}. Today is {}'
formatted = longer_phrase.format('Leo', 'Monday')
print(formatted)
