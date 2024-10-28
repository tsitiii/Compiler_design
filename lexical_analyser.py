#Made By Tsiyon Gashaw Mihretu
# ID: ETS1588/14

TOKEN_TYPES = {
    'KEYWORD': ['int'],
    'IDENTIFIER': [],
    'NUMBER': [],
    'OPERATOR': ['='],
    'SEPARATOR': [';'],
}

def is_identifier(char):
    return char.isalpha() or char == '_'

def is_digit(char):
    return char.isdigit()

def lex(input_string):
    tokens = [] 
    current_token = ''
    
    for char in input_string:
        if char.isspace():
            if current_token:
                tokens.append(classify_token(current_token))
                current_token = ''
            continue
        
        if char in TOKEN_TYPES['OPERATOR'] or char in TOKEN_TYPES['SEPARATOR']:
            if current_token:
                tokens.append(classify_token(current_token)) 
                current_token = ''
            tokens.append(classify_token(char))  
            continue
        current_token += char
    if current_token:
        tokens.append(classify_token(current_token))

    return tokens

def classify_token(token):
    if token in TOKEN_TYPES['KEYWORD']:
        return ('KEYWORD', token)
    elif token in TOKEN_TYPES['OPERATOR']:
        return ('OPERATOR', token)
    elif token in TOKEN_TYPES['SEPARATOR']:
        return ('SEPARATOR', token)
    elif token.isdigit():
        return ('NUMBER', token)
    elif all(is_identifier(ch) or is_digit(ch) for ch in token):
        return ('IDENTIFIER', token)
    else:
        return ('UNKNOWN', token)


input_line = "int age = 23;"
tokens = lex(input_line)

for token in tokens:
    print(token)