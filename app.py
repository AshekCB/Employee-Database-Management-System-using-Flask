from flask import Flask,render_template,request
import mysql_source as sql
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("home.html")


@app.route("/insert",methods=["POST","GET"])
def insert():
    result=None
    if request.method=="POST":
        i=request.form['eid']
        n=request.form['ename']
        a=request.form['age']
        s=request.form['salary']
        sql.insert_record(i,n,a,s)
        result="EMPLOYEE DATA INSERTED SUCCESSFULLY !!"
        return render_template("insert.html",result=result)
    else:
        return render_template("insert.html",result=result)

@app.route("/delete",methods=["POST","GET"])
def delete():
    result=None
    if request.method=="POST":
        eid=request.form['eid']
        sql.delete_record(eid)
        result="EMPLOYEE DATA DELETED SUCCESSFULLY !!"
        return render_template("delete.html",result=result)
    return render_template("delete.html")


@app.route("/update",methods=["POST","GET"])
def update():
    result=None
    if request.method=="POST":
        i=request.form['eid']
        n=request.form['ename']
        a=request.form['age']
        s=request.form['salary']
        sql.update_record(i,n,a,s)
        result="EMPLOYEE DATA UPDATED SUCCESSFULLY !!"
        return render_template("update.html",result=result)
    else:
        return render_template("update.html",result=result)
    

@app.route("/display",methods=["POST","GET"])
def display():
    result=None
    if request.method=="POST":
        result=sql.display_record()
        return render_template("display.html",result=result)
    else:
        return render_template("display.html",result=result)


if __name__=="__main__":
    app.run(debug=True)
