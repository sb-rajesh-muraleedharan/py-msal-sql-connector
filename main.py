import os
from connect_to_sql import get_sql_connection, get_access_token

from dotenv import load_dotenv

load_dotenv()

def main():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    tenant_id = os.getenv("TENANT_ID")
    server = os.getenv("SQL_SERVER")
    database = os.getenv("SQL_DATABASE")

    authority = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ["https://database.windows.net//.default"]

    access_token = get_access_token(client_id, client_secret, authority, scope)
    conn = get_sql_connection(server, database, access_token)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 name FROM sys.tables")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    main()
