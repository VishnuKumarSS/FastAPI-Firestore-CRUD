# FastAPI-Firestore-CRUD

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Creating a Firestore Database:

1. Begin by creating a Firebase project via the [Firebase console](https://console.firebase.google.com/).
2. Navigate to "All products" and search for "Cloud Firestore."
3. Proceed to create the database and select the nearest location. Opt for starting in "production mode" for enhanced stability and reliability.
4. Our database is now successfully created.

## Generating and Utilizing a Service Account Key from Firestore:

1. Access the project settings and locate the service accounts section.
2. Click on "generate new private key" to generate a service account key.
3. Copy and utilize the provided file path within the project for seamless integration and access to Firestore.

## Run the project
```bash
uvicorn main:app --reload
```
---
# <u>Notes:</u> ⤵️

## <u>Firestore methods</u>
In Firestore using the Python client library, you can utilize various methods to interact with the database. Here are some common methods we can use:

1. **Create a Document:**
```python
data = {"name": "Vishnu", "age": 22}
doc_ref = db.collection("users").document("user1")
doc_ref.set(data)
```

2. **Get all the Documents in a collection:**
```python
# Assuming db is the Firestore client and "users" is the collection name
collection_ref = db.collection("users")
# Get all documents in the collection
docs = collection_ref.stream()

# Iterate through each document
for doc in docs:
    # Access document data as a dictionary
    data = doc.to_dict()
    print(data)
```

3. **Get a Document:**
```python
doc_ref = db.collection("users").document("user1")
doc = doc_ref.get()
if doc.exists:
    print("Document data:", doc.to_dict())
else:
    print("No such document!")
```

4. **Update a Document:**
```python
doc_ref = db.collection("users").document("user1")
doc_ref.update({"age": 35})
```

5. **Delete a Document:**
```python
doc_ref = db.collection("users").document("user1")
doc_ref.delete()
```

6. **Add a Document with Auto-generated ID:**
```python
data = {"name": "Vishnu", "age": 25}
doc_ref = db.collection("users").document()
doc_ref.set(data)
print("Document added with ID:", doc_ref.id)
```
> We can use set() to update the data also
```python
data = {"name": "Vishnu", "age": 25}
doc_ref = db.collection("users").document("some_document_id")
doc_ref.set(data)
print("Document added with ID:", doc_ref.id)
```

7. **Query Documents:**
```python
docs = db.collection("users").where("age", ">=", 30).stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

These are just some basic methods.
Firestore offers more advanced querying and transaction capabilities as well, Refer [Firestore documentation](https://firebase.google.com/docs/firestore).

---
