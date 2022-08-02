import pytest

from core.utils.services import get_random_string


@pytest.mark.parametrize(
    'length, prefix, suffix, expected',
    (
            (12, 'test', 'service', "Test_skjdcnsjndkservice"),
            (10, 'test2', 'service2', "Test2_skjdcnsjnservice2"),
            (5, 'test3', 'service3', "Test3_skjdservice3"),
    )
)
def test_get_random_string(
        length: int,
        prefix: str,
        suffix: str,
        expected: str,
        client
):
    string = get_random_string(length, prefix, suffix)
    assert all([string.startswith(prefix.title()), expected.startswith(prefix.title())])
    assert all([string.endswith(suffix), expected.endswith(suffix)])
    assert len(string) == len(expected)
