from time import sleep
import sys

def alert(message, blink_times=6, delay=1):
    """Display an alert message with blinking animation."""
    print(message)
    for _ in range(blink_times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)
    print()

def are_vitals_normal(temperature, pulse_rate, spo2):
    """Check if all vital signs are within the normal range."""
    if temperature > 102 or temperature < 95:
        alert('Temperature critical!')
        return False
    elif pulse_rate < 60 or pulse_rate > 100:
        alert('Pulse Rate is out of range!')
        return False
    elif spo2 < 90:
        alert('Oxygen Saturation out of range!')
        return False
    return True

def unique(seq):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = unique(my_list)
    print(unique_list)  # Output: [1, 2, 3, 4, 5]
