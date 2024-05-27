import logging
import requests
from os import environ
from advance_handler import AdvanceHandler
from inspect_handler import InspectHandler

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = "http://localhost:8080/rollup"
if "ROLLUP_HTTP_SERVER_URL" in environ:
    rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

dapp_relay_address = "0xF5DE34d6BbC0446E2a45719E718efEbaaE179daE"
ether_portal_address = "0xFfdbe43d4c855BF7e0f105c400A50857f53AB044"
dao_address = "0x0000000000000000000000000000000000000000"

advance_handler = AdvanceHandler(rollup_server, ether_portal_address, dao_address)
inspect_handler = InspectHandler(rollup_server)

handlers = {
    "advance_state": advance_handler.handle,
    "inspect_state": inspect_handler.handle,
}
finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(data)
