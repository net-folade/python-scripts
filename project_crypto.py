# create keys string
# autogenerate the values string by offsetting original string
# create two dictionaries
#user input 'the message' and mode
# run encode or decode
# return result
# clean and beautify the code 

#dict_e = encrypt
#dict_d = decrypt

def enigma_light():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    
    
    #print(keys)
    #print(values)
    
    
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    
    '''
# OR create 1 and then flip 
    dict_e = dict(zip(keys,values))
    dict_d = {value:key for key, value in dict_e.items()}
    '''
    
    msg = input('Enter your secret message quietly: ').lower()
    mode = input('Crypto mode: encode (e) OR decrypt as default: ').lower()
    
    
    
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower() ])
        
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower() ])
        
        
        '''
        OR
    
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower() ])
        
    elif mode.lower() == 'd':
        new_msg = ''.join([dict_d[letter] for letter in msg.lower() ])
        
        '''
    
    return new_msg.capitalize()


print(enigma_light())


# IF YOU HAVE A LIST AND WANT TO CREATE A STRING USE THE JOIN FUNCTION WITH EMPTY STRINGS. 



















