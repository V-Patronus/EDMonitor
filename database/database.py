import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="database/edm_cards.db"):
        self.db_name = db_name
        self.ensure_db_dir()
        self.init_db()

    def ensure_db_dir(self):
        """Ensure the directory for the database exists."""
        db_dir = os.path.dirname(self.db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)

    def init_db(self):
        """Initialize the database and create the cards table if it doesn't exist."""
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    icon_path TEXT,
                    style TEXT,
                    path TEXT
                )
            ''')
            conn.commit()
        finally:
            conn.close()

    def add_card(self, name, description, icon_path, style, path):
        """Add a new card to the database."""
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO cards (name, description, icon_path, style, path)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, icon_path, style, path))
            conn.commit()
            last_id = cursor.lastrowid
            return last_id
        finally:
            conn.close()

    def update_card(self, card_id, name, description, icon_path, style, path):
        """Update an existing card."""
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE cards
                SET name = ?, description = ?, icon_path = ?, style = ?, path = ?
                WHERE id = ?
            ''', (name, description, icon_path, style, path, card_id))
            conn.commit()
        finally:
            conn.close()

    def delete_card(self, card_id):
        """Delete a card by ID."""
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM cards WHERE id = ?', (card_id,))
            conn.commit()
        finally:
            conn.close()

    def get_all_cards(self):
        """Retrieve all cards."""
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cards')
            cards = cursor.fetchall()
            return cards
        finally:
            conn.close()
