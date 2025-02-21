import time
import pytest
from gringo.sleep import sleep

def test_sleep_duration():
    start_time = time.time()
    sleep(0.1)
    duration = time.time() - start_time
    assert 0.09 <= duration <= 0.2  # Allow some margin for system timing

def test_negative_duration():
    with pytest.raises(ValueError, match="Sleep duration must be non-negative"):
        sleep(-1)

def test_zero_duration():
    start_time = time.time()
    sleep(0)
    duration = time.time() - start_time
    assert duration < 0.1  # Should return almost immediately