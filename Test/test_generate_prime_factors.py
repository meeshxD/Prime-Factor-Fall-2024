import pytest
from prime import generate_prime_factors
def test_1_string():
    with pytest.raises(ValueError, match="Wrong data type, must be an integer"):
        generate_prime_factors("string")
