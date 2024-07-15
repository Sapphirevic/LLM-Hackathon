import tkinter as tk
from tkinter import messagebox, filedialog

class POSSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("POS System")
        self.root.geometry("800x400")  # Set the window size
        self.root.configure(bg="#2C2C2C")  # Dark gray background

        # Title
        self.title_label = tk.Label(root, text="Point of Sale System", bg="#2C2C2C", fg="#FFFFFF", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Create a frame for input and receipt
        self.frame = tk.Frame(root, bg="#2C2C2C")
        self.frame.pack(pady=20)

        # Left side for inputs
        self.input_frame = tk.Frame(self.frame, bg="#2C2C2C")
        self.input_frame.pack(side=tk.LEFT, padx=20)

        # Input fields
        self.create_label_entry(self.input_frame, "Product Name:")
        self.product_entry = self.create_entry(self.input_frame)

        self.create_label_entry(self.input_frame, "Unit Price:")
        self.price_entry = self.create_entry(self.input_frame)

        self.create_label_entry(self.input_frame, "Quantity:")
        self.quantity_entry = self.create_entry(self.input_frame)

        self.create_label_entry(self.input_frame, "City:")
        self.city_entry = self.create_entry(self.input_frame)

        self.create_label_entry(self.input_frame, "Channel:")
        self.channel_entry = self.create_entry(self.input_frame)

        # Payment and Export buttons
        self.pay_button = self.create_button(self.input_frame, "Make Payment", self.make_payment, "green")
        self.export_button = self.create_button(self.input_frame, "Export Receipt", self.export_receipt, "blue")

        # Right side for receipt
        self.receipt_frame = tk.Frame(self.frame, bg="#2C2C2C")
        self.receipt_frame.pack(side=tk.RIGHT, padx=20)

        # Receipt label
        self.receipt_label = tk.Label(self.receipt_frame, text="", bg="#2C2C2C", fg="#FFFFFF", wraplength=300, font=("Arial", 12))
        self.receipt_label.pack(pady=20)

        self.receipt_content = ""

    def create_label_entry(self, parent, label_text):
        label = tk.Label(parent, text=label_text, bg="#2C2C2C", fg="#FFFFFF", font=("Arial", 14))
        label.pack(pady=5)

    def create_entry(self, parent):
        entry = tk.Entry(parent, font=("Arial", 14), width=25)
        entry.pack(pady=5)
        return entry

    def create_button(self, parent, text, command, color):
        button = tk.Button(parent, text=text, command=command, bg=color, fg="white", font=("Arial", 14))
        button.pack(pady=10)
        return button

    def make_payment(self):
        product = self.product_entry.get()
        city = self.city_entry.get()
        channel = self.channel_entry.get()

        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            total = price * quantity

            # Generate receipt
            self.receipt_content = (f"Receipt:\nProduct: {product}\nCity: {city}\nChannel: {channel}\n"
                                    f"Unit Price: ${price:.2f}\nQuantity: {quantity}\nTotal: ${total:.2f}")
            self.receipt_label.config(text=self.receipt_content)

            # Clear entries
            self.product_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.city_entry.delete(0, tk.END)
            self.channel_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid price and quantity.")

    def export_receipt(self):
        if not self.receipt_content:
            messagebox.showwarning("No Receipt", "Please make a payment to generate a receipt.")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.receipt_content)
            messagebox.showinfo("Export Successful", "Receipt exported successfully!")

# Create main application window
root = tk.Tk()
pos_system = POSSystem(root)

# Start the main event loop
root.mainloop()
