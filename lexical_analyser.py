# import re

# TOKEN_TYPES = [
#     ('KEYWORD', r'\bint\b'),      # Keywords
#     ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
#     ('NUMBER', r'\b\d+\b'),       # Numbers
#     ('OPERATOR', r'[=]'),         # Operators
#     ('SEPARATOR', r'[;]'),        # Separators
#     ('WHITESPACE', r'\s+'),       # Whitespace (to ignore)
# ]

# # Combine token types into a single regex
# token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

# def lex(input_string):
#     tokens = []
#     for match in re.finditer(token_regex, input_string):
#         token_type = match.lastgroup
#         token_value = match.group(token_type)
#         if token_type != 'WHITESPACE':  # Ignore whitespace
#             tokens.append((token_type, token_value))
#     return tokens

# input_line = "int age = 23;"
# tokens = lex(input_line)


# for token in tokens:
#     print(token)


# Define token types
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