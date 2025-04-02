from contracts import myToken
from eth_utils import to_wei

INITIAL_SUPPLY = to_wei(1000, "ether")

def deploy():
    snek_contract = myToken.deploy(INITIAL_SUPPLY)
    print(f"Token deployed at address: {snek_contract.address}")
    print(f"Token deployed with initial supply: {INITIAL_SUPPLY} wei")


def moccasin_main():
    return deploy()