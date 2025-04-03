from contracts import myToken
from eth_utils import to_wei
from moccasin.boa_tools import VyperContract

INITIAL_SUPPLY = to_wei(1000, "ether")

def deploy() -> VyperContract:
    snek_contract = myToken.deploy(INITIAL_SUPPLY)
    print(f"Token deployed at address: {snek_contract.address}")
    print(f"Token deployed with initial supply: {INITIAL_SUPPLY} wei")
    return snek_contract


def moccasin_main() -> VyperContract:
    return deploy()