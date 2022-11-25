from cryptography.fernet import Fernet

# Fuction to write the key
'''

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt 
#Password encryption
#Create one function that can create a key and another that can store the key

#***Commented the below section after running once to generate the key

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: # wb== write in bytes
        key_file.write(key)

write_key()
'''


# Fuction to load the key
def load_key():
    file = open('key.key', 'rb') # rb--- read in bytes
    key = file.read()
    file.close()
    return key



key = load_key()  
fer = Fernet(key) # initializing the encryption module


# More Functions
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user,passw = data.split('|')
            print('User:', user, '| Password:', fer.decrypt(passw.encode()).decode()) # str(fer.decrypt(passw.encode))---decrypting when showing the password

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    # use with or open the file then close it to prevent errors
    # with--- closes the file automatically
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # encripting the password when writting
                                                                # instead of using str() decode() has been used to convert the bytes string to a regular string
                                                                # str() introduces quotation marks which result to an error

while True:
    mode = input('Would you like to add a new password or view existing ones (view, add)?, press q to quit! ').lower()

    if mode =='q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue


#### Fernet Cryptography Documentation: https://cryptography.io/en/latest/fernet/
    
