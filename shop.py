from typing import Dict

class Item:
    def __init__(self, item_id: int, name: str, description: str, price: int):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self) -> Dict[str, any]:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class Shop:
    def __init__(self):
        self.items = {}
        self._initialize_items()

    def _initialize_items(self):
        # Initialize shop with some items
        self.items[1] = Item(1, "Hat", "A nice hat for your blockagotchi", 10)
        self.items[2] = Item(2, "Glasses", "Cool glasses for your blockagotchi", 15)
        self.items[3] = Item(3, "Scarf", "A warm scarf for your blockagotchi", 20)
        self.items[4] = Item(4, "Gotchi-Winter", "Winter Skin for your blockagotchi Device", 30)
        self.items[5] = Item(5, "Gotchi-Summer", "Summer Skin for your blockagotchi Device", 30)
        self.items[6] = Item(6, "Gotchi-Fall", "Fall Skin for your blockagotchi Device", 30)
        self.items[7] = Item(7, "Gotchi-Spring", "Spring Skin for your blockagotchi Device", 30)

    def get_items(self) -> Dict[int, Item]:
        return self.items

    def get_item(self, item_id: int) -> Item:
        return self.items.get(item_id)

# Example usage
if __name__ == "__main__":
    shop = Shop()
    items = shop.get_items()
    for item_id, item in items.items():
        print(item.to_dict())
