import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0:
            raise ValueError("Height must be positive")

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine category
        if bmi < 18.5:
            category = "Good job! You are looking great my Twig!"
        elif 18.5 <= bmi < 23.9:
            category = "Almost a Normal weight...almost"
        elif 24 <= bmi < 26.9:
            category = "OBESE, look at the mirror... disgusting"
        elif 27 <= bmi < 29.9:
            category = "Obese, carefull not to roll off the Treadmill"

        # Popup window
        popup = tk.Toplevel()
        popup.title("BMI Results")
        popup.geometry("300x150")

        result_label = tk.Label(popup, text=f"Your BMI is: {bmi}", font=("Arial", 12, "bold"))
        result_label.pack(pady=10)

        category_label = tk.Label(popup, text=category, font=("Arial", 10))
        category_label.pack(pady=5)

    except ValueError:
        # Handle invalid inputs
        error_popup = tk.Toplevel()
        error_popup.title("somehow you f*cked up...")
        error_popup.geometry("350x100")
        msg = tk.Label(error_popup, text="R U special needs? NUMBERS", fg="red")
        msg.pack(pady=20)

# Main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("550x250")

# Title
title_label = tk.Label(window, text="Enter your details:", font=("Arial", 14, "bold"))
title_label.pack(pady=(10, 5))

# Funny sub-label
sub_label = tk.Label(window, text="(In kilos and meters, burgers and bald eagles per football field if you prefer)", font=("Arial", 9, "italic"), fg="gray")
sub_label.pack()

# Weight entry
weight_label = tk.Label(window, text="Weight :")
weight_label.pack(pady=(15, 2))
weight_entry = tk.Entry(window)
weight_entry.pack()

# Height entry
height_label = tk.Label(window, text="Height :")
height_label.pack(pady=(10, 2))
height_entry = tk.Entry(window)
height_entry.pack()

# Submit button
submit_button = tk.Button(window, text="how fat am i?", command=calculate_bmi)
submit_button.pack(pady=20)

# Keep the window running
window.mainloop()

