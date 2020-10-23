import mysql.connector
try:
    # Open database connection
    conn = mysql.connector.connect(host="192.168.56.102", 	user="eason", passwd="671106", db="demo", charset="utf8")
    cursor = conn.cursor()  # prepare a cursor object 
    sql = "insert into student2 values (%s, %s, %s, %s, %s)"
    data = (29, '張三','2008-12-09',81.5,'機械系')
    cursor.execute(sql, data)  # Execute the SQL command
    conn.commit()
    print("新增成功")
except mysql.connector.Error as e:
    print(str(e))
    print("新增失敗")
except Exception as e:
    print(str(e))
    conn.rollback()
finally:
    if conn is not None:
        conn.close()