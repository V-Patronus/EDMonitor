# db.py
import sqlite3
from typing import List, Tuple, Optional
import logging

DB_FILE = "partes.db"
logging.basicConfig(level=logging.INFO)  # Puedes ajustar el nivel

def get_connection():
    """Devuelve una conexión a la base de datos"""
    try:
        return sqlite3.connect(DB_FILE, timeout=10.0)
    except sqlite3.Error as e:
        logging.error(f"No se pudo conectar a la base de datos: {e}")
        raise

def init_db():
    """Crea la tabla si no existe"""
    try:
        with get_connection() as conn:
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
    except sqlite3.Error as e:
        logging.error(f"Error al inicializar la base de datos: {e}")
        raise

def get_all() -> List[Tuple[str, str, int, int]]:
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT tipo, parte, posicion_i, posicion_j FROM partes ORDER BY parte")
            return cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error al obtener todas las partes: {e}")
        return []

def search(text: str) -> List[Tuple[str, str, int, int]]:
    if not text.strip():
        return get_all()
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT tipo, parte, posicion_i, posicion_j
                FROM partes
                WHERE parte LIKE ?
                ORDER BY parte
            """, (f"%{text}%",))
            return cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error en búsqueda: {e}")
        return []

def add(tipo: str, parte: str, i: int, j: int) -> bool:
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO partes (tipo, parte, posicion_i, posicion_j)
                VALUES (?, ?, ?, ?)
            """, (tipo or "", parte, i, j))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        logging.warning(f"Parte duplicada al añadir: {parte}")
        return False
    except sqlite3.Error as e:
        logging.error(f"Error al añadir parte {parte}: {e}")
        return False

def delete(parte: str) -> bool:
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM partes WHERE parte = ?", (parte,))
            success = cur.rowcount > 0
            conn.commit()
            return success
    except sqlite3.Error as e:
        logging.error(f"Error al eliminar parte {parte}: {e}")
        return False

def update(old_parte: str, new_parte: str, new_tipo: str, new_i: int, new_j: int) -> bool:
    try:
        with get_connection() as conn:
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
    except sqlite3.Error as e:
        logging.error(f"Error al actualizar parte {old_parte} → {new_parte}: {e}")
        return False