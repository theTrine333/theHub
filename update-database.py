import sqlite3

def update_database():
    # Connect to the database
    conn = sqlite3.connect('theHub.db')
    print("Connection Succeded!!!")

    # Example: Execute a query to update a table

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_database()
