import tkinter as tk
import sqlite3

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tkinter GUI with SQLite Database")
        self.geometry("400x400")

        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS test (value text)""")

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Add to Database", command=self.add_to_database)
        self.button.pack()

    def add_to_database(self):
        value = self.entry.get()
        self.cursor.execute("""INSERT INTO test (value) VALUES (?)""", (value,))
        self.conn.commit()

if __name__ == "__main__":
    app = App()
    app.mainloop()
