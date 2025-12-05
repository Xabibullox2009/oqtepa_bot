import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="oqtepa_lavash",
        user="postgres",
        password="1234",
        host="localhost",
        port=5432
    )


def insert_user(user_id, name, phone_number):
    con = get_connection()
    cur = con.cursor()
    query = """
    INSERT INTO users (id, name, phone_number) VALUES (%s, %s, %s)
    """
    cur.execute(query, (user_id, name, phone_number))
    con.commit()
    cur.close()
    con.close()
    return True 


def get_all_users(user_id):
    con = get_connection()
    cur = con.cursor()

    query = """SELECT * FROM users WHERE id = %s"""
    cur.execute(query, (user_id,))
    users = cur.fetchall()

    cur.close()
    con.close()
    return users