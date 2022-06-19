import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

CACHE_DIRECTORY = ".cache/"


def find(key: str) -> Optional[str]:
    """Find a cache with `key`

    Parameters:
        key: The cache key

    Returns:
        The cache value, None if not exists

    """
    file_path = os.path.join(os.getcwd(), CACHE_DIRECTORY, key)
    if os.path.exists(file_path):
        with open(file_path) as f:
            return f.read()
    else:
        return None


def write(key: str, value: str):
    """Write a cache with provided `key` and `value`

    Parameters:
        key: The cache key
        value: The cache value

    """
    file_path = os.path.join(os.getcwd(), CACHE_DIRECTORY, key)
    os.makedirs(os.path.pardir(file_path), exist_ok=True)
    os.write(file_path, bytes(value, "utf-8"))
