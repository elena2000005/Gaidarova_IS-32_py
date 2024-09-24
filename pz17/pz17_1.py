import tkinter as tk
from tkinter import ttk


def submit():
    # Считывание данных из всех полей формы
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END).strip()
    postcode = postcode_entry.get()
    country = country_entry.get()
    card_type_selected = card_type.get()
    card_number = cardnumber_entry.get()
    security_code = security_entry.get()
    name_on_card = nameoncard_entry.get()

    # Вывод всех данных в консоль
    print("=== Submitted Data ===")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    print(f"Post code: {postcode}")
    print(f"Country: {country}")
    print(f"Card type: {card_type_selected}")
    print(f"Card number: {card_number}")
    print(f"Security code: {security_code}")
    print(f"Name on card: {name_on_card}")
    print("=======================")


root = tk.Tk()
root.title("Order Form")
root.geometry("400x530")
root.configure(bg='#d0e79c')

step1_frame = tk.LabelFrame(root, text="Step 1: Your details", bg='#d0e79c', padx=10, pady=10)
step1_frame.pack(fill="x", padx=20, pady=10)

tk.Label(step1_frame, text="Name", bg='#d0e79c').grid(row=0, column=0, sticky='w')
name_entry = tk.Entry(step1_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(step1_frame, text="Email", bg='#d0e79c').grid(row=1, column=0, sticky='w')
email_entry = tk.Entry(step1_frame, width=30)
email_entry.grid(row=1, column=1)

tk.Label(step1_frame, text="Phone", bg='#d0e79c').grid(row=2, column=0, sticky='w')
phone_entry = tk.Entry(step1_frame, width=30)
phone_entry.grid(row=2, column=1)

step2_frame = tk.LabelFrame(root, text="Step 2: Delivery address", bg='#d0e79c', padx=10, pady=10)
step2_frame.pack(fill="x", padx=20, pady=10)

tk.Label(step2_frame, text="Address", bg='#d0e79c').grid(row=0, column=0, sticky='w')
address_text = tk.Text(step2_frame, height=4, width=30)
address_text.grid(row=0, column=1)

tk.Label(step2_frame, text="Post code", bg='#d0e79c').grid(row=1, column=0, sticky='w')
postcode_entry = tk.Entry(step2_frame, width=30)
postcode_entry.grid(row=1, column=1)

tk.Label(step2_frame, text="Country", bg='#d0e79c').grid(row=2, column=0, sticky='w')
country_entry = tk.Entry(step2_frame, width=30)
country_entry.grid(row=2, column=1)

step3_frame = tk.LabelFrame(root, text="Step 3: Card details", bg='#d0e79c', padx=10, pady=10)
step3_frame.pack(fill="x", padx=20, pady=10)

tk.Label(step3_frame, text="Card type", bg='#d0e79c').grid(row=0, column=0, sticky='w')

card_type = tk.StringVar()
visa_radio = tk.Radiobutton(step3_frame, text="VISA", variable=card_type, value="VISA", bg='#d0e79c')
visa_radio.grid(row=0, column=1, sticky='w')

amex_radio = tk.Radiobutton(step3_frame, text="AmEx", variable=card_type, value="AmEx", bg='#d0e79c')
amex_radio.grid(row=0, column=2, sticky='w')

mc_radio = tk.Radiobutton(step3_frame, text="Mastercard", variable=card_type, value="Mastercard", bg='#d0e79c')
mc_radio.grid(row=0, column=3, sticky='w')

tk.Label(step3_frame, text="Card number", bg='#d0e79c').grid(row=1, column=0, sticky='w')
cardnumber_entry = tk.Entry(step3_frame, width=30)
cardnumber_entry.grid(row=1, column=1, columnspan=3)

tk.Label(step3_frame, text="Security code", bg='#d0e79c').grid(row=2, column=0, sticky='w')
security_entry = tk.Entry(step3_frame, width=30)
security_entry.grid(row=2, column=1, columnspan=3)

tk.Label(step3_frame, text="Name on card", bg='#d0e79c').grid(row=3, column=0, sticky='w')
nameoncard_entry = tk.Entry(step3_frame, width=30)
nameoncard_entry.grid(row=3, column=1, columnspan=3)

submit_button = tk.Button(root, text="BUY IT!", command=submit, bg='#3b4b2b', fg='white', width=20)
submit_button.pack(pady=20)

root.mainloop()
