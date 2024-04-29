import tkinter as tk

def create_form():
    # Create the main window
    window = tk.Tk()
    window.title("Form")

    # Create the form fields
    sn_label = tk.Label(window, text="Serial Number")
    sn_label.pack()
    sn_entry = tk.Entry(window)
    sn_entry.pack()

    date_label = tk.Label(window, text="Date")
    date_label.pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    remarks_label = tk.Label(window, text="Remarks")
    remarks_label.pack()
    remarks_entry = tk.Entry(window)
    remarks_entry.pack()

    submit_btn = tk.Button(window, text="Submit", command=submit)
    submit_btn.pack()

    # Start the main event loop
    window.mainloop()

def submit():
    sn = sn_entry.get()
    date = date_entry.get()
    remarks = remarks_entry.get()

    # Process the submitted data (e.g., save to a file, display, etc.)
    print("Serial Number:", sn)
    print("Date:", date)
    print("Remarks:", remarks)

    # Optionally, clear the entry fields for the next submission
    sn_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    remarks_entry.delete(0, tk.END)
