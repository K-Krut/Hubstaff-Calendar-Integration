from datetime import datetime, timedelta
from typing import List, Dict


# def merge_activities(activities: List[Dict], max_gap_minutes=5) -> List[Dict]:
#     if not activities:
#         return []
#
#     sorted_activities = sorted(activities, key=lambda x: x["starts_at"])
#     merged_sessions = []
#
#     current_session = {
#         "start": datetime.fromisoformat(sorted_activities[0]["starts_at"].replace("Z", "+00:00")),
#         "end": datetime.fromisoformat(sorted_activities[0]["starts_at"].replace("Z", "+00:00")) + timedelta(seconds=sorted_activities[0].get("tracked", 0)),
#     }
#
#     for activity in sorted_activities[1:]:
#         start_time = datetime.fromisoformat(activity["starts_at"].replace("Z", "+00:00"))
#         end_time = start_time + timedelta(seconds=activity.get("tracked", 0))
#
#         if (start_time - current_session["end"]).total_seconds() <= max_gap_minutes * 60:
#             current_session["end"] = max(current_session["end"], end_time)
#         else:
#             merged_sessions.append(current_session)
#             current_session = {
#                 "start": start_time,
#                 "end": end_time,
#             }
#
#     merged_sessions.append(current_session)
#     return merged_sessions
#

def merge_activities(activities: List[Dict], max_gap_minutes=5) -> List[Dict]:
    if not activities:
        return []

    sorted_activities = sorted(activities, key=lambda x: x["starts_at"])
    merged_sessions = []

    current_start = datetime.fromisoformat(sorted_activities[0]["starts_at"].replace("Z", "+00:00"))
    current_end = current_start + timedelta(seconds=sorted_activities[0].get("tracked", 0))

    for activity in sorted_activities[1:]:
        start_time = datetime.fromisoformat(activity["starts_at"].replace("Z", "+00:00"))
        end_time = start_time + timedelta(seconds=activity.get("tracked", 0))

        if (start_time - current_end).total_seconds() <= max_gap_minutes * 60:
            current_end = max(current_end, end_time)
        else:
            merged_sessions.append({
                "start": current_start.isoformat(),
                "end": current_end.isoformat(),
            })
            current_start = start_time
            current_end = end_time

    merged_sessions.append({
        "start": current_start.isoformat(),
        "end": current_end.isoformat(),
    })

    return merged_sessions