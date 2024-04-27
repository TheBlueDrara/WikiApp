import pymongo
import os

mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/MyDataBase")
database_name = "MyDataBase"
collection_name = "MyCollection"

try:
    # Create a MongoClient
    client = pymongo.MongoClient(mongodb_uri)

    # Access or create the database
    db = client[database_name]

    # Access or create the collection (table)
    collection = db[collection_name]


    # Insert six sample documents into the collection (values)
    if collection.count_documents({}) == 0:

        sample_data = [
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "tie_name": "Kata Ashi",
            "amount_of_ropes_needed": 5,
            "description": "kata-ashi-zuri (片足吊り) means “one-legged suspension”. on the ground. The kata-ashi-zuri is often used as a precursor to the yokozuri."
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 3,
            "tie_name": "Agura",
            "description": "Leg harness, which in Japanese simply means: sitting cross-legged. It is a very basic, uncomplicated harness in Shibari, and it allows for rope tops on all levels to produce a stable tie structure, as well as practice locks, how to maintain rope tension and how to work with the ropes in order to create a leg harness that is suitable for ground work or for inverted suspension"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 2,
            "tie_name": "Takate kote (Gote)",
            "description": "hands behind back tie"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 2,
            "tie_name": "Maeate",
            "description": "hands infront"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 1,
            "tie_name": "Futomomo",
            "description": "fat leg tie"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 3,
            "tie_name": "ButterFly Harness",
            "description": "Chest Harness"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 1,
            "tie_name": "Oshiri Shibari",
            "description": "waist tie"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 1,
            "tie_name": "Ashiri Shibari",
            "description": "leg tie"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 1,
            "tie_name": "Bunny Ears",
            "description": "Hands Over Head"
            },
            {
            "rope_type": "yuta",
            "length_of_rope": 8,
            "amount_of_ropes_needed": 1,
            "tie_name": "A line",
            "description": "Bamboo Line"
            }
        ]

    # Insert the sample data into the collection
    result = collection.insert_many(sample_data)

    # Output the inserted document IDs (optional)
    print("Inserted document IDs:", result.inserted_ids)

    print("Database, collection, and documents creation completed successfully.")

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")

finally:
    # Close the MongoDB connection (if opened)
    if 'client' in locals():
        client.close()
