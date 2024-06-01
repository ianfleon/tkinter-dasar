# Belajar: 1

import tkinter as tk

# Membuat object utama
root = tk.Tk()

# Membuat object Label dan pasangkan ke root
message = tk.Label(root, text="Hello World!")

# Menggabungkan dengan root
message.pack()

# Run
root.mainloop()