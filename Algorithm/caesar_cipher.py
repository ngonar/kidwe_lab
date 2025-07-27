

the_dictionary = {
    'a':'e','b':'f','c':'g','d':'h','e':'i','f':'j',
    'g':'k','h':'l','i':'m','j':'n','k':'o','l':'p',
    'm':'q','n':'r','o':'s','p':'t','q':'u','r':'v',
    's':'w','t':'x','u':'y','v':'z','w':'a','x':'b',
    'y':'c','z':'d'
}

the_plain_string = 'iwan'
the_encrypted_string = ''
for letter in the_plain_string:
    the_encrypted_string += the_dictionary[letter]

print(the_encrypted_string)