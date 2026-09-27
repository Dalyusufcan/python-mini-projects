import tkinter as tk
from tkinter import messagebox
from bmi_calculator import calculate_bmi, classify_bmi


root = tk.Tk()

window_width = 450
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("BMI Calculator")


frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")


label = tk.Label(frame, text="BMI Calculator")
label.grid(row=0, column=0, columnspan=2, pady=(0, 15))


weight_label = tk.Label(frame, text="Kilo (kg):")
weight_label.grid(row=1, column=0, padx=(0, 10), pady=8)

weight_entry = tk.Entry(frame, width=20)
weight_entry.grid(row=1, column=1, pady=8)


height_label = tk.Label(frame, text="Boy (cm veya m):")
height_label.grid(row=2, column=0, padx=(0, 10), pady=8)

height_entry = tk.Entry(frame, width=20)
height_entry.grid(row=2, column=1, pady=8)


def calculate():
    weight_text = weight_entry.get()
    height_text = height_entry.get()

    if weight_text == "" or height_text == "":
        messagebox.showerror("Hata", "Kilo ve boy alanlarını doldurun.")
        return

    try:
        weight = float(weight_text)
        height = float(height_text)  
    except ValueError:
        messagebox.showerror("Hata", "Kilo ve boy sayısal değer olmalıdır.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Hata", "Kilo ve boy sıfırdan büyük olmalıdır.")
        return

    if height > 3:
        height_m = height / 100
    else:
        height_m = height

    bmi = calculate_bmi(weight, height_m)
    category = classify_bmi(bmi)

    result_label.config(text=f"BMI: {bmi:.2f} - {category}")

result_label = tk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=(15, 0))



calculate_button = tk.Button(frame, text="Hesapla", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=(15, 0))


root.mainloop()