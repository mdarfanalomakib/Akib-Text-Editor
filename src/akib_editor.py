import tkinter as tk
from tkinter import filedialog, messagebox

class AkibEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Akib Text Editor")
        
        # Text area
        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=1, fill="both")
        
        # Menu bar
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Akib Files", "*.akib")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".akib", filetypes=[("Akib Files", "*.akib")])
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END).strip()
                with open(file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = AkibEditor(root)
    root.mainloop()
