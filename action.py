from robocorp.actions import action
from datetime import datetime

@action
def get_current_date() -> str:
    """
    Returns the current date in ISO format.
    """
    return datetime.now().isoformat()
