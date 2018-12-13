import pymongo

def dbmongo():
    mongouser = "user"
    mongopwd = "pwd"
    mongoserver = "server"
    mongoport = "host"
    mongodbname = "dbname"

    uri = 'mongodb://' + mongouser + ':' + mongopwd + '@' + mongoserver + ':' + mongoport + '/' + mongodbname
    client = pymongo.MongoClient(uri)
    db = client.get_database(mongodbname)

    return (client,db)
