import pyodbc
import msal

def get_access_token(client_id, client_secret, authority, scope):
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )
    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Could not obtain access token")
    

def get_sql_connection(server, database, access_token):
    token_bytes = bytes(access_token, "utf-8")
    exptoken = b"".join([token_bytes, b"\0"])
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Authentication=ActiveDirectoryAccessToken;"
    )
    conn = pyodbc.connect(conn_str, attrs_before={1256: exptoken})
    return conn    