from time import sleep
import sys
from typing import List, Any

# Constants for vital sign limits
TEMP_MIN = 95
TEMP_MAX = 102
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 90

def alert(message: str, times: int = 6, delay: int = 1) -> None:
    """Show a blinking alert message."""
    print(message)
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)
    print()

def check_vitals(temp: float, pulse: int, spo2: int) -> bool:
    """
    Return True if all vitals are normal, else alert and return False.
    """
    if temp > TEMP_MAX or temp < TEMP_MIN:
        alert('Temperature critical!')
        return False
    if pulse < PULSE_MIN or pulse > PULSE_MAX:
        alert('Pulse Rate is out of range!')
        return False
    if spo2 < SPO2_MIN:
        alert('Oxygen Saturation out of range!')
        return False
    return True

def unique(seq: List[Any]) -> List[Any]:
    """
    Return a list with duplicates removed, preserving order.
    """
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

# Example usage
if __name__ == "__main__":
    # Check vitals example
    check_vitals(101, 80, 95)
    # Remove duplicates example
    my_list = [1, 2, 2, 3, 4, 4, 5]
    print(unique(my_list))  # Output: [1, 2, 3, 4, 5]
