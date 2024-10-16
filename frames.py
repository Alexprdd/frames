import tkinter as tk

window=tk.Tk()
window.title("frames")
window.geometry("800x800")

mainframe=tk.Frame(window,borderwidth=5, relief="groove")
mainframe.pack(fill=tk.BOTH, expand=True)
label1=tk.Label(mainframe, text="JNJSSN", bg="red", fg="blue")
label1.pack()

secondframe=tk.Frame(mainframe,borderwidth=5, relief="ridge")
secondframe.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
label2=tk.Label(secondframe, text="List", bg="red", fg="blue")
label2.pack()

#Creating list widget

fruitlist=tk.Listbox(secondframe)
fruitlist.pack(pady=20)
for item in ["banana","apple","orange","grapes","melon"]:
    fruitlist.insert(tk.END, item)


thirdframe=tk.Frame(mainframe,borderwidth=5, relief="ridge")
thirdframe.pack(side=tk.RIGHT,fill=tk.BOTH, expand=True)
label3=tk.Label(thirdframe, text="sassasas", bg="red", fg="blue")
label3.pack()






window.mainloop()