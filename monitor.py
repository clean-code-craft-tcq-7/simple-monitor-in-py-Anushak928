import sys
from time import sleep
from typing import List, Any

# Constants for vital sign limits
TEMP_RANGE = (95, 102)
PULSE_RANGE = (60, 100)
SPO2_MIN = 90

def alert(message: str, times: int = 6, delay: int = 1) -> None:
    """
    Show a blinking alert message.
    Args:
        message (str): The alert message to show.
        times (int): Number of blink cycles.
        delay (int): Delay in seconds between blinks.
    """
    print(message)
    blink_pattern = ['\r* ', '\r *']
    for _ in range(times):
        for pattern in blink_pattern:
            print(pattern, end='')
            sys.stdout.flush()
            sleep(delay)
    print()

def is_value_in_range(value: float, min_val: float, max_val: float) -> bool:
    """Helper to check if a value is within an inclusive range."""
    return min_val <= value <= max_val

def check_vitals(temp: float, pulse: int, spo2: int) -> bool:
    """
    Check if all vitals are within normal range.
    Returns:
        bool: True if all vitals are normal, False otherwise.
    """
    if not is_value_in_range(temp, *TEMP_RANGE):
        alert('Temperature is out of range!')
        return False

    if not is_value_in_range(pulse, *PULSE_RANGE):
        alert('Pulse rate is out of range!')
        return False

    if spo2 < SPO2_MIN:
        alert('Oxygen saturation is out of range!')
        return False

    return True

def unique(seq: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order.
    Args:
        seq (List[Any]): The list to process.
    Returns:
        List[Any]: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    # Example usage
    _ = check_vitals(temp=101, pulse=80, spo2=95)
    print(unique([1, 2, 2, 3, 4, 4, 5]))
