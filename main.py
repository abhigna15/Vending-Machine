import sqlite3
try:
    sqliteConnection = sqlite3.connect('items_final.db')
    sqlite_create_table_query = '''CREATE TABLE vending_machine_final(
                                id INTEGER,
                                coke INTEGER,
                                lays INTEGER,
                                five star INTEGER,
                                snickers INTEGER,
                                biscuits INTEGER,
                                pepsi INTEGER,
                                silk INTEGER,
                                kurkure INTEGER,
                                doritos INTEGER);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")