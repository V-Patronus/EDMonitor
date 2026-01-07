from PySide6.QtCore import QObject, Signal, Slot
import os
import sqlite3
from datetime import datetime
import json
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        # PyInstaller 6 structure: base is either _MEIPASS or exe dir
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
        
        # 1. Try direct path (root of bundle)
        path = os.path.join(base_path, relative_path)
        if os.path.exists(path):
            return path
            
        # 2. Try _internal folder
        internal_path = os.path.join(base_path, "_internal", relative_path)
        if os.path.exists(internal_path):
            return internal_path
            
        return path
    return os.path.abspath(relative_path)

def persistent_path(relative_path):
    """ Returns a path relative to the application to save settings (User requested) """
    if getattr(sys, 'frozen', False):
        # Bundled mode: Look in _internal folder relative to the .exe
        base_path = os.path.dirname(sys.executable)
        full_path = os.path.join(base_path, "_internal", relative_path)
    else:
        # Development mode: Root of the project
        base_path = os.path.abspath(".")
        full_path = os.path.join(base_path, relative_path)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path

class BackupManager(QObject):
    # Signals to be emitted by main to request actions (connected internally)
    export_cards_requested = Signal(str)
    export_partes_requested = Signal(str)
    export_partes_pdf_requested = Signal(str)
    set_cards_path = Signal(str)
    set_partes_path = Signal(str)

    # Status signals
    progress = Signal(int, str)
    finished = Signal(bool, str)
    paths_loaded = Signal(dict)
    cancel_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # JSON file to persist paths: Use persistent location
        # JSON file to persist paths: Use folder 'database' as requested
        self._json_path = persistent_path(os.path.join('database', 'backup_paths.json'))
        # Ensure directory exists (persistent_path already does this, but for safety)
        self._ensure_db_dir()

        # internal cancel flag for cooperative cancellation
        self._cancel_requested = False

        # Connect backup signals
        self.export_cards_requested.connect(self._export_cards_excel)
        self.export_partes_requested.connect(self._export_partes_excel)
        self.export_partes_pdf_requested.connect(self._export_partes_pdf)
        self.set_cards_path.connect(self._on_set_cards_path)
        self.set_partes_path.connect(self._on_set_partes_path)
        self.cancel_requested.connect(self._on_request_cancel)

    def _on_set_cards_path(self, path: str):
        self._save_json({'cards': path})
        self.progress.emit(0, f"Ruta Cards guardada: {path}")

    def _on_set_partes_path(self, path: str):
        self._save_json({'partes': path})
        self.progress.emit(0, f"Ruta Partes guardada: {path}")

    @Slot()
    def load_paths(self):
        data = self._read_json()
        cards = data.get('cards', '')
        partes = data.get('partes', '')
        self.paths_loaded.emit({'cards': cards, 'partes': partes})

    def _ensure_db_dir(self):
        db_dir = os.path.dirname(self._json_path)
        if db_dir and not os.path.exists(db_dir):
            try:
                os.makedirs(db_dir)
            except Exception:
                pass

    def _read_json(self):
        try:
            if os.path.exists(self._json_path):
                with open(self._json_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def _save_json(self, partial: dict):
        try:
            data = self._read_json()
            data.update(partial)
            with open(self._json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    @Slot()
    def _on_request_cancel(self):
        self._cancel_requested = True
        self.progress.emit(0, 'Cancelación solicitada...')

    # Export implementations run in this QObject's thread (worker thread)
    @Slot(str)
    def _export_cards_excel(self, outpath: str):
        try:
            import pandas as pd
        except Exception:
            self.finished.emit(False, "Falta la librería 'pandas'. Instálala: pip install pandas openpyxl")
            return

        self.progress.emit(5, "Conectando a base de datos cards...")
        # Use resource_path to find the bundled database
        dbpath = resource_path(os.path.join('database', 'edm_cards.db'))
        try:
            # Connect in read-only mode to avoid permission issues if in Program Files
            conn = sqlite3.connect(f"file:{dbpath}?mode=ro", uri=True)
            df = pd.read_sql_query('SELECT * FROM cards', conn)
            conn.close()
        except Exception as e:
            # Fallback if URI mode is not supported or fails
            try:
                conn = sqlite3.connect(dbpath)
                df = pd.read_sql_query('SELECT * FROM cards', conn)
                conn.close()
            except Exception as e2:
                self.finished.emit(False, f"Error leyendo DB cards: {e2} (Direct path: {dbpath})")
                return
        if self._cancel_requested:
            self.finished.emit(False, 'Exportación de Cards cancelada')
            return
        try:
            df.to_excel(outpath, index=False)
        except Exception as e:
            self.finished.emit(False, f"Error exportando Excel de Cards: {e}")
            return

        self.finished.emit(True, f"Excel de Cards exportado: {outpath}")

    @Slot(str)
    def _export_partes_excel(self, outpath: str):
        try:
            import pandas as pd
        except Exception:
            self.finished.emit(False, "Falta la librería 'pandas'. Instálala: pip install pandas openpyxl")
            return

        self.progress.emit(5, "Conectando a base de datos partes...")
        # Use resource_path to find the bundled database
        dbpath = resource_path(os.path.join('database', 'partes.db'))
        try:
            conn = sqlite3.connect(f"file:{dbpath}?mode=ro", uri=True)
            df = pd.read_sql_query('SELECT * FROM partes', conn)
            conn.close()
        except Exception as e:
            try:
                conn = sqlite3.connect(dbpath)
                df = pd.read_sql_query('SELECT * FROM partes', conn)
                conn.close()
            except Exception as e2:
                self.finished.emit(False, f"Error leyendo DB partes: {e2} (Direct path: {dbpath})")
                return
        if self._cancel_requested:
            self.finished.emit(False, 'Exportación de Partes cancelada')
            return
        try:
            df.to_excel(outpath, index=False)
        except Exception as e:
            self.finished.emit(False, f"Error exportando Excel de Partes: {e}")
            return

        self.finished.emit(True, f"Excel de Partes exportado: {outpath}")

    @Slot(str)
    def _export_partes_pdf(self, outpath: str):
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet
        except Exception:
            self.finished.emit(False, "Falta la librería 'reportlab'. Instálala: pip install reportlab")
            return

        dbpath = resource_path(os.path.join('database', 'partes.db'))
        try:
            conn = sqlite3.connect(f"file:{dbpath}?mode=ro", uri=True)
            cur = conn.cursor()
            cur.execute('SELECT parte, tipo, posicion_i, posicion_j FROM partes')
            rows = cur.fetchall()
            conn.close()
        except Exception as e:
            try:
                conn = sqlite3.connect(dbpath)
                cur = conn.cursor()
                cur.execute('SELECT parte, tipo, posicion_i, posicion_j FROM partes')
                rows = cur.fetchall()
                conn.close()
            except Exception as e2:
                self.finished.emit(False, f"Error leyendo DB partes: {e2} (Direct path: {dbpath})")
                return

        # Create a 5x6 grid (posicion_i: 1..5 rows, posicion_j: 1..6 cols)
        rows_count = 5
        cols_count = 6
        grid = [[[] for _ in range(cols_count)] for _ in range(rows_count)]
        for parte, tipo, i_pos, j_pos in rows:
            try:
                i = int(i_pos) - 1
                j = int(j_pos) - 1
                if 0 <= i < rows_count and 0 <= j < cols_count:
                    # store only the parte number (or include tipo if desired)
                    if tipo:
                        entry = f"{parte} ({tipo})"
                    else:
                        entry = f"{parte}"
                    grid[i][j].append(entry)
            except Exception:
                continue

        if self._cancel_requested:
            self.finished.emit(False, 'Generación de PDF cancelada')
            return

        try:
            doc = SimpleDocTemplate(outpath, pagesize=A4)
            story = []
            styles = getSampleStyleSheet()
            title = Paragraph('Tablero de Partes', styles['Heading2'])
            story.append(title)
            story.append(Spacer(1, 12))

            # Build table data: each cell shows header 'Celda (i+1, j+1)' and list of partes
            table_data = []
            for i in range(rows_count):
                row_cells = []
                for j in range(cols_count):
                    cell_parts = grid[i][j]
                    header = f"<b>Celda ({i+1}, {j+1})</b>"
                    if cell_parts:
                        content = header + '<br/>' + '<br/>'.join(map(lambda s: s.replace('&', '&amp;'), cell_parts))
                    else:
                        content = header + '<br/>'
                    p = Paragraph(content, styles['BodyText'])
                    row_cells.append(p)
                table_data.append(row_cells)

            table = Table(table_data, repeatRows=0)
            table_style = TableStyle([
                ('GRID', (0,0), (-1,-1), 0.5, colors.black),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('FONTSIZE', (0,0), (-1,-1), 9),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ])
            table.setStyle(table_style)
            story.append(table)
            doc.build(story)
        except Exception as e:
            self.finished.emit(False, f"Error generando PDF tablero: {e}")
            return

        self.finished.emit(True, f"PDF tablero de Partes generado: {outpath}")
