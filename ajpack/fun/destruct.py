import time

def self_destruct() -> None:
    """
    Self destruction on point!
    """
    # Count down
    for i in range(5, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)
    
    # Wait two seconds before printing the message
    time.sleep(2)
    print(";) Just kidding! I would never do that...")
