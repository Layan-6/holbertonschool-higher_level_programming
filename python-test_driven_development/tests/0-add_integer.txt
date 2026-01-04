>>> __import__('0-add_integer').add_integer(1, 2)
3
>>> __import__('0-add_integer').add_integer(100, -2)
98
>>> __import__('0-add_integer').add_integer(2)
100
>>> __import__('0-add_integer').add_integer(100.3, -2)
98
>>> __import__('0-add_integer').add_integer(1.5, 2.7)
3
>>> __import__('0-add_integer').add_integer("Hello", 2)
Traceback (most recent call last):
TypeError: a must be an integer
>>> __import__('0-add_integer').add_integer(2, "World")
Traceback (most recent call last):
TypeError: b must be an integer
>>> __import__('0-add_integer').add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer
>>> __import__('0-add_integer').add_integer(1e400, 1)
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer
>>> __import__('0-add_integer').add_integer(float('nan'), 1)
Traceback (most recent call last):
ValueError: cannot convert float NaN to integer
