a = input("Enter Name: ")
b = input("Enter Date: ")
letter = '''
       Dear <|Name|>,
       you are selected!
       <|Date|>
        '''
print(letter)
letter = letter.replace("<|Name|>",a).replace("<|Date|>",b)
print(letter)