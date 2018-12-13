import pymongo

def dbmongo():
    mongouser = "test"
    mongopwd = "test"
    mongoserver = "10.0.153.211"
    mongoport = "27017"
    mongodbname = "test"

    uri = 'mongodb://' + mongouser + ':' + mongopwd + '@' + mongoserver + ':' + mongoport + '/' + mongodbname
    client = pymongo.MongoClient(uri)
    db = client.get_database(mongodbname)

    return (client,db)