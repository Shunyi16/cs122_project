#gui.py
from tkinter import*
from tkinter import ttk
import jobs_search as js
import matplotlib.pyplot as plt
import numpy as np

# define a class called HeyThere
class MainPage:

    # define an __init__ method with root as an argument
    def __init__(self,root):

        # add a title to the GUI
        root.title("Job Market Search")

        #define a main frame for the widgets
        mainframe = ttk.Frame(root, padding = "3 3 3 3")
        mainframe.grid( row=0, column=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        label_1 = ttk.Label(mainframe, text="Job Searching")
        label_1.grid(row=1, column=0)

        self.position = StringVar()

        label_2 = ttk.Label(mainframe, text="Position:")
        label_2.grid(row=2, column=0)

        position_entry = ttk.Entry(mainframe, textvariable=self.position)
        position_entry.grid(row=3,column=0)

        search_button = ttk.Button(mainframe, text="Search", command=self.search_action)
        search_button.grid(row=4,column=0)
        more_button = ttk.Button(mainframe, text="More")
        more_button.grid(row=5,column=0)

        # define another frame for displaying the pie char
        frame_1 = ttk.Frame(root)
        frame_1.grid(row=0, column=1)
        self.img = PhotoImage(file='companies.png')
        self.image_label = ttk.Label(frame_1, image=self.img)
        self.image_label.image = self.img
        self.image_label.grid(row=0, column=1)
    

    def search_action(self):
        input_position = self.position.get()
        js.new_search(input_position)
        self.draw_char()
    
    def draw_char(self):
        try:
            with open('linkedin-jobs.csv', 'r') as file:
                next(file)
                lines = file.readlines()

            # create dictionary to store the company and appearing times
            comp_dict = {}
            for line in lines:
                company = line.split(',')[2].strip()
                if company in comp_dict:
                    comp_dict[company] += 1
                else:
                    comp_dict[company] = 1

            #plot the pie char for compmaies
            plt.figure(figsize=(12, 8))  
            companies = list(comp_dict.keys())
            size = list(comp_dict.values())
            plt.pie(size, labels=companies, startangle=90)
            plt.axis('equal')
            plt.savefig('companies.png')
            self.update_image_label()
        except FileNotFoundError:
            print("Error: CSV file not found.")

    def update_image_label(self):
        self.img = PhotoImage(file='companies.png')
        self.image_label.config(image=self.img)
        self.image_label.image = self.img
        
if __name__ == "__main__":
    root = Tk()
    MainPage(root)
    root.mainloop()