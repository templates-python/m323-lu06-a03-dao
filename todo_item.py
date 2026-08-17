from dataclasses import dataclass


# TODO: Implementiere die TodoItem-Klasse mit @dataclass
@dataclass
class TodoItem:
    item_id: int
    title: str
    is_completed: bool
