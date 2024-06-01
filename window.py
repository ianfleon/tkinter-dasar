# Belajar: 2

import tkinter as tk

root = tk.Tk()

# Set nama window
root.title("Tkinter Dasar")

# Set ukuran dan posisi window (Width<x>Height<+>x<+>y)
# root.geometry("600x300+50+50")

# Membuat ukuran dan posisi window sesuai ukuran monitor dan di tengah

# Ukuran window
window_width = 300
window_height = 200

# Get ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Menentukan titik tengah
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set geometry
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Run
root.mainloop()