from todoItem import TodoItem
from todoDao import TodoDao


def test_add_item():
    dao = TodoDao('test_todo.db')
    dao.create_table()
    new_item = TodoItem(None, 'Test item', False)
    dao.add_item(new_item)
    retrieved_item = dao.get_item(1)
    assert retrieved_item is not None
    assert retrieved_item.title == 'Test item'
    assert retrieved_item.is_completed == False
    dao.close()


def test_get_item():
    dao = TodoDao('test_todo.db')
    retrieved_item = dao.get_item(1)
    assert retrieved_item is not None
    assert retrieved_item.title == 'Test item'
    dao.close()


def test_get_all_items():
    dao = TodoDao('test_todo.db')
    all_items = dao.get_all_items()
    assert len(all_items) == 1
    dao.close()


def test_update_item():
    dao = TodoDao('test_todo.db')
    item_to_update = dao.get_item(1)
    item_to_update.title = 'Updated item'
    update_status = dao.update_item(item_to_update)
    assert update_status == True
    updated_item = dao.get_item(1)
    assert updated_item.title == 'Updated item'
    dao.close()


def test_delete_item():
    dao = TodoDao('test_todo.db')
    delete_status = dao.delete_item(1)
    assert delete_status == True
    deleted_item = dao.get_item(1)
    assert deleted_item is None
    dao.close()
