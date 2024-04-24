import customtkinter as tk

# FUNCTION quit_app()
def quit_app():
    # command to quit the app
    window.quit()

# FUNCTION dark_mode()
def dark_mode():
    # switch to Dark Theme
    tk.set_appearance_mode("dark")
    result_dark.configure(text="Activated Dark Mode")
    window.after(1000, hide_dark_message)

# FUNCTION light_mode()
def light_mode():
    # switch to Dark Theme
    tk.set_appearance_mode("light")
    result_light.configure(text="Activated Light Mode")
    window.after(1000, hide_light_message)

# FUNCTION hide_dark_message()
def hide_dark_message():
    # hide the message
    result_dark.configure(text="")

# FUNCTION hide_light_message()
def hide_light_message():
    # hide the message
    result_light.configure(text="")

# FUNCTION blue_theme()
def blue_theme():
    # set the theme to blue
    tk.set_default_color_theme("blue")

# FUNCTION green_theme()
def green_theme():
    # set the theme to blue
    tk.set_default_color_theme("green")

# set the default theme to "Light"
tk.set_appearance_mode("Light")

# create the window
window = tk.CTk()
# defined the window size
window.geometry("1280x720")
# give a title
window.title("Random App")

# create widgets for column 0

# create label "settings"
settings = tk.CTkLabel(
    window,
    text="Settings",
    font=(("Helvetica", 20))
)

# create button "button_dark"
button_dark = tk.CTkButton(
    window,
    text="Dark Mode",
    command=dark_mode
)

# create button "button_light"
button_light = tk.CTkButton(
    window,
    text="Light Mode",
    command=light_mode
)

# create button "button_theme_blue"
button_theme_blue = tk.CTkButton(
    window,
    text="Theme: Blue",
    command=blue_theme
)

# create button "button_theme_green"
button_theme_green = tk.CTkButton(
    window,
    text="Theme: Green",
    command=green_theme
)


# create button "button_quit"
button_quit = tk.CTkButton(
    window,
    text="Quit",
    command=quit_app
)

# create label "result"
result = tk.CTkLabel(
    window,
    text="Output",
    font=(("Helvetica", 20))
)

# create label for pressing the dark mode button
result_dark = tk.CTkLabel(
    window,
    text=""
)

# create label for pressing the light mode button
result_light = tk.CTkLabel(
    window,
    text=""
)

# create widgets for column 1

# create label "timer"
timer = tk.CTkLabel(
    window,
    text="Timer",
    font=(("Arial", 20))
)

# create button "start"
start = tk.CTkButton(
    window,
    text="Start Timer",
)

# define the grid
# column 0
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
# column 1
window.columnconfigure(1, weight=1)


# display the widgets
# column 0 row 0
settings.grid(row=0, column=0, sticky="n", pady=10)
button_dark.grid(row=0, column=0, sticky="w", padx=20)
button_light.grid(row=0, column=0, sticky="e", padx=20)
button_theme_blue.grid(row=0, column=0, sticky="sw", padx=20)
button_theme_green.grid(row=0, column=0, sticky="s", padx=20)

# column 0 row 1
result.grid(row=1, column=0, sticky="n", pady=10)
result_dark.grid(row=1, column=0)
result_light.grid(row=1, column=0)
button_quit.grid(row=1, column=0, sticky="s", pady=20)
# column 1
timer.grid(row=0, column=1, sticky="n", pady=10)
start.grid(row=0, column=1,)

window.mainloop()
