import os

import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL setup
db_name = os.getenv("DB_NAME_LOCAL")
db_user = os.getenv("DB_USERNAME_LOCAL")
db_password = os.getenv("DB_PASSWORD_LOCAL")
db_host = os.getenv("DB_HOST_LOCAL", "localhost")
db_port = os.getenv("DB_PORT_LOCAL", 5432)


# connect to PostgreSQL
conn = psycopg2.connect(
    dbname=db_name,
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
)

cursor = conn.cursor(cursor_factory=DictCursor)

query = """SELECT * 
    FROM relays 
    INNER JOIN transactions 
    ON relays.transaction_id = transactions.id
    WHERE transactions.source_chain_id = 23
    ORDER BY transactions.sequence ASC;"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close out
cursor.close()
conn.close()
