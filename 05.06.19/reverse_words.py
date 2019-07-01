# You need to write a function that reverses the words in a given string.
#  A word can also fit an empty string.
#  If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# reverse('Hello World') == 'World Hello'
# reverse('Hi There.') == 'There. Hi'

# def reverse(st):
#     st = " ".join(st.split(" ")[::-1] )
#     return st

# print(reverse('sit  udwtg sd fkusrosydwwyeuopfrdwakddg otp '))

def reverse(st):
    string = st.split()
    string.reverse()
    st = " ".join(string)
    return st

