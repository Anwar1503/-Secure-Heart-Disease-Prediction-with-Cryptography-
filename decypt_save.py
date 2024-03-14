import os

#adding elements for array
def add(arr,k):
    new_arr=[]
    for i in arr:
        new_arr.append(i+k)
    return new_arr 

key=input("eneter a 5 digit key separated by space")
string=key.split()
keys=[int(x) for x in string]
decrypt_keys=add(keys,20)



#code for reversing the list
def reverse(lst):
    return lst[::-1]

#rotate right
def rotate_left(lst,k):
    x=[]
    y=[]
    for i in range(0,len(lst)):
        if(i<k):
            x.append(lst[i])
        elif(i>=k):
            y.append(lst[i])
    return y+x    

def rotate_right(lst,k):
    x=[]
    y=[]
    for i in range(0,len(lst)):
        m=len(lst)-k
        if(i<m):
            x.append(lst[i])
        elif(i>=m):
            y.append(lst[i])
    return y+x

#adding elements for array
def add(arr,k):
    new_arr=[]
    for i in arr:
        new_arr.append(i+k)
    return new_arr    
        
def decrypt(encrypted_str, keys):
    # Convert the encrypted message to a list of integers
    encrypted_int = [ord(c) for c in encrypted_str]
    decrypted_int = []
    for i, c in enumerate(encrypted_int):
        # Use a different key for each character
        key = keys[i % len(keys)]
        # Decrypt the character using the key
        decrypted_int.append(c ^ key)
    # Convert the list of decrypted integers back to a string
    decrypted_str = ''.join([chr(c) for c in decrypted_int])
    return decrypted_str





# Define the name of the input file and output files
input_file = "C:\\Users\\panwarbasha\\projects\\ML_Health_projectAkhilesh.txt"  # Replace with your input file path
name, ext = os.path.splitext(input_file)
output_file = name + "_decrypted" + ext

# Open the input file for reading
with open(input_file, 'r') as f:
    # Read the contents of the file
    content = f.read()
    # Encrypt the contents of the file
    encrypted_content = decrypt(content,decrypt_keys)
    # Write the encrypted contents to a new file
    with open(output_file, 'w') as f_encrypted:
        f_encrypted.write(encrypted_content)



