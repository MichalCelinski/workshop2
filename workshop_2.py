from mysql.connector import connect


class User:
    def __init__(self, username, password, email):
        self.id = None
        self.username = username
        self.password = password
        self.email = email

    def save(self):
        db_connection = connect(user='root', password='admin', host='127.0.0.1', database='workshop_db')
        cursor = db_connection.cursor()
        if self.id:
            cursor.execute('UPDATE Users SET email=%s, username=%s, hashed_password=%s WHERE id=%s',
                           (self.email, self.username, self.password, self.id))
        else:
            cursor.execute('INSERT INTO Users(email, username, hashed_password) VALUES (%s, %s, %s);',
                           (self.email, self.username, self.password))
        cursor.close()
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def load_by_email(email):
        db_connection = connect(user='root', password='admin', host='127.0.0.1', database='workshop_db')
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE email=%s;', (email,))
        data = cursor.fetchone()
        if data is None:
            return None
        cursor.close()
        db_connection.close()
        user = User(username=data[2], password=data[3], email=data[1])
        user.id = data[0]
        return user

    def delete(self):

        if self.id:
            db_connection = connect(user='root', password='admin', host='127.0.0.1', database='workshop_db')
            cursor = db_connection.cursor()
            cursor.execute('DELETE FROM Users WHERE id=%s', (self.id,))
            cursor.close()
            db_connection.commit()
            db_connection.close()
            self.id = None
        else:
            pass

    @staticmethod
    def load_all():
        db_connection = connect(user='root', password='admin', host='127.0.0.1', database='workshop_db')
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM Users')
        all = []
        for row in cursor:
            user = User(row[2], row[3], row[1])
            user.id = row[0]
            all.append(user)
        cursor.close()
        db_connection.close()
        # for i in all:
        #     print(i.username)
        return all