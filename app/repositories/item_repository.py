from app.models.item_model import Item
from core.extensions import db

class ItemRepository:
    @staticmethod
    def get_all_items():
        """Mengambil semua item dari database."""
        return Item.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        """Mengambil item berdasarkan ID."""
        return Item.query.get(item_id)

    @staticmethod
    def create_item(name, description):
        """Membuat item baru."""
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return new_item
