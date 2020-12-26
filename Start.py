
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def SearchInDataBaseBYDate(ID, Date):
    myquery = {"id": ID, "Date": Date}
    mydoc = mycol.find(myquery)
    return mydoc


def SearchInDataBaseBYAcident(ID, Accident):
    myquery = {"id": ID, "Accident": Accident}
    mydoc = mycol.find(myquery)
    return mydoc


if __name__ == '__main__':
    app.run(debug=True)
