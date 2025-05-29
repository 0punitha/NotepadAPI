from flask import Flask, request, jsonify
import mysql.connector

app= Flask(__name__)

def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="notepad"

    )
# @app.route('/add_user', methods=['POST'])
# def add():
#     #data=request.form.get('sno')
#     sno= request.form.get('sno')
#     name=request.form.get('name')
#     notes = request.form.get('content')
    
#     conn = db_connection()
#     cursor = conn.cursor()
#     sql = "insert into info (sno,name,notes) values (%s, %s, %s)"
#     values = (sno, name, notes)
#     cursor.execute(sql,values)

#     conn.commit()
#     cursor.close()
#     conn.close()
#     return jsonify({"message": "data added"})
@app.route('/add_user', methods=['POST'])
def add_user():
    sno = request.form.get('sno')
    name = request.form.get('name')
    notes = request.form.get('notes')

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO info (sno, name, notes) VALUES (%s, %s, %s)",
        (sno, name, notes)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Data added successfully"})



@app.route('/user_read/<int:num>', methods=['GET'])
# def get_data(num):

#     conn=db_connection()
#     cursor= conn.cursor()


#     cursor.execute('select *from info where sno = %s', (num,))
#     result = cursor.fetchall()


#     cursor.close()
#     conn.close()
#     return jsonify(result)
def get_data(num):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM info WHERE sno = %s', (num,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)



@app.route('/update_user', methods=['POST'])
def update_user():
    sno = request.form.get('sno')
    name = request.form.get('name')
    notes = request.form.get('notes')

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE info set name = %s, notes= %s WHERE sno= %s", 
        (name, notes, sno)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Data added successfully"})

@app.route('/delete_user', methods=['POST'])
def remove():
    sno = request.form.get('sno')
    
    conn= db_connection()
    cursor=conn.cursor()

    cursor.execute('delete from info where sno = %s', (sno,))
    conn.commit()
    
    cursor.close()
    conn.close()

    return jsonify({"message": "User deleted successfully"})
    
if __name__ == '__main__':
     app.run(debug=True)