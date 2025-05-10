import sqlite3
import json
from models import Category

# GET ALL CATEGORIES
def get_all_categories():
    #connects to database

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            id,
            label
        FROM Categories
        ORDER BY label
        """
        )

        categories = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row["id"], row["label"])
            categories.append(category.__dict__)

    return categories

# GET SINGLE CATEGORY
def get_single_category(id):

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            label
        FROM Categories
        WHERE id = ?
        """, (id,))

        data = db_cursor.fetchone()

        category = Category(data["id"], data["label"])

    return category.__dict__

# CREATE
def create_category(new_category):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute( """
        INSERT INTO Category
            (label)
        VALUES
            (?);
        """,
            (new_category["label"],))

        id = db_cursor.lastrowid

        new_category["id"] = id

    return new_category

# UPDATE
def update_category(id, new_category):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()


        db_cursor.execute("""
            UPDATE Category
            SET
                label = ?
            WHERE id = ?
            """,
            (new_category["label"], id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
           return False
        else:
            return True

# DELETE
def delete_category(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Category
        WHERE id = ?
        """, (id, ))
