import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from Translate import translate
from GetContent import getcontent
from StoreString import store_string
from Readcontent import read
import os


class TranslateGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator Tool")
        self.root.geometry("700x650")

        # ---- Input File ----
        tk.Label(root, text="Select Input File：").pack(anchor="w", padx=10, pady=5)
        file_frame = tk.Frame(root)
        file_frame.pack(fill="x", padx=10)

        self.input_path_var = tk.StringVar()
        tk.Entry(file_frame, textvariable=self.input_path_var, width=60).pack(side="left")
        tk.Button(file_frame, text="Browse", command=self.select_input_file).pack(side="left", padx=5)

        # ---- Original Text ----
        tk.Label(root, text="Original Content：").pack(anchor="w", padx=10, pady=5)
        self.original_text = scrolledtext.ScrolledText(root, height=10)
        self.original_text.pack(fill="both", padx=10)

        # ---- Translated Text ----
        tk.Label(root, text="Translated result：").pack(anchor="w", padx=10, pady=5)
        self.result_text = scrolledtext.ScrolledText(root, height=10)
        self.result_text.pack(fill="both", padx=10)

        # ---- Buttons ----
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Load", command=self.load_content).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="Translate", command=self.translate_text).grid(row=0, column=1, padx=8)
        tk.Button(btn_frame, text="Read", command=self.read_output).grid(row=0, column=2, padx=8)
        tk.Button(btn_frame, text="Save", command=self.save_output).grid(row=0, column=3, padx=8)

    # === GUI functions ===

    def select_input_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if path:
            self.input_path_var.set(path)

    def load_content(self):
        """Load original text into the text box"""
        path = self.input_path_var.get().strip()

        try:
            content = getcontent(path if path else None)
        except Exception as e:
            messagebox.showerror("Error", f"Fail to load file：\n{e}")
            return

        self.original_text.delete(1.0, tk.END)
        self.original_text.insert(tk.END, content)

    def translate_text(self):
        """Translate the original text"""
        content = self.original_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "Content is empty")
            return

        try:
            result = translate(content)
        except Exception as e:
            messagebox.showerror("Error", f"Fail to translate：\n{e}")
            return

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def read_output(self):
        """Read translated text aloud"""
        text = self.result_text.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Empty,can not read！")
            return

        read(text=text)

    def save_output(self):
        """Save translated text directly using os and open(), without store_string()."""

        text = self.result_text.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Empty, cannot save.")
            return

        # Ask user where to save the file
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Translated File As"
        )

        if not path:
            return  # User cancelled saving

        try:
            # Create parent folder if it doesn't exist
            os.makedirs(os.path.dirname(path), exist_ok=True)

            # Save text to file
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")
        else:
            messagebox.showinfo("Success", f"File saved to:\n{path}")


# ====== Run GUI ======
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslateGUI(root)
    root.mainloop()
