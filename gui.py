import tkinter as tk
from tkinter import ttk

def perform_conversion():
    value_str = entry_value.get()
    specific_conversion = specific_conversion_var.get()

    if not specific_conversion:
        result_label.config(text="Select Specific Conversion")
        return

    if not value_str:
        result_label.config(text="Enter a Value")
        return

    try:
        value = float(value_str)
    except ValueError:
        result_label.config(text="Invalid Input")
        return

    result = perform_specific_conversion(value, specific_conversion)
    result_label.config(text=result)

def perform_specific_conversion(value, specific_conversion):
    if specific_conversion == "Centimeter to Meter":
        return f"{value} cm is equal to {value / 100} m"
    elif specific_conversion == "Meter to Centimeter":
        return f"{value} m is equal to {value * 100} cm"
    elif specific_conversion == "Celsius to Fahrenheit":
        return f"{value} °C is equal to {(value * 9/5) + 32} °F"
    elif specific_conversion == "Fahrenheit to Celsius":
        return f"{value} °F is equal to {(value - 32) * 5/9} °C"
    elif specific_conversion == "Second to Minute":
        return f"{value} s is equal to {value / 60} min"
    elif specific_conversion == "Minute to Second":
        return f"{value} min is equal to {value * 60} s"
    return "Invalid Conversion"

window = tk.Tk()
window.title("Unit Conversion")
window.geometry("600x360")

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

length_frame = ttk.Frame(notebook)
notebook.add(length_frame, text="Length")

temperature_frame = ttk.Frame(notebook)
notebook.add(temperature_frame, text="Temperature")

time_frame = ttk.Frame(notebook)
notebook.add(time_frame, text="Time")

specific_conversion_var = tk.StringVar(window)
specific_conversion_menu = tk.OptionMenu(length_frame, specific_conversion_var, "")
specific_conversion_menu.config(font=("Helvetica", 16), width=20)
specific_conversion_menu.grid(row=2, column=1, padx=10, pady=5)

value_label = tk.Label(length_frame, text="Enter Value", font=("Arial", 14), width=20)
value_label.grid(row=3, column=0, padx=10, pady=5)

entry_value = tk.Entry(length_frame, font=("Arial", 19))
entry_value.grid(row=3, column=1, padx=10, pady=5)

convert_button = tk.Button(length_frame, text="Convert", font=("Arial", 18), command=perform_conversion, bg="blue", fg="white")
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(length_frame, text="", font=("Arial", 18), relief="solid", borderwidth=1, width=20, height=1)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

length_specific_conversions = ["Centimeter to Meter", "Meter to Centimeter"]
specific_conversion_var.set("")  
specific_conversion_menu['menu'].delete(0, 'end')  
for option in length_specific_conversions:
    specific_conversion_menu['menu'].add_command(label=option, command=tk._setit(specific_conversion_var, option))

specific_conversion_label_temp = tk.Label(temperature_frame, text="", font=("Arial", 14))
specific_conversion_label_temp.grid(row=1, column=0, padx=10, pady=5)

specific_conversion_var_temp = tk.StringVar(window)
specific_conversion_menu_temp = tk.OptionMenu(temperature_frame, specific_conversion_var_temp, "")
specific_conversion_menu_temp.config(font=("Helvetica", 16), width=20)
specific_conversion_menu_temp.grid(row=2, column=1, padx=10, pady=5)

value_label_temp = tk.Label(temperature_frame, text="Enter Value", font=("Arial", 14), width=20)
value_label_temp.grid(row=3, column=0, padx=10, pady=5)

entry_value_temp = tk.Entry(temperature_frame, font=("Arial", 19))
entry_value_temp.grid(row=3, column=1, padx=10, pady=5)

convert_button_temp = tk.Button(temperature_frame, text="Convert", font=("Arial", 18), command=perform_conversion, bg="blue", fg="white")
convert_button_temp.grid(row=4, column=0, columnspan=2, pady=10)

result_label_temp = tk.Label(temperature_frame, text="", font=("Arial", 18), relief="solid", borderwidth=1, width=20, height=1)
result_label_temp.grid(row=5, column=0, columnspan=2, pady=10)

temperature_specific_conversions = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
specific_conversion_var_temp.set("")  
specific_conversion_menu_temp['menu'].delete(0, 'end')  
for option in temperature_specific_conversions:
    specific_conversion_menu_temp['menu'].add_command(label=option, command=tk._setit(specific_conversion_var_temp, option))

specific_conversion_label_time = tk.Label(time_frame, text="", font=("Arial", 14))
specific_conversion_label_time.grid(row=1, column=0, padx=10, pady=5)

specific_conversion_var_time = tk.StringVar(window)
specific_conversion_menu_time = tk.OptionMenu(time_frame, specific_conversion_var_time, "")
specific_conversion_menu_time.config(font=("Helvetica", 16), width=20)
specific_conversion_menu_time.grid(row=2, column=1, padx=10, pady=5)

value_label_time = tk.Label(time_frame, text="Enter Value", font=("Arial", 14), width=20)
value_label_time.grid(row=3, column=0, padx=10, pady=5)

entry_value_time = tk.Entry(time_frame, font=("Arial", 19))
entry_value_time.grid(row=3, column=1, padx=10, pady=5)

convert_button_time = tk.Button(time_frame, text="Convert", font=("Arial", 18), command=perform_conversion, bg="blue", fg="white")
convert_button_time.grid(row=4, column=0, columnspan=2, pady=10)

result_label_time = tk.Label(time_frame, text="", font=("Arial", 18), relief="solid", borderwidth=1, width=20, height=1)
result_label_time.grid(row=5, column=0, columnspan=2, pady=10)

time_specific_conversions = ["Second to Minute", "Minute to Second"]
specific_conversion_var_time.set("")  
specific_conversion_menu_time['menu'].delete(0, 'end')  
for option in time_specific_conversions:
    specific_conversion_menu_time['menu'].add_command(label=option, command=tk._setit(specific_conversion_var_time, option))

window.mainloop()
