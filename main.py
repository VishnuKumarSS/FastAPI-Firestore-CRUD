from fastapi import FastAPI, Request
from firebase_admin import credentials, firestore, initialize_app

# Initialize FastAPI
app = FastAPI()

# Initialize Firebase Admin SDK
cred = credentials.Certificate("ServiceAccountKeyFirestore.json")
initialize_app(cred)

# Initialize Firestore
db = firestore.client()


# FastAPI Route to Add User Data to Firestore
@app.post("/add_user_data")
async def add_user_data(data: dict):
    users_ref = db.collection("users").document()
    users_ref.set(data)
    print("Document added with ID:", users_ref.id)

    # We can also use the below method to add data
    # users_ref = db.collection("users")
    # users_ref.add(data)
    return {"message": f"UserData added successfully in document id: {users_ref.id}"}


# FastAPI Route to Get Data from Firestore
@app.get("/get_user_data")
async def get_user_data():
    # Example: Get data from a 'users' collection
    users_ref = db.collection("users")
    users = users_ref.stream()
    data = []
    for user in users:
        user_data = user.to_dict()
        user_data["user_document_id"] = user._reference.id
        data.append(user_data)
    return data


@app.get("/get_user_data/{user_id}")
async def get_user_data(request: Request, user_id: str):
    # * Example for getting param
    # {{base_url}}/get_user/qcEBYMn99sXbNllojMpk?param_name=something
    # param_name = request.query_params.get("param_name")
    # print("param_name:", param_name)

    # Example: Get data from a 'users' collection
    user_doc_ref = db.collection("users").document(user_id)
    user = user_doc_ref.get()
    
    # Check if the document exists
    if user.exists:
        # Return the data
        return user.to_dict()
    else:
        # Return an error message if the document doesn't exist
        return {"error": "User Document not found"}


# FastAPI Route to Update Data in Firestore
@app.put("/update_user_data/{user_id}")
async def update_data(user_id: str, data: dict):
    # Example: Update data in a 'users' collection
    user_ref = db.collection("users").document(user_id) # user_id is a document id
    user_ref.update(data)
    return {"message": f"Data updated successfully for document id: {user_id}"}


# FastAPI Route to Delete Data from Firestore
@app.delete("/delete_user_data/{user_id}")
async def delete_data(user_id: str):
    # Example: Delete data from a 'users' collection
    user_ref = db.collection("users").document(user_id)
    user_ref.delete()
    return {"message": f"Data deleted successfully for document id: {user_id}"}
