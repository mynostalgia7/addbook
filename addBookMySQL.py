<<<<<<< HEAD
#파이썬으로 sql사용하기 feat mySQL
import sys
import pymysql
from PyQt5.QtWidgets import QApplication
class mysqlDB():
    def __init__(self)->None:
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()
        super().__init__()
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'sa',
            passwd = '1234',
            db = 'sa',
            charset = 'utf8',
            port = 3306,
            cursorclass = pymysql.cursors.DictCursor)
    def insert(self, new_name, new_phone, new_filename):        
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO addbook (name, phone, filename ) VALUES (%s, %s, %s)"
            result = cursor.execute(sql, (new_name, new_phone, new_filename))
            self.connection.commit()
            return result
    
    def update(self, name_key, new_phone, new_filename):
        with self.connection.cursor() as cursor:
            sql = "UPDATE addbook SET phone = %s, filename = %s WHERE name = %s"
            result = cursor.execute(sql, (new_phone, new_filename, name_key ))
            self.connection.commit()
            return result
    
    def delete(self, name_key):                
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM addbook WHERE name = %s"
            result = cursor.execute(sql, name_key)
            self.connection.commit()
            return result
    
    def getAllData(self):
        print('여기는 전부 읽기')    
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook"
            cursor.execute(sql)
            results = cursor.fetchall()
        return results

    def search(self, any_key):                
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook WHERE name LIKE %s OR phone LIKE %s OR filename LIKE %s"
            key = '%' + any_key + '%'
            cursor.execute(sql, (key, key, key))
            result = cursor.fetchone() 
            # 만약 모든 레코드를 가져와서 확인 하고 싶다면
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)
            # 를 사용해서 핸들링 하세요 

            return result
    def pause(self):
        input("다음 테스트를 진행하려면 Enter를 누르세요...")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = mysqlDB()
    # 추가 테스트    
    result = db.insert("홍길동3","011-1234-6543","D:/hdh2024/myPrj02/res/unknown.png")
    print("Insert test: ", result)   
    db.pause()

    # 수정 테스트
    result = db.update("홍길동3","010-4333-4433","D:/hdh2024/myPrj02/res/22.png")
    print("Update Test : ", result)
    db.pause()

    # 찾기 테스트
    result = db.search("홍")
    print("Search Test : ", result)
    db.pause()

    # 삭제 테스트
    result = db.delete("홍길동3")
    print("Delete Test : ", result)

    exit(app.exec_())

=======
#파이썬으로 sql사용하기 feat mySQL
import sys
import pymysql
from PyQt5.QtWidgets import QApplication
class mysqlDB():
    def __init__(self)->None:
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()
        super().__init__()
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'sa',
            passwd = '1234',
            db = 'sa',
            charset = 'utf8',
            port = 3306,
            cursorclass = pymysql.cursors.DictCursor)
    def insert(self, new_name, new_phone, new_filename):        
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO addbook (name, phone, filename ) VALUES (%s, %s, %s)"
            result = cursor.execute(sql, (new_name, new_phone, new_filename))
            self.connection.commit()
            return result
    
    def update(self, name_key, new_phone, new_filename):
        with self.connection.cursor() as cursor:
            sql = "UPDATE addbook SET phone = %s, filename = %s WHERE name = %s"
            result = cursor.execute(sql, (new_phone, new_filename, name_key ))
            self.connection.commit()
            return result
    
    def delete(self, name_key):                
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM addbook WHERE name = %s"
            result = cursor.execute(sql, name_key)
            self.connection.commit()
            return result
    
    def getAllData(self):
        print('여기는 전부 읽기')    
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook"
            cursor.execute(sql)
            results = cursor.fetchall()
        return results

    def search(self, any_key):                
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook WHERE name LIKE %s OR phone LIKE %s OR filename LIKE %s"
            key = '%' + any_key + '%'
            cursor.execute(sql, (key, key, key))
            result = cursor.fetchone() 
            # 만약 모든 레코드를 가져와서 확인 하고 싶다면
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)
            # 를 사용해서 핸들링 하세요 

            return result
    def pause(self):
        input("다음 테스트를 진행하려면 Enter를 누르세요...")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = mysqlDB()
    # 추가 테스트    
    result = db.insert("홍길동3","011-1234-6543","D:/hdh2024/myPrj02/res/unknown.png")
    print("Insert test: ", result)   
    db.pause()

    # 수정 테스트
    result = db.update("홍길동3","010-4333-4433","D:/hdh2024/myPrj02/res/22.png")
    print("Update Test : ", result)
    db.pause()

    # 찾기 테스트
    result = db.search("홍")
    print("Search Test : ", result)
    db.pause()

    # 삭제 테스트
    result = db.delete("홍길동3")
    print("Delete Test : ", result)

    exit(app.exec_())

>>>>>>> 7b818d0cdbb31e41969f629e09d4ffc94c89458f
