import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://Reohex:Reohex@reohexx.07d8r.mongodb.net/?retryWrites=true&w=majority&appName=Reohexx"
)

result = str(client)

if "connect=True" in result:
    try:
        print("CONFIG DB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("CONFIG DB CONNECTION FAILED ❌")
    except:
        pass


COLLECTIONS = client["CONFIG_DATABASE"]
BLACKLISTED_SKS = COLLECTIONS.BLACKLISTED_SKS
TOKEN_DB = COLLECTIONS.TOKEN_DB
SKS_DB = COLLECTIONS.SKS_DB
