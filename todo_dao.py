"""Datenbankzugriff für die ToDo-Einträge."""

import sqlite3
from todo_item import TodoItem


# TODO: Implementiere die TodoDao-Klasse für CRUD-Operationen
class TodoDao:
    """Liest und schreibt ToDo-Einträge in der SQLite-Datenbank."""
