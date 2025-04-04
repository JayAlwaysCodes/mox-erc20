from script.deploy import deploy, INITIAL_SUPPLY
import boa

RANDOM_USER = boa.env.generate_address("random_user")

def test_token_supply():
    snek_token = deploy()
    assert snek_token.totalSupply() == INITIAL_SUPPLY

def test_token_emits_event():
    snek_token = deploy()
    
    # Get owner address first
    owner = snek_token.owner()
    
    with boa.env.prank(owner):
        # Perform transfer
        snek_token.transfer(RANDOM_USER, INITIAL_SUPPLY)
        
        # Get transfer event
        transfer_events = snek_token.get_logs()
        assert len(transfer_events) > 0  # Ensure event was emitted
        
        # Access event parameters directly
        event = transfer_events[0]
        assert event.sender == owner
        assert event.receiver == RANDOM_USER
        assert event.value == INITIAL_SUPPLY
    
    # Verify balance update
    assert snek_token.balanceOf(RANDOM_USER) == INITIAL_SUPPLY