"Make variables readable by naming tuples"

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

c = Color(55, 155, 255)
white = Color(255, 255, 255)
print(c.red)
print(white.green)
