import tkinter as tk

#defining the colors
 
light_pink = "#FFB6C1"
soft_pink = "#FFDBE9"
cream_pink = "#FFE6EE"

# creating the welcome window 
welcome_window = tk.Tk()
welcome_window.title("To do list")
welcome_window.geometry("700x400") #size of welcome window
welcome_window.configure(bg=cream_pink)

# function for closing the welcome window

def open_task_manager():
    welcome_window.destroy()
    import task_manager
# label constructor from tkinter , creates a text widget
welcome_label = tk.Label(
    welcome_window, #parent window , it tells that where the label will be shown
    text = """    Welcome to To Do List 
    Created by Tayyaba Arshad""",
    bg = cream_pink, #background color of the label
    fg = "black", #forground color (text color),
    font = ("Comic Sans MS", 16, "bold")
)
# .pack() is used to display a widget on the screen without this the widget is created but never visible
welcome_label.pack(padx = 50, pady= (50, 50))

start_button = tk.Button(
    welcome_window,
    text = "Start",
    command= open_task_manager, #run this function when button is clicked
    bg = light_pink,
    fg = "black",
    font = ("Comic Sans MS", 16, "bold")

)

start_button.pack(padx= 50, pady= 50)
# mainloop runs until a user do any action like click button etc
welcome_window.mainloop()










