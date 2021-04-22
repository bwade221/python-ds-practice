def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    week = range(1,8)
    week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','friday','Saturday']
    index = day_of_week - 1

    if day_of_week in week:
        return week_days[index]
    else:
        return

print(weekday_name(1))
print(weekday_name(7))
print(weekday_name(0))
print(weekday_name(9))