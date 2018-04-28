from b2client import B2


def connect(creds):
    conn = B2(creds.account_id, creds.access_key)
    conn.authorize()
    return conn
