import customtkinter as tk

tk.set_appearance_mode("light")

# functions for functionality
def quit_app():
    # when button will be pressed it will quit the app
    root.quit()

# functions for theming / appearance
# FUNCTION appearance_dark()
def appearance_dark():
    # sets the window to dark mode
    tk.set_appearance_mode("dark")

# FUNCTION appearance_light()
def appearance_light():
    # sets the window to light mode
    tk.set_appearance_mode("light")

# FUNCTION set_blue_theme()
def set_blue_theme():
    # sets the theme to blue
    tk.set_default_color_theme("blue")

# FUNCTION set_darkblue_theme()
def set_darkblue_theme():
    # sets the theme to darkblue
    tk.set_default_color_theme("darkblue")

# FUNCTION set_green_theme()
def set_green_theme():
    # sets the theme to green
    tk.set_default_color_theme("green")

# functions for hiding labels


# window creation
root = tk.CTk()
root.title("testing")
root.geometry("1280x720")

# create widgets
# LABELS
# column 0, row 0
appearance = tk.CTkLabel(
    root,
    text="Appearance Settings"
)

# column 0, row 1
theme = tk.CTkLabel(
    root,
    text="Theme Settings"
)

# column 0, row 2
output = tk.CTkLabel(
    root,
    text="Output"
)

# BUTTONS for appearance
dark_mode = tk.CTkButton(
    root,
    text="Dark Mode",
    command=appearance_dark
)

light_mode = tk.CTkButton(
    root,
    text="Light Mode",
    command=appearance_light
)

# BUTTONS for theming
theme_blue = tk.CTkButton(
    root,
    text="Blue Theme",
    command=set_blue_theme
)

theme_darkblue = tk.CTkButton(
    root,
    text="Dark Blue Theme",
    command=set_darkblue_theme
)

theme_green = tk.CTkButton(
    root,
    text="Green Theme",
    command=set_green_theme,
)

# define the rows and columns
# column 0
root.columnconfigure(0, weight=1)
# row 0
root.rowconfigure(0, weight=1) 
# row 1
root.rowconfigure(1, weight=1)
# row 2
root.rowconfigure(2, weight=5)
# column 1
root.columnconfigure(1, weight=1)

# display widgets
# on row 0 and column 0
appearance.grid(row=0,column=0, sticky="n", pady=10)
dark_mode.grid(row=0, column=0, sticky="w", padx=20)
light_mode.grid(row=0, column=0, sticky="e", padx=20)
# on row 1 and column 0
theme.grid(row=1, column=0)
theme_green.grid(row=1, column=0, sticky="w", padx=20, pady=20 )
# on row 2 and column 0
output.grid(row=2, column=0)

root.mainloop()