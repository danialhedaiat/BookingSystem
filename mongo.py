from fastapi import APIRouter
from DB import DB


router = APIRouter()

@router.get("/dbs")
async def list_databases():
    try:
        db = DB()
        dbs = await db.mongo_client.list_database_names()  # Fetch all databases
        return {"databases": dbs}
    except Exception as e:
        return {"status": "❌ Failed to fetch databases!", "error": str(e)}

@router.get("/collections/")
async def list_collections():
    try:
        db = DB()
        dbs = await db.db.list_collection_names()  # Fetch all databases
        return {"databases": dbs}
    except Exception as e:
        return {"status": "❌ Failed to fetch databases!", "error": str(e)}


@router.get("/data/{collection_name}")
async def get_collection_data(collection_name: str):
    db = DB()
    collection = db.db[collection_name]
    cursor = collection.find({},
                             {"_id":0})  # Get all documents
    documents = await cursor.to_list(length=100)  # Convert to a list (limit 100)
    return {"data": documents}