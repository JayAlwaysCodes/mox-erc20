from script.deploy import deploy, INITIAL_SUPPLY

def test_token_supply():
    snek_token = deploy()

    assert snek_token.totalSupply() == INITIAL_SUPPLY
    