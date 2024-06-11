import logging
import json
import requests
from urllib.parse import urlparse
from blockagotchi import BlockaGotchi, get_current_time
from user import User, GlobalState
from shop import Item, Shop
from cartesi_wallet.util import hex_to_str, str_to_hex

logger = logging.getLogger(__name__)

class AdvanceHandler:
    EGG_LIMIT = 1000
    GLOBAL_IDS = 1

    def __init__(self, rollup_server: str, ether_portal_address: str, dao_address: str):
        self.rollup_server = rollup_server
        self.ether_portal_address = ether_portal_address
        self.dao_address = dao_address
        self.state = GlobalState().get_state()
        self.wallet = self.state["wallet"]

    def encode(self, d: dict) -> str:
        return "0x" + json.dumps(d).encode("utf-8").hex()

    def decode_json(self, b: str) -> dict:
        s = bytes.fromhex(b[2:]).decode("utf-8")
        d = json.loads(s)
        return d

    def create_notice(self, payload: str) -> bool:
        try:
            response = requests.post(self.rollup_server + "/notice", json={"payload": payload})
            logger.info(f"Received notice status {response.status_code} body {response.content}")
            return response.status_code == 200
        except Exception as error:
            logger.error(f"Failed to create notice. {error}")
            return False

    def create_report(self, payload: str) -> bool:
        try:
            response = requests.post(self.rollup_server + "/report", json={"payload": payload})
            logger.info(f"Received report status {response.status_code} body {response.content}")
            return response.status_code == 200
        except Exception as error:
            logger.error(f"Failed to create report. {error}")
            return False

    def handle(self, data: dict) -> str:
        logger.info(f"Received advance request data {data}")
        msg_sender = data["metadata"]["msg_sender"]
        payload = data["payload"]

        try:
            notice = None
            if msg_sender.lower() == self.ether_portal_address.lower():
                notice = self.wallet.ether_deposit_process(payload)
                self.create_notice(notice.payload)
                return "accept"
        except Exception as error:
            error_msg = f"Failed to process command '{payload}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"
        
        try:
            req_json = self.decode_json(payload)
            logger.info(req_json)
            action = req_json["action"]
    
            if action == "create_blockagotchi":
                return self.create_blockagotchi(msg_sender.lower(), req_json["name"])
            elif action == "feed_blockagotchi":
                return self.feed_blockagotchi(msg_sender.lower(), req_json["food_type"])
            elif action == "walk_blockagotchi":
                return self.walk_blockagotchi(msg_sender.lower(), req_json["walk_type"])
            elif action == "bathe_blockagotchi":
                return self.bathe_blockagotchi(msg_sender.lower(), req_json["bath_type"], req_json["is_paid"])
            elif action == "buy_item":
                return self.buy_item(msg_sender.lower(), req_json["item_id"])
            elif action == "apply_item":
                return self.apply_item(msg_sender.lower(), req_json["item_id"])
            return "reject"
        except Exception as error:
            error_msg = f"Failed to process action '{payload}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def create_blockagotchi(self, user_id: str, name: str) -> str:
        try:
            if self.state["global_eggs"] >= self.EGG_LIMIT:
                error_msg = f"Egg limit reached. Cannot create more blockagotchis."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"

            user = self.state["users"].get(user_id)
            if not user:
                user = User(user_id)
                self.state["users"][user_id] = user

            if user.blockagotchi is not None and user.blockagotchi.alive:
                error_msg = f"User {user_id} already has a living blockagotchi."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"

            if user.blockagotchi and not user.blockagotchi.alive:
                user.remove_blockagotchi()

            if self.wallet.balance_get(user_id).ether_get() < 1:
                error_msg = f"User {user_id} does not have enough Ether to create a blockagotchi."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"
            else:
                self.wallet.ether_transfer(user_id, self.dao_address, 1)
                birth_time = get_current_time()
                blockagotchi = BlockaGotchi(user_id, name, birth_time, self.GLOBAL_IDS)
                self.GLOBAL_IDS += 1
                user.add_blockagotchi(blockagotchi)
                self.state["blockagotchis"][blockagotchi.id] = blockagotchi
                self.state["global_eggs"] += 1
                notice_payload = {"event": "create_blockagotchi", "user_id": user_id, "blockagotchi_id": blockagotchi.id}
                self.create_notice(self.encode(notice_payload))
                logger.info(f"Created blockagotchi {blockagotchi.name} for user {user_id}. Total eggs: {self.state['global_eggs']}")
                return "accept"
        except Exception as error:
            error_msg = f"Failed to create blockagotchi for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def feed_blockagotchi(self, user_id: str, food_type: str) -> str:
        try:
            user = self.state["users"].get(user_id)
            if user and user.blockagotchi:
                user.blockagotchi.feed(food_type)
                notice_payload = self.encode({"event": "feed_blockagotchi", "user_id": user_id, "blockagotchi_id": user.blockagotchi.id, "food_type": food_type})
                self.create_notice(notice_payload)
                logger.info(f"{user.blockagotchi.name} was fed with {food_type}.")
                return "accept"
            else:
                error_msg = f"User {user_id} does not have a blockagotchi to feed."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"
        except Exception as error:
            error_msg = f"Failed to feed blockagotchi for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def walk_blockagotchi(self, user_id: str, walk_type: str) -> str:
        try:
            user = self.state["users"].get(user_id)
            if user and user.blockagotchi:
                user.blockagotchi.walk(walk_type)
                notice_payload = self.encode({"event": "walk_blockagotchi", "user_id": user_id, "blockagotchi_id": user.blockagotchi.id, "walk_type": walk_type})
                self.create_notice(notice_payload)
                logger.info(f"{user.blockagotchi.name} went for a {walk_type} walk.")
                return "accept"
            else:
                error_msg = f"User {user_id} does not have a blockagotchi to walk."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"
        except Exception as error:
            error_msg = f"Failed to walk blockagotchi for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def bathe_blockagotchi(self, user_id: str, bath_type: str, is_paid: bool) -> str:
        try:
            user = self.state["users"].get(user_id)
            if user and user.blockagotchi:
                user.blockagotchi.bathe(bath_type, is_paid)
                notice_payload = self.encode({"event": "bathe_blockagotchi", "user_id": user_id, "blockagotchi_id": user.blockagotchi.id, "bath_type": bath_type, "is_paid": is_paid})
                self.create_notice(notice_payload)
                logger.info(f"{user.blockagotchi.name} had a {bath_type} bath. Paid: {is_paid}")
                return "accept"
            else:
                error_msg = f"User {user_id} does not have a blockagotchi to bathe."
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"
        except Exception as error:
            error_msg = f"Failed to bathe blockagotchi for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def buy_item(self, user_id: str, item_id: int) -> str:
        try:
            user = self.state["users"].get(user_id)
            shop = self.state["shop"]
            item = shop.get_item(item_id)
            if user and item:
                if self.wallet.balance_get(user_id).ether_get() >= item.price:
                    user.add_item(item)
                    self.wallet.ether_transfer(user_id, self.dao_address, item.price)
                    notice_payload = self.encode({"event": "buy_item", "user_id": user_id, "item_id": item_id})
                    self.create_notice(notice_payload)
                    logger.info(f"User {user_id} bought item {item.name} for {item.price} Ether.")
                    return "accept"
                else:
                    error_msg = f"User {user_id} does not have enough Ether to buy item {item.name}."
                    logger.info(error_msg)
                    self.create_report(self.encode(error_msg))
                    return "reject"
            return "reject"
        except Exception as error:
            error_msg = f"Failed to buy item '{item_id}' for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def apply_item(self, user_id: str, item_id: int) -> str:
        try:
            user = self.state["users"].get(user_id)
            if user and user.apply_item_to_blockagotchi(item_id):
                notice_payload = self.encode({"event": "apply_item", "user_id": user_id, "item_id": item_id})
                self.create_notice(notice_payload)
                logger.info(f"User {user_id} applied item {item_id} to their blockagotchi.")
                return "accept"
            else:
                error_msg = f"User {user_id} got an error while trying to apply item {item_id}"
                logger.info(error_msg)
                self.create_report(self.encode(error_msg))
                return "reject"
        except Exception as error:
            error_msg = f"Failed to apply item '{item_id}' for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"
    
    def remove_item(self, user_id: str, item_id: int) -> str:
        try:
            user = self.state["users"].get(user_id)
            if user and user.remove_item_from_blockagotchi(item_id):
                notice_payload = self.encode({"event": "remove_item", "user_id": user_id, "item_id": item_id})
                self.create_notice(notice_payload)
                logger.info(f"User {user_id} removed item {item_id} from their blockagotchi.")
                return "accept"
            return "reject"
        except Exception as error:
            error_msg = f"Failed to remove item '{item_id}' for user '{user_id}'. {error}"
            self.create_report(self.encode(error_msg))
            logger.debug(error_msg, exc_info=True)
            return "reject"