import pymysql
def Inser(VALUE):
    db = pymysql.connect(host="localhost", user="Simon",password= "*****",port=3306, db='movie')
    cursor = db.cursor()
    sql = "INSERT INTO MTIME(NAME,LINK,POINT,POINT2,YEAR) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,VALUE)
    db.commit()
    db.close()
