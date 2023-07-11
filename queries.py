from databaseConnection import db



def create(name,email,password):
    cursor = db.cursor()
    sql = "INSERT INTO your_table (name,email,password) VALUES (%s,%s,%s)"
    values = (name,email,password)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return 'Record created successfully'


def read():
    cursor = db.cursor()
    sql = "SELECT * FROM your_table"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return str(results)


def update():
    cursor = db.cursor()
    sql = "UPDATE your_table SET column1 = %s WHERE column2 = %s"
    values = (request.form['value1'], request.form['value2'])
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return 'Record updated successfully'


def delete():
    cursor = db.cursor()
    sql = "DELETE FROM your_table WHERE column = %s"
    value = (request.form['value'])
    cursor.execute(sql, (value,))
    db.commit()
    cursor.close()
    return 'Record deleted successfully'
