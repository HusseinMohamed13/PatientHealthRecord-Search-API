from flask import Flask, redirect, url_for, render_template, session, request
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

@app.route('/', methods=['GET'])
def SearchForm():
    return render_template("searchForm.html")


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        userDetails = request.form
        ID = GetID(userDetails)

        Date = GetDate(userDetails)
        Ac = GetAcident(userDetails)

        Check = CheckInPuts(ID, Date, Ac)

        if Check != "checked":
            return Check

        mydoc = None    
        searchoption = GetSearchOption(userDetails)
        if(searchoption==None):
            return "must choose search option"
        elif (searchoption=="date"):
            mydoc = SearchInDataBaseBYDate(ID, Date)
        elif(searchoption=="accidenttype"):
            mydoc = SearchInDataBaseBYAcident(ID, Ac)

        if mydoc.count() == 0:
            return "user not found"
        else:
            return render_template("card.html", HealthRecords=mydoc, name=mydoc[0]["name"], age=mydoc[0]["age"], address=mydoc[0]["address"], phone=mydoc[0]["Phone"], height=mydoc[0]["height"], weight=mydoc[0]["weight"])

    return render_template("searchForm.html")


def GetID(userDetails):
    Id = userDetails['id']
    if Id == "":
        return None

    return int(Id)

def GetDate(userDetails):
    Date = userDetails['date']
    return str(Date)

def GetSearchOption(userDetails):
    SearchOption = userDetails['searchoption']
    return str(SearchOption)

def GetAcident(userDetails):
    Acident = userDetails['Accident']
    return str(Acident)


def SearchInDataBaseBYDate(ID, Date):
    myquery = {"id": ID, "Date": Date}
    mydoc = mycol.find(myquery)
    return mydoc


def SearchInDataBaseBYAcident(ID, Accident):
    myquery = {"id": ID, "Accident": Accident}
    mydoc = mycol.find(myquery)
    return mydoc


def CheckInPuts(ID, Date, Ac):
    if ID == None:
        return "User Must Enter ID"
    if Date == "" and Ac == "":
        return "You Must Enter Date or Accident"
    return "checked"


if __name__ == '__main__':
    app.run(debug=True)
