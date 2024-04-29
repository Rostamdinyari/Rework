from server import run_server
import tkinter as tk
from flask import Flask, render_template, request

def main():
    # Perform main program logic here
    print("Starting the server...")
    run_server()

if __name__ == '__main__':
    main()
    
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

app = Flask(__name__)

@app.route("/Home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sn = request.form.get("sn")
        date = request.form.get("date")
        remarks = request.form.get("remarks")

        # Process the submitted data (e.g., save to a file, display, etc.)
        print("Serial Number:", sn)
        print("Date:", date)
        print("Remarks:", remarks)

        # Optionally, clear the form fields for the next submission
        return render_template("form.html", submitted=True)

    return render_template("form.html", submitted=False)