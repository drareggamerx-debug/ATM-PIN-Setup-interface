import tkinter as tk

root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("400x500")

top_frame = tk.Frame(root, bd=3, relief="raised", bg="lightgray")
top_frame.place(x=20, y=20, width=360, height=120)

label_acc = tk.Label(top_frame, text="Account Number:", bg="lightgray")
label_acc.place(x=10, y=15)

entry_acc = tk.Entry(top_frame)
entry_acc.place(x=140, y=15)

label_pin = tk.Label(top_frame, text="New PIN:", bg="lightgray")
label_pin.place(x=10, y=55)

entry_pin = tk.Entry(top_frame, show="*")
entry_pin.place(x=140, y=55)

keypad_frame = tk.Frame(root, bd=3, relief="sunken")
keypad_frame.place(x=100, y=160)

def press_num(num):
    entry_pin.insert(tk.END, str(num))

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('0', 3, 1)
]

for text, row, col in buttons:
    btn = tk.Button(keypad_frame, text=text, width=5, height=2, 
                    command=lambda val=text: press_num(val))
    btn.grid(row=row, column=col, padx=5, pady=5)

output_text = tk.Text(root, width=42, height=4, bd=2, relief="sunken")
output_text.place(x=20, y=380)

def submit_details():
    acc_no = entry_acc.get()
    pin_no = entry_pin.get()
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"SUCCESS!\nAccount: {acc_no}\nPIN Saved: {pin_no}")

submit_btn = tk.Button(root, text="Submit", bg="green", fg="white", 
                       font=("Arial", 10, "bold"), command=submit_details)
submit_btn.place(x=160, y=340)

root.mainloop()