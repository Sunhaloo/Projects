import customtkinter as tk

tk.set_appearance_mode("light")

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

# BUTTONS



# define the rows and columns
# column 0
root.columnconfigure(0, weight=1)
# row 0
root.rowconfigure(0, weight=2)
# row 1
root.rowconfigure(1, weight=1)
# row 2
root.rowconfigure(2, weight=5)
# column 1
root.columnconfigure(1, weight=1)

# display widgets
# on row 0 and column 0
appearance.grid(row=0,column=0, sticky="n", pady=10)
# on row 1 and column 0
theme.grid(row=1, column=0)
# on row 2 and column 0
output.grid(row=2, column=0)

root.mainloop()