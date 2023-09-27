from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Establish a database connection
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("database.db")
if not db.open():
    print("Error: Couldn't open the database.")
    # Handle the error appropriately

# Get a list of all table names in the database
query = QSqlQuery(db)
query.exec_("SELECT name FROM sqlite_master WHERE type='table'")

table_names = []
while query.next():
    table_name = query.value(0)
    table_names.append(table_name)

# Loop through the table names and print the data in each table
for table_name in table_names:
    print(f"Table: {table_name}")

    # Fetch all data from the current table
    query.exec_(f"SELECT * FROM {table_name}")

    # Print the column names
    column_names = [query.record().fieldName(i) for i in range(query.record().count())]
    print("Columns:", column_names)

    # Print the data rows
    while query.next():
        row_data = [query.value(i) for i in range(query.record().count())]
        print(row_data)

    print("\n")

# Close the database connection
db.close()
