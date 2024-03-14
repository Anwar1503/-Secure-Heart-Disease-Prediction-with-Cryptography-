import tkinter as tk

class UserForm:
    def __init__(self, master):
        self.master = master
        master.title("User Health Form")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.grid(row=1, column=0)

        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=1, column=1)

        self.sex_label = tk.Label(master, text="Sex(male or female) : ")
        self.sex_label.grid(row=2, column=0)

        self.sex_entry = tk.Entry(master)
        self.sex_entry.grid(row=2, column=1)

        self.cp_label = tk.Label(master, text="Chest Pain Type (cp):")
        self.cp_label.grid(row=3, column=0)

        self.cp_entry = tk.Entry(master)
        self.cp_entry.grid(row=3, column=1)

        self.trestbps_label = tk.Label(master, text="Resting Blood Pressure (trestbps):")
        self.trestbps_label.grid(row=4, column=0)

        self.trestbps_entry = tk.Entry(master)
        self.trestbps_entry.grid(row=4, column=1)

        self.chol_label = tk.Label(master, text="Serum Cholesterol (chol):")
        self.chol_label.grid(row=5, column=0)

        self.chol_entry = tk.Entry(master)
        self.chol_entry.grid(row=5, column=1)

        self.fbs_label = tk.Label(master, text="Fasting Blood Sugar (fbs):")
        self.fbs_label.grid(row=6, column=0)

        self.fbs_entry = tk.Entry(master)
        self.fbs_entry.grid(row=6, column=1)

        self.restecg_label = tk.Label(master, text="Resting Electrocardiographic Results (restecg):")
        self.restecg_label.grid(row=7, column=0)

        self.restecg_entry = tk.Entry(master)
        self.restecg_entry.grid(row=7, column=1)

        self.thalach_label = tk.Label(master, text="Maximum Heart Rate Achieved (thalach):")
        self.thalach_label.grid(row=8, column=0)

        self.thalach_entry = tk.Entry(master)
        self.thalach_entry.grid(row=8, column=1)

        self.exang_label = tk.Label(master, text="Exercise Induced Angina (exang):")
        self.exang_label.grid(row=9, column=0)

        self.exang_entry = tk.Entry(master)
        self.exang_entry.grid(row=9, column=1)

        self.oldpeak_label = tk.Label(master, text="ST Depression Induced by Exercise Relative to Rest (oldpeak):")
        self.oldpeak_label.grid(row=10, column=0)

        self.oldpeak_entry = tk.Entry(master)
        self.oldpeak_entry.grid(row=10, column=1)

        self.slope_label = tk.Label(master, text="Slope of the Peak Exercise ST Segment (slope):")
        self.slope_label.grid(row=11, column=0)

        self.slope_entry = tk.Entry(master)
        self.slope_entry.grid(row=11, column=1)

        self.ca_label = tk.Label(master, text="Number of Major Vessels (0-3) Colored by Fluoroscopy (ca):")
        self.ca_label.grid(row=12, column=0)

        self.ca_entry = tk.Entry(master)
        self.ca_entry.grid(row=12, column=1)

        self.thal_label = tk.Label(master, text="Thalassemia:")
        self.thal_label.grid(row=13, column=0)

        self.thal_entry = tk.Entry(master)
        self.thal_entry.grid(row=13, column=1)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=14, column=1)

        self.master = master
        self.message_label = None

        # ... rest of the code ...

    def submit(self):
            user_data = {}
            user_data['Name'] = self.name_entry.get()
            user_data['Age'] = self.age_entry.get()
            user_data['Sex'] = self.sex_entry.get()
            user_data['Chest Pain Type (cp)'] = self.cp_entry.get()
            user_data['Resting Blood Pressure (trestbps)'] = self.trestbps_entry.get()
            user_data['Serum Cholesterol (chol)'] = self.chol_entry.get()
            user_data['Fasting Blood Sugar (fbs)'] = self.fbs_entry.get()
            user_data['Resting Electrocardiographic Results (restecg)'] = self.restecg_entry.get()
            user_data['Maximum Heart Rate Achieved (thalach)'] = self.thalach_entry.get()
            user_data['Exercise Induced Angina (exang)'] = self.exang_entry.get()
            user_data['ST Depression Induced by Exercise Relative to Rest (oldpeak)'] = self.oldpeak_entry.get()
            user_data['Slope of the Peak Exercise ST Segment (slope)'] = self.slope_entry.get()
            user_data['Number of Major Vessels (0-3) Colored by Fluoroscopy (ca)'] = self.ca_entry.get()
            user_data['Thalassemia'] = self.thal_entry.get()

            data_list = []
            for key, value in user_data.items():
                data_list.append(f'{key}: {value}')

            message = '\n'.join(data_list)
            message += '\n\nSuccessfully added user data to list!'
            self.data=list(user_data.values())
            self.dic=dict(user_data.items())
            print(message)

            # Open message GUI
            message_window = tk.Toplevel(self.master)
            message_window.title('Message')

            message_label = tk.Label(message_window, text=f"Hello {user_data['Name']}! You are {user_data['Age']} years old and {user_data['Sex']}.")
            message_label.pack()

            # Add message to the GUI
            if self.message_label:
                self.message_label.destroy()

            self.message_label = tk.Label(self.master, text=message)
            self.message_label.grid(row=15, column=0, columnspan=2)
            

class MessageGUI:
    def __init__(self, master, name, age, sex):
        self.master = master
        self.master.title('Message')
        self.create_widgets(name, age, sex)

    def create_widgets(self, name, age, sex):
        message_label = tk.Label(self.master, text=f"Hello {name}! You are {age} years old and {sex}.")
        message_label.pack()

def get_user_data():
    root = tk.Tk()
    gui = UserForm(root)
    root.mainloop()
    data_list=gui.data
    dic=gui.dic
    message_window = tk.Tk()
    message_gui = MessageGUI(message_window, data_list[0], data_list[1], data_list[2])
    message_window.mainloop()
    return gui.data,gui.dic
data_list,dic=get_user_data()
if(data_list[2]=='male'):
    data_list[2]='1'
elif(data_list[2]=='female'):
    data_list[2]='0'    
main_data=[]
for i in range(1,len(data_list)):
    main_data.append(float(data_list[i]))
name1=data_list[0]
print(main_data)
print(dic)


