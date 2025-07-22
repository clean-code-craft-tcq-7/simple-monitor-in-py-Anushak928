import sys
from time import sleep
from typing import List, Any, Callable

# Constants for vital sign limits
TEMP_RANGE = (95, 102)
PULSE_RANGE = (60, 100)
SPO2_MIN = 90

def alert(message: str, times: int = 6, delay: int = 1) -> None:
    """
    Show a blinking alert message.
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
    """Check if a value is within [min_val, max_val] inclusive."""
    return min_val <= value <= max_val

def check_vitals(temp: float, pulse: int, spo2: int) -> bool:
    """
    Check vitals using data-driven validation to reduce complexity.
    """
    vitals_checks = [
        ("Temperature is out of range!", lambda: is_value_in_range(temp, *TEMP_RANGE)),
        ("Pulse rate is out of range!", lambda: is_value_in_range(pulse, *PULSE_RANGE)),
        ("Oxygen saturation is out of range!", lambda: spo2 >= SPO2_MIN),
    ]

    all_normal = True
    for message, condition in vitals_checks:
        if not condition():
            alert(message)
            all_normal = False

    return all_normal

def unique(seq: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order.
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
