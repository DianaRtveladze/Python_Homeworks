import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test1234",
    database="it_step"
)

# Create cursor
cursor = conn.cursor()

# Create User table
cursor.execute("CREATE TABLE IF NOT EXISTS User (\n"
               "                    id INT AUTO_INCREMENT PRIMARY KEY,\n"
               "                    username VARCHAR(255) UNIQUE NOT NULL,\n"
               "                    email VARCHAR(255) UNIQUE NOT NULL\n"
               "                )")

# Create Profile table
cursor.execute("""CREATE TABLE IF NOT EXISTS Profile (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    bio TEXT,
                    profile_picture VARCHAR(255),
                    FOREIGN KEY (user_id) REFERENCES User(id)
                )""")

# Add records to User table
user_data = [
    ("user1", "user1@example.com"),
    ("user2", "user2@example.com"),
    ("user3", "user3@example.com"),
    ("user4", "user4@example.com"),
    ("user5", "user5@example.com")
]

cursor.executemany("INSERT INTO User (username, email) VALUES (%s, %s)", user_data)

# Add records to Profile table
profile_data = [
    (1, "Bio of user1", "profile_picture1.jpg"),
    (2, "Bio of user2", "profile_picture2.jpg"),
    (3, "Bio of user3", "profile_picture3.jpg"),
    (4, "Bio of user4", "profile_picture4.jpg"),
    (5, "Bio of user5", "profile_picture5.jpg")
]

cursor.executemany("INSERT INTO Profile (user_id, bio, profile_picture) VALUES (%s, %s, %s)", profile_data)

# Commit changes and close connection
conn.commit()
conn.close()
