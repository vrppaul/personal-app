# Backend part of the App

## Currently implemented apps
- [Planner](#planner)


## Planner

Simply creates TODO tasks, which can be planned on several levels:
- Day
- Week
- Month
- Year
- Uncategorized (without concrete due date)

### Main parts
- **Planned period**. Represents some period of time, which can be either day, week, month or year.

    All tasks are either connected to some period, which means that have a due time or not connected,
which equals to not having a due time.

    Planned period is created dynamically either when a new task is created for this planned or
    at the last day of the week (7 new day periods are created and 1 week period), at the last day of month, at the last day of year.

    If user requests periods too far into the future, no periods may be returned, which means that no tasks were created for selected dates.


- **Planned task**. Represents the task that should be done. Can be planned to any time in the future.

    Each task can be connected to a specific time period, which would mean that it has a due date.

    Each task can be moved from any date period to any other time period or be made uncategorized,
    which would mean no due date.
