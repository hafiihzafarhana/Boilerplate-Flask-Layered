from app.repositories.item_repository import ItemRepository

class ItemService:
    @staticmethod
    def get_all_items():
        """Mengambil semua item dan mengembalikannya."""
        items = ItemRepository.get_all_items()
        return items

    @staticmethod
    def get_item_by_id(item_id):
        """Mengambil item berdasarkan ID."""
        item = ItemRepository.get_item_by_id(item_id)
        return item

    @staticmethod
    def create_item(name, description):
        """Membuat item baru."""
        new_item = ItemRepository.create_item(name, description)
        return new_item
