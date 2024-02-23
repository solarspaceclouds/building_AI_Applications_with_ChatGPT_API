import tkinter as tk
from tkinter import filedialog, messagebox
import openai
import config

# Set your OpenAI API key from a config file or directly
openai.api_key = config.API_KEY

# Initialize file_location to None to check if a file is selected
file_location = None

def translate_text(text, target_language):
    model_engine = "gpt-3.5-turbo"
    response = openai.chat.completions.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": "Translate the following text into " + target_language + ": " + text}
        ]
    )

    translated_text = "".join(response.choices[0].message.content.strip())
    text_field.delete("1.0", tk.END)  # Clear existing text
    text_field.insert(tk.END, translated_text)  # Insert the translated text

def browse_file():
    global file_location
    file_location = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    if file_location:
        messagebox.showinfo("File Selected", "File selected successfully. Now choose a language and click 'Translate'.")

def on_translate():
    global file_location
    target_language = language_var.get().lower()  # Fetch the selected language from the dropdown
    if file_location:
        try:
            with open(file_location, "r", encoding="utf-8") as file:
                text = file.read()
        except Exception as e:
            messagebox.showerror("Error", "Failed to read the file. Please ensure it's a valid .txt file.")
            return
    else:
        text = text_input_field.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("No Text", "Please enter text or select a file before translating.")
            return
    translate_text(text, target_language)

def save_translated_text():
    translated_text = text_field.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showerror("No Translation", "Please translate text before attempting to download.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(translated_text)
        messagebox.showinfo("Success", "The translated text has been saved successfully.")

root = tk.Tk()
root.title("Text Translator")


# GUI Layout
language_var = tk.StringVar(root)
languages = ["Mandarin", "Bulgarian", "Hindi", "Spanish", "French"]
language_var.set(languages[0])  # Default value

tk.Label(root, text="Text Translator").grid(row=0, column=0, columnspan=2)
tk.Button(root, text="Browse File", command=browse_file).grid(row=1, column=0)
tk.OptionMenu(root, language_var, *languages).grid(row=1, column=1)
text_input_field = tk.Text(root, height=10, width=50)  # Renamed to clarify its purpose
text_input_field.grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Translate", command=on_translate).grid(row=3, column=0, columnspan=2)
text_field = tk.Text(root, height=10, width=50)  # For displaying the translated text
text_field.grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Download Translation", command=save_translated_text).grid(row=5, column=0, columnspan=2)

root.mainloop()