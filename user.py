from typing import Optional, Dict, List
from blockagotchi import BlockaGotchi
from cartesi_wallet import wallet as Wallet
from shop import Item, Shop

class User:
    def __init__(self, user_id: str):
        self.id = user_id
        self.blockagotchi: Optional[BlockaGotchi] = None
        self.items: List[Item] = []

    def add_blockagotchi(self, blockagotchi: BlockaGotchi) -> None:
        self.blockagotchi = blockagotchi

    def get_blockagotchi(self) -> Optional[BlockaGotchi]:
        return self.blockagotchi

    def remove_blockagotchi(self) -> None:
        self.blockagotchi = None

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def get_items(self) -> List[Item]:
        return self.items

    def apply_item_to_blockagotchi(self, item_id: int) -> bool:
        if self.blockagotchi:
            item = next((item for item in self.items if item.item_id == item_id), None)
            if item and item not in self.blockagotchi.items:
                self.blockagotchi.add_item(item)
                self.blockagotchi.happiness += item.price
                self.items.remove(item)
                return True
        return False
    
    def remove_item_from_blockagotchi(self, item_id: int) -> bool:
        if self.blockagotchi:
            item = next((item for item in self.blockagotchi.items if item.item_id == item_id), None)
            if item:
                self.blockagotchi.remove_item(item)
                self.blockagotchi.happiness -= item.price
                self.items.append(item)
                return True
        return False

    def to_dict(self) -> Dict[str, any]:
        return {
            "id": self.id,
            "blockagotchi": self.blockagotchi.to_dict() if self.blockagotchi else None,
            "items": [item.to_dict() for item in self.items]
        }

class GlobalState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalState, cls).__new__(cls)
            cls._instance.state = {
                "blockagotchis": {},
                "users": {},
                "tokens": {},
                "global_eggs": 0,
                "wallet": Wallet,
                "shop": Shop()
            }
        return cls._instance

    def get_state(self) -> Dict[str, any]:
        return self.state
