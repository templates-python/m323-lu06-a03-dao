from todoItem import TodoItem
from todoDao import TodoDao

def main():
    # DAO-Instanz erstellen und Tabelle erstellen
    dao = TodoDao('todo_example.db')
    dao.create_table()

    # Neues ToDo-Element hinzufügen
    new_item = TodoItem(None, 'Buy milk', False)
    dao.add_item(new_item)
    new_item = TodoItem(None, 'Buy cheese', False)
    dao.add_item(new_item)

    # ToDo-Element abrufen
    retrieved_item = dao.get_item(1)
    if retrieved_item:
        print(
            f"Item ID: {retrieved_item.item_id}, Title: {retrieved_item.title}, Is Completed: {retrieved_item.is_completed}")

    # Alle ToDo-Elemente abrufen
    all_items = dao.get_all_items()
    print("All items:")
    for item in all_items:
        print(f"Item ID: {item.item_id}, Title: {item.title}, Is Completed: {item.is_completed}")

    # ToDo-Element aktualisieren
    retrieved_item.is_completed = True
    is_updated = dao.update_item(retrieved_item)
    print(f"Was the item updated? {is_updated}")

    # ToDo-Element löschen
    is_deleted = dao.delete_item(1)
    print(f"Was the item deleted? {is_deleted}")

    # Verbindung schließen
    dao.close()


# Ausführung der Hauptlogik
if __name__ == '__main__':
    main()
