#main_window.py
from tkinter import*
from tkinter import ttk
import jobs_search as js
from popup import Popup as pp
import matplotlib.pyplot as plt
import re

# define a class called HeyThere
class MainPage:

    # define an __init__ method with root as an argument
    def __init__(self,root):

        # add a title to the GUI
        root.title("Search for Jobs")

        #define a left_frame for the widgets
        left_frame = ttk.Frame(root, width=260, padding = "3 3 3 3")
        left_frame.grid( row=0, column=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # defind buttons to get data and update the pie chart
        search_button = ttk.Button(left_frame, text="Get Data", command=self.popup_window)
        search_button.grid(row=0,column=0)
        update_button = ttk.Button(left_frame, text="Update Chart", command=self.update_chart)
        update_button.grid(row=0,column=1)

        # defind text area for the summary
        summary_label = ttk.Label(left_frame, text="Job Search Summary:")
        summary_label.grid(row=3, column=0, pady=(10, 5))

        self.summary_text = ttk.Label(left_frame, text=" ", wraplength=250)
        self.summary_text.grid(row=4, column=0, padx=5, columnspan=2)

        # define the right_frame for displaying the pie char
        right_frame = ttk.Frame(root)
        right_frame.grid(row=0, column=1)
        self.img = PhotoImage(file='companies.png')
        self.image_label = ttk.Label(right_frame, image=self.img)
        self.image_label.image = self.img
        self.image_label.grid(row=1, column=1)



    # call the pop up window
    def popup_window(self):
        pp(root)

    # update the pie char
    def update_chart(self):
        self.draw_char()

    # update the summary
    def update_summary(self, percentages):
        percentages.sort(key=lambda x: x[0].lower())
        summary_info = "Companies:\n"

        for company, percent in percentages:
            summary_info += f"{company}: {percent}%\n"

        # Update the summary text label
        self.summary_text.config(text=summary_info)
    
    # draw the pie chart
    def draw_char(self):
        try:
            with open('linkedin-jobs.csv', 'r') as file:
                next(file)
                lines = file.readlines()

            total_count = 0
            # create dictionary to store the company and appearing times
            comp_dict = {}
            for line in lines:
                company_name = line.split(',')[2].strip()
                company = re.sub(r'^[^a-zA-Z]+','',company_name)
                if company in comp_dict:
                    comp_dict[company] += 1
                else:
                    comp_dict[company] = 1
                total_count += 1
            
            # calculate the percentage
            percentages = {}
            for company, count in comp_dict.items():
                percentage = (count / total_count) * 100
                percentages[company] = round(percentage, 2)
    
            percentages = sorted(percentages.items(), key=lambda x: x[1], reverse=True)

            #plot the pie chart for compmaies
            plt.figure(figsize=(8,8))  
            companies = list(comp_dict.keys())
            size = list(comp_dict.values())
            wedges, texts = plt.pie(size, labels=companies, startangle=90, rotatelabels='true',labeldistance=0.5)

            # reformat the labels
            for text in texts:
                label = text.get_text()
                if len(label) > 30:
                    text.set_text(label[0:30] + '......')

            plt.axis('equal')
            plt.title('Companies', loc='left', pad=30)
            plt.savefig('companies.png')

            self.update_image_label()
            self.update_summary(percentages)
            return percentages
        
        except FileNotFoundError:
            print("Error: CSV file not found.")

    # update image labes
    def update_image_label(self):
        self.img = PhotoImage(file='companies.png')
        self.image_label.config(image=self.img)
        self.image_label.image = self.img


if __name__ == "__main__":
    root = Tk()
    MainPage(root)
    root.mainloop()