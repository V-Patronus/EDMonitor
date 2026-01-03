import logging
from PySide6.QtCore import QObject, Signal, Slot
from database.database import PartesDatabaseManager
import threading

_logger = logging.getLogger(__name__)

class PartesWorker(QObject):
    # Signals
    parts_loaded = Signal(list)
    part_added = Signal(str, str, int, int)
    part_updated = Signal(str, str, str, int, int)
    part_deleted = Signal(str)
    search_results = Signal(list)
    error_occurred = Signal(str)
    
    # Init signal to notify when DB is ready (optional, but good for loading)
    db_ready = Signal()

    def __init__(self, db_path="database/partes.db"):
        super().__init__()
        self.db_path = db_path
        self.db_manager = None # Initialize in slot or safe place if needed, but safe here if just assigned

    @Slot()
    def init_db(self):
        """Initialize database connection."""
        try:
            _logger.debug("PartesWorker.init_db START (thread=%s)", threading.get_ident())
            self.db_manager = PartesDatabaseManager(self.db_path)
            _logger.debug("PartesWorker.init_db DB ready")
            self.db_ready.emit()
            # Note: load_parts will be invoked by connected slots or explicitly
            # Let's wait for explicit call to be safe/granular, but user usually wants immediate load.
        except Exception as e:
            _logger.debug("PartesWorker.init_db ERROR: %s", e)
            self.error_occurred.emit(str(e))

    @Slot()
    def load_parts(self):
        try:
            if not self.db_manager:
                 self.db_manager = PartesDatabaseManager(self.db_path)
            parts = self.db_manager.get_all()
            self.parts_loaded.emit(parts)
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(str, str, int, int)
    def add_part(self, tipo, parte, i, j):
        try:
            if self.db_manager.add(tipo, parte, i, j):
                self.part_added.emit(parte, tipo, i, j)
            else:
                self.error_occurred.emit(f"No se pudo añadir la parte '{parte}'. Posible duplicado.")
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(str, str, str, int, int)
    def update_part(self, old_parte, new_parte, new_tipo, new_i, new_j):
        try:
            if self.db_manager.update(old_parte, new_parte, new_tipo, new_i, new_j):
                self.part_updated.emit(old_parte, new_parte, new_tipo, new_i, new_j)
            else:
                self.error_occurred.emit(f"No se pudo actualizar la parte '{old_parte}'.")
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(str)
    def delete_part(self, parte):
        try:
            if self.db_manager.delete(parte):
                self.part_deleted.emit(parte)
            else:
                self.error_occurred.emit(f"No se pudo eliminar la parte '{parte}'.")
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(str)
    def search_parts(self, text):
        try:
            if not self.db_manager:
                 self.db_manager = PartesDatabaseManager(self.db_path)
            results = self.db_manager.search(text)
            self.search_results.emit(results)
        except Exception as e:
            self.error_occurred.emit(str(e))
