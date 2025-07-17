from time import sleep
import sys

def show_alert(message, blink_times=6, delay=1):
    """Display an alert message with blinking animation and return False."""
    print(message)
    for _ in range(blink_times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)
    print()
    return False

def vitals_ok(temperature, pulse_rate, spo2):
    """Check if all vital signs are within the normal range."""
    if temperature > 102 or temperature < 95:
        return show_alert('Temperature critical!')
    elif pulse_rate < 60 or pulse_rate > 100:
        return show_alert('Pulse Rate is out of range!')
    elif spo2 < 90:
        return show_alert('Oxygen Saturation out of range!')
    return True

def remove_duplicates(seq):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

# Example usage
if __name__ == "__main__":
    # Vital signs check
    vitals_ok(103, 72, 95)

    # Remove duplicates example
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print("Unique List:", remove_duplicates(sample_list))