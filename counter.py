import tkinter as tk

def count_characters():

    text = text_box.get("1.0", tk.END).strip()

    char_count = {}
    for char in text:
        if char != " " and char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Rapport détaillé :\n")
    for char, count in sorted(char_count.items()):
        output_box.insert(tk.END, f"{char} : {count}\n")
    output_box.insert(tk.END, f"\nNombre total de caractères utilisés : {sum(char_count.values())}")


root = tk.Tk()
root.title("Compteur de caractères")


text_box = tk.Text(root, height=10, width=50)
text_box.pack()


count_button = tk.Button(root, text="Compter les caractères", command=count_characters)
count_button.pack()


output_box = tk.Text(root, height=15, width=50)
output_box.pack()


root.mainloop()
  