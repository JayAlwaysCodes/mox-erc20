import pytest
from contracts.sub_lesson import stateless_fuzz_solvable
from hypothesis import given, HealthCheck, settings
from boa.test.strategies import strategy

@pytest.fixture(scope="session")
def contract():
    deployed = stateless_fuzz_solvable.deploy()
    print(f"Contract deployed at: {deployed.address}")
    return deployed

@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(input=strategy("uint256"))
def test_always_returns_input_number(contract, input):
    try:
        result = contract.always_returns_input_number(input)
        print(f"Input: {input}, Result: {result}")
        assert result == input, f"Expected {input}, got {result}"
    except Exception as e:
        print(f"Exception occurred with input {input}: {str(e)}")
        raise