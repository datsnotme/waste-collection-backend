import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_db_connection():
    """
    Creates a MySQL connection to Aiven cloud database.
    Uses SSL CA certificate required by Aiven.
    """

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl_ca=os.getenv("DB_SSL_CA"),   # required for Aiven SSL
            autocommit=True,
            connection_timeout=10
        )

        if conn.is_connected():
            print("✅ Connected to Aiven MySQL")

        return conn

    except Error as e:
        print("❌ Aiven Database Connection Failed")
        print("Error:", e)
        print("Host:", os.getenv("DB_HOST"))
        print("Port:", os.getenv("DB_PORT"))
        print("Database:", os.getenv("DB_NAME"))
        return None