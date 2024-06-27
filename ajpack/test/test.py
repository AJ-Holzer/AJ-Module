from typing import Any

def simple_test(txt: Any) -> bool:
    """Test that the function works as expected."""
    green: str = "\033[92m"
    
    print(f"{green}The function works! --> {str(txt)}")
    return True