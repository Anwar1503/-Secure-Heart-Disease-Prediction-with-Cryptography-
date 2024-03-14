import tkinter as tk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from gui_app import main_data,name1,dic
from functools import reduce
from re import M
import random
import operator
import os


#getting heart data from the user

heart_data = pd.read_csv("C:\\Users\\panwarbasha\\projects\\ML_Health_project\\heart.csv")


#print(heart_data['target'].value_counts())

x=heart_data.drop(columns='target',axis=1)
y=heart_data['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)
#print(x.shape,x_test.shape,x_train.shape)

#training the model

model=LogisticRegression()
model.fit(x_train,y_train)
x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)
#print("training data accuarcy is :",training_data_accuracy)
x_test_prediction=model.predict(x_test)
testing_data_accuracy=accuracy_score(x_test_prediction,y_test)
#print("testing data accuarcy is :",testing_data_accuracy)

#predictiing the performance

lst=main_data

input_data=tuple(lst)
input_data_as_numpy_array=np.asarray(input_data)
#reshaping the numpy array as we are predicting for only one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
if (prediction[0]==1):
    print("***********************************************")
    print("the patient is suffering from heart disease !!!")
    print("***********************************************")
else:
    print("*************************************************")
    print("the patient does not have any heart related issue")
    print('*************************************************')    
k=int(prediction[0])

name=name1
a_name = name.title()
# Create a window
window = tk.Tk()

# Set the window title and dimensions
window.title("Sastra Online heart checkup")
window.geometry("500x400")
window.config(bg="light blue")

# Add the Sastra College logo to the window
logo = tk.PhotoImage(file="C:\\Users\\panwarbasha\\projects\\ML_Health_project\\sastra.png")
logo = logo.subsample(2) 
logo_label = tk.Label(window, image=logo)
logo_label.pack()

# Create a label with the message
message_label = tk.Label(window, text="Welcome to Sastra Online Heart checkup!",font="arial 15 bold")
message_label.pack()

if(k==0):
    message_label = tk.Label(window, text=f"Hey {a_name}! Glad to say,you don't have any heart disease",font="arial 12 bold",bg='green',fg='black')
    message_label.pack()
    message_label = tk.Label(window, text="Keep maintaing your health well like this",font="italics 10 bold",bg='black',fg='White')
    message_label.pack()
    message_label = tk.Label(window, text="Eat green vegetables and fuits to maiantain good health",font="italics 10 bold",bg='black',fg='white')
    message_label.pack()

    logo1 = tk.PhotoImage(file="C:\\Users\\panwarbasha\\projects\\ML_Health_project\\healthy_heart.png")
    logo1 = logo1.subsample(6) 
    logo_label1 = tk.Label(window, image=logo1)
    logo_label1.place(x=20,y=300)
    logo_label1.pack()
elif(k==1):
    message_label = tk.Label(window, text=f"Hey {a_name}!Sorry to say, you have a heart disease!!!",font="arial 12 bold",bg='red',fg='black')
    message_label.pack()
    message_label = tk.Label(window, text="Consult a Doctor as soon as possible",font="=italics 10 bold",bg='black',fg='white')
    message_label.pack()
    message_label = tk.Label(window, text="Ensure you avoid eating oil and spicy foods until you meet a doctor",font="italics 10 bold",bg='black',fg='white')
    message_label.pack()

    logo1 = tk.PhotoImage(file="C:\\Users\\panwarbasha\\projects\\ML_Health_project\\diseased_heart.png")
    logo1 = logo1.subsample(2) 
    logo_label1 = tk.Label(window, image=logo1)
    logo_label1.place(x=20,y=300)
    logo_label1.pack()

message_label = tk.Label(window, text="Note:The result is based on inputs you have given to the system",font="italics 10 bold",bg='yellow',fg='black')
message_label.pack()    
message_label = tk.Label(window, text="     we are not responsible for your wrong inputs to the system",font="italics 10 bold",bg='yellow',fg='black')
message_label.pack()
    
message_label = tk.Label(window, text="for details contact email-sastra@gmail.in and ph_no:xxxxxxxxxxx",font="italics 8 bold",bg='white',fg='black')
message_label.place(x=120,y=380)

# Run the window
window.mainloop()
if(k==1):
    dic['Result']="Positive(+ve)"
elif(k==0):
    dic['Result'] ="Negative(-ve)"  

def save_dict_to_file(dictionary,name):
    """
    Saves the items of a dictionary to a text file with a name specified by the user.

    :param dictionary: the dictionary to be saved
    :type dictionary: dict
    """
    # Get the file name from the user

    file_name = f"C:\\Users\\panwarbasha\\projects\\ML_Health_project{name}.txt"
    
    # Open the file in write mode and write the dictionary to it
    with open(file_name, 'w') as f:
        for key, value in dictionary.items():
            line =str(key) + ': ' + str(value)+ '\n'
            
            f.write(line)

    
    #print(list8)

save_dict_to_file(dic,name1)



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
        



def encrypt(message, keys):
    # Convert the message to a list of integers
    message_int = [ord(c) for c in message]
    encrypted_int = []
    for i, c in enumerate(message_int):
        # Use a different key for each character
        key = keys[i % len(keys)]
        # Encrypt the character using the key
        encrypted_int.append(c ^ key)
    # Convert the list of encrypted integers back to a string
    encrypted_str = ''.join([chr(c) for c in encrypted_int])
    return encrypted_str

key=input("enter a 5 set key separated by space")
string=key.split()
keys=[int(x) for x in string]
encry_key=add(keys,20)

# Define the name of the input file and output files
input_file = f"C:\\Users\\panwarbasha\\projects\\ML_Health_project{name1}.txt"  # Replace with your input file path
name, ext = os.path.splitext(input_file)


# Open the input file for reading
with open(input_file, 'r') as f:
    # Read the contents of the file
    content = f.read()
    
    # Encrypt the contents of the file
    encrypted_content = encrypt(content,encry_key)
    # Write the encrypted contents to a new file
    with open(input_file, 'w') as f_encrypted:
        f_encrypted.write(encrypted_content)

print('Dictionary saved to file:', name)