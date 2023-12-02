import tkinter as tk
from tkinter import*
from tkinter import ttk
import jobs_search as js

class Popup:
    
    def __init__(self,root):
        # defind root
        root = Toplevel()
        root.wm_title('Get Job Position')       
        root.geometry("300x200")

        # defind mainframe
        mainframe = ttk.Frame(root, padding = "3 3 3 7")
        mainframe.grid( row=0, column=0, sticky=(W, E))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        label_1 = ttk.Label(mainframe, text="Job Searching")
        label_1.grid(row=0, column=0, pady=5)

        self.position = StringVar()

        label_2 = ttk.Label(mainframe, text="Position:")
        label_2.grid(row=1, column=0, pady=5)

        self.position_entry = ttk.Entry(mainframe, textvariable=self.position)
        self.position_entry.grid(row=3,column=0, sticky=(W, E), padx=10, pady=10)

        # Display default text in the entry
        self.position_entry.insert(0, "Please enter position here...")
        self.position_entry.bind("<FocusIn>", self.on_entry_click)

        search_button = ttk.Button(mainframe, text="Search", command=lambda: self.search_action(root))
        search_button.grid(row=4,column=0, pady=5)

        self.complete_label = ttk.Label(mainframe, text="")
        self.complete_label.grid(row=5, column=0, pady=5)

        # Center the mainframe within the root window
        mainframe.grid_rowconfigure(3, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        
    def search_action(self, root):
        self.complete_label.config(text="Searching ...")
        input_position = self.position.get()
        js.new_search(input_position)

        self.complete_label.after(1000, lambda: self.complete_label.config(text="Completed Search"))

        root.after(2000, root.destroy)
              
    def on_entry_click(self, event):
        if self.position_entry.get() == "Please enter position here...":
            self.position_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = Tk()
    Popup(root)
    root.mainloop()