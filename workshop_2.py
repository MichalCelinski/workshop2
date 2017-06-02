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
        cursor.execute('INSERT INTO Users(email, username, hashed_password) VALUES (%s, %s, %s);',
                       (self.email, self.username, self.password))
        cursor.close()
        db_connection.commit()
        db_connection.close()
        return 'dodano do bazy'

    @staticmethod
    def load_by_email(email):
        db_connection = connect(user='root', password='admin', host='127.0.0.1', database='workshop_db')
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE email=%s;', (email,))
        for row in cursor:
            data = list(row)
        cursor.close()
        db_connection.close()
        user = User(username=data[2], password=data[3], email=data[1])
        user.id = data[0]
        return user