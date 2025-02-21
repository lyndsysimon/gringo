import time
from typing import Union, Optional

def sleep(duration: Union[int, float], *, interrupt_on: Optional[str] = None) -> None:
    """Sleep for the specified duration.
    
    Args:
        duration: Time to sleep in seconds
        interrupt_on: If provided, the function will check for this string in stdin
                     and return early if found. The string must end with a newline.
    """
    if duration < 0:
        raise ValueError("Sleep duration must be non-negative")
        
    if interrupt_on is not None:
        import sys
        import select
        
        end_time = time.time() + duration
        while time.time() < end_time:
            remaining = end_time - time.time()
            if remaining <= 0:
                break
                
            # Check if there's input available
            if select.select([sys.stdin], [], [], remaining)[0]:
                line = sys.stdin.readline()
                if line.rstrip('\n') == interrupt_on:
                    return
            
    else:
        time.sleep(duration)