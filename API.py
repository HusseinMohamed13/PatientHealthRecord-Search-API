from flask import Flask, redirect, url_for, render_template, session, request
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)


cred = credentials.Certificate("gg-ez-4f7b5-firebase-adminsdk-1e3vs-47f421d501.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'HealthRecord')
     


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

        if len(mydoc) == 0:
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
   mydoc = [doc.to_dict() for doc in doc_ref.where(u'id', u'==', ID).where(u"Date", u"==", Date).stream()]
   return mydoc

def SearchInDataBaseBYAcident(ID, Accident):
    mydoc = [doc.to_dict() for doc in doc_ref.where(u'id', u'==', ID).where(u"Accident", u"==", Accident).stream()]
    return mydoc

def CheckInPuts(ID, Date, Ac):
    if ID == None:
        return "User Must Enter ID"
    if Date == "" and Ac == "":
        return "You Must Enter Date or Accident"
    return "checked"


if __name__ == '__main__':
    app.run(debug=True)
