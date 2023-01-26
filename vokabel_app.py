import sqlite3
import tkinter as tk

# Connect to or create the vocabulary database
conn = sqlite3.connect('vocab.db')
cursor = conn.cursor()

# Create the vocabulary table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS vocab
                 (english TEXT, german TEXT)''')

def add_word():
    # Get the English and German words from the input fields
    english = english_entry.get()
    german = german_entry.get()
    
    # Insert the words into the vocabulary table
    cursor.execute('''INSERT INTO vocab (english, german)
                      VALUES (?, ?)''', (english, german))
    conn.commit()
    
    # Clear the input fields
    english_entry.delete(0, 'end')
    german_entry.delete(0, 'end')

def get_word():
    # Get the English word from the input field
    english = english_entry.get()
    
    # Retrieve the corresponding German word from the vocabulary table
    cursor.execute('''SELECT german FROM vocab WHERE english=?''', (english,))
    german = cursor.fetchone()
    
    # Display the German word
    german_label.config(text=german)

# Create the main window
root = tk.Tk()
root.title("Vocabulary App")

# Create the input fields
english_entry = tk.Entry(root)
german_entry = tk.Entry(root)

# Create the labels
english_label = tk.Label(root, text="English:")
german_label = tk.Label(root, text="German:")

# Create the buttons
add_button = tk.Button(root, text="Add", command=add_word)
get_button = tk.Button(root, text="Get", command=get_word)

# Place the widgets on the window
english_label.grid(row=0, column=0)
english_entry.grid(row=0, column=1)
german_label.grid(row=1, column=0)
german_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0)
get_button.grid(row=2, column=1)

# Start the main loop
root.mainloop()

# Close the database connection
cursor.close()
conn.close()
