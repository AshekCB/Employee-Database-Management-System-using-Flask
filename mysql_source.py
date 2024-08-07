from mysql import connector

db=connector.connect(
    host="localhost",
    user="root",
    password="Abhi17@db",
    database="ashek_web_sql"
)

#print("successfull")

cursor=db.cursor()

def insert_record(id,n,age,sal):
    db=connector.connect(
    host="localhost",
    user="root",
    password="Abhi17@db",
    database="ashek_web_sql")

    cursor=db.cursor()


    query="INSERT INTO emp (eid,ename,age,salary) VALUES (%s,%s,%s,%s)"
    values=(int(id),n,int(age),int(sal))
    
    cursor.execute(query,values)
    db.commit()

    cursor.close()

def delete_record(eid):
    db=connector.connect(
    host="localhost",
    user="root",
    password="Abhi17@db",
    database="ashek_web_sql")

    cursor=db.cursor()


    query="DELETE FROM  emp WHERE eid = (%s)"
    values=(eid,)
    
    cursor.execute(query,values)
    db.commit()

    cursor.close()


def update_record(eid,ename,age,salary) :
    db=connector.connect(
    host="localhost",
    user="root",
    password="Abhi17@db",
    database="ashek_web_sql")

    cursor=db.cursor()


    query="UPDATE  emp SET ename=%s, age=%s, salary=%s WHERE eid=%s"
    values=(ename,age,salary,eid)
    
    cursor.execute(query,values)
    db.commit()

    cursor.close()
   

def display_record():
    db=connector.connect(
    host="localhost",
    user="root",
    password="Abhi17@db",
    database="ashek_web_sql")

    cursor=db.cursor()

    query="SELECT * FROM emp"

    cursor.execute(query)

    res=cursor.fetchall()
    res_=[]
    for i in res :
        res_.append(i)

    return res_   

#print(display_record())    



#insert_record(1,"Ashek",22,35000)
#delete_record(1)

#update_record(56,"Ashek Babu",22,60000)
