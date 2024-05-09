"""A simple AI Action template for comparing timezones.

Please checkout the base guidance on AI Actions in our main repository readme:
https://github.com/sema4ai/actions#readme
"""

from datetime import datetime

import pytz
from sema4ai.actions import action
from zoneinfo import ZoneInfo


@action
def compare_time_zones(user_timezone: str, compare_to_timezones: str) -> str:
    """Compares user timezone time difference to given timezones.

    Args:
        user_timezone: User timezone in tz database format.
            Example: "Europe/Helsinki"
        compare_to_timezones: Comma separated timezones in tz database format.
            Example: "America/New_York, Asia/Kolkata"

    Returns:
        A string with the requested timezones, their current time and the user time
        difference in hours.
    """
    output: list[str] = []

    try:
        user_tz = pytz.timezone(user_timezone)
        user_now = datetime.now(user_tz)
    except pytz.InvalidTimeError:
        return f"Timezone {user_timezone!r} could not be found. Use tz database format."

    output.append(
        f"- Current time in {user_timezone} is {user_now.strftime('%I:%M %p')}"
    )

    target_timezones = [s.strip() for s in compare_to_timezones.split(",")]
    for timezone in target_timezones:
        try:
            target_tz = pytz.timezone(timezone)
            target_now = datetime.now(target_tz)
            user_offset, target_offset = (
                user_now.astimezone(ZoneInfo(user_timezone)).utcoffset(),
                user_now.astimezone(ZoneInfo(timezone)).utcoffset(),
            )
            time_diff = (user_offset - target_offset).total_seconds() / 3600

            output.append(
                f"- Current time in {timezone} is {target_now.strftime('%I:%M %p')}, the difference with {user_timezone} is {time_diff} hours"
            )
        except pytz.InvalidTimeError:
            output.append(
                f"- Timezone '{timezone}' could not be found. Use tz database format."
            )

    # Pretty print for log
    output_string = "\n".join(output)
    print(output_string)
    return output_string
