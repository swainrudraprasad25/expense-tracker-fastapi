from mysql.connector import connect


def get_connect():
    return connect(
        host="localhost",
        user="root", 
        password="swain@12345", 
        database="expense_db"
    )



