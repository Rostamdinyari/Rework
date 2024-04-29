from server import run_server
import pymongo

# Establish connection with MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Rework"]
collection = db["mainPage"]

def main():
    # Perform main program logic here
    print("Starting the server...")
    run_server()

if __name__ == '__main__':
    main()

@app.route("/Home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sn = request.form.get("sn")
        date = request.form.get("date")
        remarks = request.form.get("remarks")

        # Create a document to insert into MongoDB
        document = {
            "Serial Number": sn,
            "Date": date,
            "Remarks": remarks
        }

        # Insert the document into the MongoDB collection
        collection.insert_one(document)

        # Optionally, clear the form fields for the next submission
        return render_template("form.html", submitted=True)

    return render_template("form.html", submitted=False)
