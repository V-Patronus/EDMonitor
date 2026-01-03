import sqlite3
import os
import logging
from typing import List, Tuple

logging.basicConfig(level=logging.INFO)

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

class PartesDatabaseManager:
    def __init__(self, db_name="database/partes.db"):
        self.db_name = db_name
        self.ensure_db_dir()
        self.init_db()

    def ensure_db_dir(self):
        """Ensure the directory for the database exists."""
        db_dir = os.path.dirname(self.db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)

    def get_connection(self):
        """Devuelve una conexión a la base de datos"""
        try:
            return sqlite3.connect(self.db_name, timeout=10.0)
        except sqlite3.Error as e:
            logging.error(f"No se pudo conectar a la base de datos: {e}")
            raise

    def init_db(self):
        """Crea la tabla si no existe"""
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS partes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT,
                        parte TEXT UNIQUE NOT NULL,
                        posicion_i INTEGER CHECK(posicion_i BETWEEN 1 AND 5),
                        posicion_j INTEGER CHECK(posicion_j BETWEEN 1 AND 6)
                    )
                """)
                conn.commit()
            finally:
                conn.close()
        except sqlite3.Error as e:
            logging.error(f"Error al inicializar la base de datos: {e}")
            raise

    def get_all(self) -> List[Tuple[str, str, int, int]]:
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT tipo, parte, posicion_i, posicion_j FROM partes ORDER BY parte")
                return cur.fetchall()
            finally:
                conn.close()
        except sqlite3.Error as e:
            logging.error(f"Error al obtener todas las partes: {e}")
            return []

    def search(self, text: str) -> List[Tuple[str, str, int, int]]:
        if not text.strip():
            return self.get_all()
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    SELECT tipo, parte, posicion_i, posicion_j
                    FROM partes
                    WHERE parte LIKE ?
                    ORDER BY parte
                """, (f"%{text}%",))
                return cur.fetchall()
            finally:
                conn.close()
        except sqlite3.Error as e:
            logging.error(f"Error en búsqueda: {e}")
            return []

    def add(self, tipo: str, parte: str, i: int, j: int) -> bool:
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO partes (tipo, parte, posicion_i, posicion_j)
                    VALUES (?, ?, ?, ?)
                """, (tipo or "", parte, i, j))
                conn.commit()
                return True
            finally:
                conn.close()
        except sqlite3.IntegrityError:
            logging.warning(f"Parte duplicada al añadir: {parte}")
            return False
        except sqlite3.Error as e:
            logging.error(f"Error al añadir parte {parte}: {e}")
            return False

    def delete(self, parte: str) -> bool:
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM partes WHERE parte = ?", (parte,))
                success = cur.rowcount > 0
                conn.commit()
                return success
            finally:
                conn.close()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar parte {parte}: {e}")
            return False

    def update(self, old_parte: str, new_parte: str, new_tipo: str, new_i: int, new_j: int) -> bool:
        try:
            conn = self.get_connection()
            try:
                cur = conn.cursor()
                
                # Verificar si el nuevo número ya existe (y no es el mismo)
                if old_parte != new_parte:
                    cur.execute("SELECT 1 FROM partes WHERE parte = ?", (new_parte,))
                    if cur.fetchone():
                        logging.warning(f"No se puede actualizar: '{new_parte}' ya existe")
                        return False

                cur.execute("""
                    UPDATE partes
                    SET parte = ?, tipo = ?, posicion_i = ?, posicion_j = ?
                    WHERE parte = ?
                """, (new_parte, new_tipo or "", new_i, new_j, old_parte))
                
                success = cur.rowcount > 0
                conn.commit()
                return success
            finally:
                conn.close()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar parte {old_parte} → {new_parte}: {e}")
            return False
