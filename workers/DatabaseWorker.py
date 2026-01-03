import logging
import threading
from PySide6.QtCore import QObject, Signal, Slot
from database.database import DatabaseManager

_logger = logging.getLogger(__name__)

class DatabaseWorker(QObject):
    # Signals to communicate with the main thread
    cards_loaded = Signal(list)
    card_added = Signal(int)
    card_updated = Signal(int)
    card_deleted = Signal(int)
    error_occurred = Signal(str)

    def __init__(self, db_path="database/edm_cards.db"):
        super().__init__()
        self.db_manager = DatabaseManager(db_path)

    @Slot()
    def load_cards(self):
        try:
            _logger.debug("DatabaseWorker.load_cards START (thread=%s)", threading.get_ident())
            cards = self.db_manager.get_all_cards()
            _logger.debug("DatabaseWorker.load_cards fetched %d cards", len(cards))
            self.cards_loaded.emit(cards)
            _logger.debug("DatabaseWorker.load_cards emitted cards_loaded")
        except Exception as e:
            _logger.debug("DatabaseWorker.load_cards ERROR: %s", e)
            self.error_occurred.emit(str(e))

    @Slot(str, str, str, str, str)
    def add_card(self, name, description, icon_path, style, path):
        try:
            new_id = self.db_manager.add_card(name, description, icon_path, style, path)
            self.card_added.emit(new_id)
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(int, str, str, str, str, str)
    def update_card(self, card_id, name, description, icon_path, style, path):
        try:
            self.db_manager.update_card(card_id, name, description, icon_path, style, path)
            self.card_updated.emit(card_id)
        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot(int)
    def delete_card(self, card_id):
        try:
            self.db_manager.delete_card(card_id)
            self.card_deleted.emit(card_id)
        except Exception as e:
            self.error_occurred.emit(str(e))
