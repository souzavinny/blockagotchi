import logging
from urllib.parse import urlparse
from blockagotchi import BlockaGotchi, get_current_time
from user import User, GlobalState
from shop import Item, Shop
import json
import requests
from cartesi_wallet.util import hex_to_str

logger = logging.getLogger(__name__)

class InspectHandler:
    def __init__(self, rollup_server: str):
        self.state = GlobalState().get_state()
        self.rollup_server = rollup_server

    def encode(self, d: dict) -> str:
        return "0x" + json.dumps(d).encode("utf-8").hex()

    def handle(self, data: dict) -> dict:
        logger.info(f"Received inspect request data {data}")
        report = {}
        try:
            url = urlparse(hex_to_str(data["payload"]))
            path = url.path.lower()
            if path.startswith("balance/"):
                report = self.get_balance(path)
            elif path.startswith("user_blockagotchi/"):
                report = self.get_user_blockagotchi(path)
            elif path.startswith("all_blockagotchis"):
                report = self.get_all_blockagotchis()
            elif path.startswith("blockagotchi/"):
                report = self.get_blockagotchi(path)
            elif path.startswith("shop_items"):
                report = self.get_shop_items()
            elif path.startswith("ranking"):
                report = self.get_ranking()

            response = requests.post(self.rollup_server + "/report", json=report)
            logger.info(f"Received report status {response.status_code} body {response.content}")

            return "accept"
        except Exception as error:
            error_msg = f"Failed to process inspect request. {error}"
            logger.debug(error_msg, exc_info=True)
            return "reject"

    def get_balance(self, path: str) -> dict:
        try:
            info = path.replace("balance/", "").split("/")
            token_type, account = info[0], info[1]
            amount = 0
            if token_type == "ether":
                amount = self.state["wallet"].balance_get(account).ether_get()
            return {"payload": self.encode({"amount": str(amount), "token_type": token_type})}
        except Exception as error:
            error_msg = f"Failed to get balance for path '{path}'. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}

    def get_user_blockagotchi(self, path: str) -> dict:
        try:
            user_id = path.replace("user_blockagotchi/", "")
            user = self.state["users"].get(user_id)
            if user and user.blockagotchi:
                return {"payload": self.encode(user.blockagotchi.to_dict())}
            return {"payload": self.encode({"error": "User or blockagotchi not found"})}
        except Exception as error:
            error_msg = f"Failed to get user blockagotchi for path '{path}'. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}

    def get_all_blockagotchis(self) -> dict:
        try:
            blockagotchis = [blockagotchi.to_dict() for blockagotchi in self.state["blockagotchis"].values()]
            return {"payload": self.encode(blockagotchis)}
        except Exception as error:
            error_msg = f"Failed to get all blockagotchis. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}

    def get_blockagotchi(self, path: str) -> dict:
        try:
            blockagotchi_id = path.replace("blockagotchi/", "")
            blockagotchi = self.state["blockagotchis"].get(int(blockagotchi_id))
            if blockagotchi:
                return {"payload": self.encode(blockagotchi.to_dict())}
            return {"payload": self.encode({"error": "blockagotchi not found"})}
        except Exception as error:
            error_msg = f"Failed to get blockagotchi for path '{path}'. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}

    def get_shop_items(self) -> dict:
        try:
            shop = self.state["shop"]
            items = [item.to_dict() for item in shop.get_items().values()]
            return {"payload": self.encode(items)}
        except Exception as error:
            error_msg = f"Failed to get shop items. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}

    def get_ranking(self) -> dict:
        try:
            blockagotchis = sorted(self.state["blockagotchis"].values(), key=lambda x: x.overall_score, reverse=True)
            ranking = [blockagotchi.to_dict() for blockagotchi in blockagotchis]
            return {"payload": self.encode(ranking)}
        except Exception as error:
            error_msg = f"Failed to get ranking. {error}"
            logger.debug(error_msg, exc_info=True)
            return {"payload": self.encode({"error": error_msg})}
