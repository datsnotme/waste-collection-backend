from db_config import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    print("Connected to:", result[0])

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables:", tables)

    cursor.close()
    conn.close()
except Exception as e:
    print("Database connection failed:")
    print(e)