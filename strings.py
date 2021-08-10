"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
    Done
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
    Done
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
    Done
### git comment
"""
import pytest

def no_duplicates(a_string):
    res = ''.join(sorted(set(a_string)))
    return res


def reversed_words(a_string):
    words = a_string.split(' ')
    tmp = ' '.join(reversed(words))
    res =tmp.split(' ')
    return res


def four_char_strings(a_string):
     def divide_chunks(l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]
     n=4
     x = list(divide_chunks(a_string, n))
     return x



def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__string__':
    main()
"""   
test_no_duplicates()
test_reversed_words()
test_four_char_strings()

a_string = str(input("Insert a String: "))
print(no_duplicates(a_string))
print(reversed_words(a_string))
print(four_char_strings(a_string))
"""