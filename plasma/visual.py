import tkinter as tk
import plasma.basic

# test python graphic ui tkinter
def init():
	top = tk.Tk()

	canvas = tk.Canvas(top)
	canvas.pack()

	# canvas.create_line(50, 0, 400, 200)
	canvas.create_rectangle(50, 50, 100, 200)

	top.mainloop()

