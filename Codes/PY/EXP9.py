import tkinter as tk
from tkinter import messagebox
def save():
    id=entry_id.get()
    name=entry_name.get()
    gender=gender_var.get()
    skills=", ".join([skill for skill, var in skills_var.items() if var.get()])
    department=listbox_dept.get(tk.ACTIVE)
    if not id or not name or not department:
        messagebox.showerror("Error", "Please fill all Fields")
        return
    with open("employee.txt", "a") as file:
        file.write("{}, {}, {}, {}, {}\n".format(id,name,gender,skills,department))
    messagebox.showinfo("Success", "Employee details saved successfully")
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    gender_var.set("Male")
    for var in skills_var.values():
        var.set(0)
    listbox_dept.selection_clear(0, tk.END)
def load():
    try:
        with open("employee.txt", "r") as file:
            data=file.readlines()
            text_output.delete("1.0", tk.END)
            for line in data:
                text_output.insert(tk.END, line)
    except FileNotFoundError:
        messagebox.showerror("Error", "Data Not Found")

root=tk.Tk()
root.title("Employee Management System")
root.geometry("400x500")

tk.Label(root, text="Employee ID:").pack()
entry_id=tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name:").pack()
entry_name=tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Gender:").pack()
gender_var=tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Skills:").pack()
skills_var={"Python":tk.IntVar(), "Java":tk.IntVar(), "C/C++":tk.IntVar()}
for skill, var in skills_var.items():
    tk.Checkbutton(root, text=skill, variable=var).pack()

tk.Label(root, text="Department:").pack()
listbox_dept=tk.Listbox(root, height=3)
for dept in ["HR", "IT", "Finance"]:
    listbox_dept.insert(tk.END, dept)
listbox_dept.pack()

tk.Button(root, text="Save Details", command=save).pack()
tk.Button(root, text="Load Details", command=load).pack()

tk.Label(root, text="Saved Employees:").pack()
text_output=tk.Text(root, height=5, width=40)
text_output.pack()

root.mainloop()
