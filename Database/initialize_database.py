from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication
from loguru import logger
import os

def initializeDatabase():
    app = QApplication([])

    try:
        if not os.path.exists("../Logs"):
            logger.critical(f"Missing 'Logs' directory")
            os.mkdir("../Logs")
            logger.success("'Logs' directory created successfully")

            logger.add("../Logs/file.log", rotation="1 day")
            logger.success("Logging file created successfully")
    except Exception as e:
        logger.error(f"Error creating 'Logs' directory: {str(e)}")

    try:
        if not os.path.exists("database.db"):
            def create_table(query, table_name, table_definition):
                if not query.exec_(table_definition):
                    error_message = f"Error creating {table_name} table: {query.lastError().text()}"
                    logger.error(error_message)
                    raise Exception(error_message)
                else:
                    logger.success(f"Table '{table_name}' created successfully")

            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            logger.success("Database file created successfully")

            if not db.open():
                logger.error("Error: Unable to open the database")
            else:
                logger.success("Database opened successfully")

            db.transaction()

            query = QSqlQuery()

            try:
                logger.info("Attempting to create tables")

                table_definitions = {
                    "categories": """
                        CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            category_name TEXT,
                            description TEXT,
                            is_deleted INTEGER
                        )
                    """,
                    "lists": """
                        CREATE TABLE IF NOT EXISTS lists (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            list_name TEXT,
                            description TEXT,
                            category_id INTEGER,
                            is_deleted INTEGER
                        )
                    """,
                    "tasks": """
                        CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task_name TEXT,
                            description TEXT,
                            due_date DATE,
                            priority_id INTEGER,
                            status_id INTEGER,
                            creation_date DATE,
                            last_modified_date DATE,
                            list_id INTEGER
                        )
                    """,
                    "priorities": """
                        CREATE TABLE IF NOT EXISTS priorities (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            priority_name TEXT
                        )
                    """,
                    "statuses": """
                        CREATE TABLE IF NOT EXISTS statuses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            status_name TEXT
                        )
                    """
                }

                for table_name, table_definition in table_definitions.items():
                    create_table(query, table_name, table_definition)

                db.commit()
                logger.success("Tables created successfully")

            except Exception as e:
                db.rollback()
                logger.error(f"Error: {str(e)}")

            try:
                logger.info("Attempting to insert into priorities table")

                insert_priorities = {
                    "Low": """
                        INSERT INTO priorities (
                            priority_name
                        )
                        VALUES (
                            "Low"
                        )
                    """,
                    "Medium": """
                        INSERT INTO priorities (
                            priority_name
                        )
                        VALUES (
                            "Medium"
                        )
                    """,
                    "Hard": """
                        INSERT INTO priorities (
                            priority_name
                        )
                        VALUES (
                            "Hard"
                        )
                    """
                }

                for value_to_insert, insert_query in insert_priorities.items():
                    if not query.exec_(insert_query):
                        error_message = f"Error inserting {value_to_insert} in priorities table: {query.lastError().text()}"
                        logger.error(error_message)
                        raise Exception(error_message)
                    else:
                        logger.success(f"Value '{value_to_insert}' inserted to priorities table successfully")

                db.commit()
                logger.success("Values inserted successfully")

            except Exception as e:
                db.rollback()
                logger.error(f"Error: {str(e)}")

            try:
                logger.info("Attempting to insert into statuses table")

                insert_statuses = {
                    "To Do": """
                        INSERT INTO statuses (
                            status_name
                        )
                        VALUES (
                            "To Do"
                        )
                    """,
                    "In Progress": """
                        INSERT INTO statuses (
                            status_name
                        )
                        VALUES (
                            "In Progress"
                        )
                    """,
                    "Completed": """
                        INSERT INTO statuses (
                            status_name
                        )
                        VALUES (
                            "Completed"
                        )
                    """,
                    "Archived": """
                        INSERT INTO statuses (
                            status_name
                        )
                        VALUES (
                            "Archived"
                        )
                    """,
                    "Deleted": """
                        INSERT INTO statuses (
                            status_name
                        )
                        VALUES (
                            "Deleted"
                        )
                    """
                }

                for value_to_insert, insert_query in insert_statuses.items():
                    if not query.exec_(insert_query):
                        error_message = f"Error inserting {value_to_insert} in statuses table: {query.lastError().text()}"
                        logger.error(error_message)
                        raise Exception(error_message)
                    else:
                        logger.success(f"Value '{value_to_insert}' inserted to statuses table successfully")

                db.commit()
                logger.success("Values inserted successfully")

            except Exception as e:
                db.rollback()
                logger.error(f"Error: {str(e)}")

            db.close()
    except Exception as e:
        logger.error(f"Error creating database file: {str(e)}")
        raise

initializeDatabase()