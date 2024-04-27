import pymongo
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# MongoDB connection details (replace with your actual values if needed)
mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/MyDataBase")
database_name = "MyDataBase"
collection_name = "MyCollection"
print(os.getenv("MONGODB_URI"))
# Connect to MonשgoDB
client = pymongo.MongoClient(mongodb_uri)
db = client[database_name]
collection = db[collection_name]

# Define Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for flash messaging


#Home page
@app.route("/")
def list_items():
    items = list(collection.find())  # Fetch all documents
    return render_template("list.html", items=items)

#The Chosen Tie
@app.route("/technique/<tie_name>")
def display_technique(tie_name):
  item = collection.find_one({"tie_name": tie_name}) 
  if not item:
    return render_template("error.html", message="Technique not found.")
  return render_template("detail.html", item=item)

#The Fillter Func
@app.route("/filter", methods=["GET"])
def filter_techniques():
    available_rope = request.args.get("available_rope", type=int)
    print(available_rope)
    rope_length = request.args.get("rope_length", type=int)
    print(rope_length)
    filter_rope_type = request.args.get("filter_rope_type", type=str)
    print(filter_rope_type)

    query = {
    "$and": [
        {"amount_of_ropes_needed": {"$lte": available_rope}},
        {"length_of_rope": {"$lte": rope_length}},
        {"rope_type": {"$regex": f".*{filter_rope_type}.*", "$options": "i"}}
    ]
}



    print("Query:", query)
    filtered_items = collection.find(query)
    filtered_items = list(filtered_items)
    print("Filtered Items:", list(filtered_items))
    return render_template("filtered_list.html", items=filtered_items)


#ADD to DB Funcc
@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        tie_name = request.form["tie_name"]
        description = request.form["description"]
        length_of_rope = int(float(request.form["length_of_rope"]))
        rope_type = request.form["rope_type"]
        amount_of_ropes_needed = int(request.form["amount_of_ropes_needed"])

        try:
            collection.insert_one({
                "tie_name": tie_name,
                "description": description,
                "length_of_rope": length_of_rope,
                "rope_type": rope_type,
                "amount_of_ropes_needed": amount_of_ropes_needed
            })
        except pymongo.errors.DuplicateKeyError:
            flash("Error: A technique with that name already exists.", "error")
        except pymongo.errors.PyMongoError as e:
            flash(f"An error occurred: {e}", "error")

        return redirect(url_for("confirmation"))

    return render_template("add.html")

#Just a nice confirmation Func that something was added
@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

#Delete Func
@app.route("/delete_item/<tie_name>", methods=["POST"])
def delete_item(tie_name):
  """Handles deletion requests for items."""

  if not request.method == "POST": 
    return redirect(url_for("list_items"))  

  try:
    collection.delete_one({"tie_name": tie_name})
    flash("Item deleted successfully.", "success")
  except pymongo.errors.PyMongoError as e:
    flash(f"An error occurred: {e}", "error")

  return redirect(url_for("list_items"))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# sadasdasdas