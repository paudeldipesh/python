import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5


print(f"Done for 20: {fx(20)}")
print(f"Done for 6: {fx(6)}")
print(f"Done for 2: {fx(2)}")
