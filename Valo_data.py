import pandas as pd
import mysql.connector

# 🔌 Connect to existing DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="val_db"  
)

cursor = conn.cursor()

# 🧱 Create Maps Table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS maps (
    map_id INT AUTO_INCREMENT PRIMARY KEY,
    map_name VARCHAR(50) NOT NULL 
)
""")

print("✅ Map table ready")

df = pd.read_csv("maps.csv")

# 🧹 Clean columns
df.columns = df.columns.str.strip().str.lower()


# 🔁 Insert agents
data = [
    (row['map_name'],)for _, row in df.iterrows()
]

cursor.executemany("""
    INSERT INTO maps (map_name)
    VALUES (%s)
""", data)

conn.commit()

print("✅ Maps inserted successfully")

# 🔒 Close

cursor.close()
conn.close()

