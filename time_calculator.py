import re
import math

def add_time(start, duration, start_day=None):
    start_split = re.split(r'[: ]', start)
    
    start_hour_raw = int(start_split[0])
    start_minute_raw = int(start_split[1])
    start_am_pm = start_split[2]

    duration_split = re.split(':', duration)
    
    duration_hour_raw = int(duration_split[0])
    duration_minute_raw = int(duration_split[1])

    # Handle minute over hour conversion
    if duration_minute_raw + start_minute_raw >= 60:
        processing_minute = start_minute_raw + duration_minute_raw - 60
        processing_hour = start_hour_raw + duration_hour_raw + 1
    else:
        processing_minute = start_minute_raw + duration_minute_raw
        processing_hour = start_hour_raw + duration_hour_raw
    
    # Add hours if PM start
    if start_am_pm == 'PM':
        processing_hour += 12
    
    # Get final AM/PM
    if processing_hour % 24 >= 12:
        am_pm = 'PM'
    else:
        am_pm = 'AM'
    
    # Get days passed counter and final hour in 24hr clock
    if processing_hour > 24:
        day_counter = 0

        while processing_hour > 24:
            processing_hour -= 24
            day_counter += 1
    else:
        day_counter = 0
    
    # Handle 0 o'clock
    if processing_hour == 0:
        processing_hour = 12
    
    if processing_hour > 12:
        processing_hour -= 12

        if am_pm == 'AM':
            day_counter += 1
    
    
    # Convert to string format
    final_hour = str(processing_hour)
    
    string_minute = str(processing_minute)
    if len(string_minute) < 2:
        final_minute = '0' + string_minute
    else:
        final_minute = string_minute
    
    # Create new time string
    new_time = ''
    new_time += final_hour
    new_time += ':'
    new_time += final_minute
    new_time += ' ' + am_pm

    # Adding final day of week
    day_dict = {'sunday':1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7}
    day_list = list(day_dict.keys())
    
    if start_day:
        start_day_number = day_dict[start_day.lower()]
        day_diff = start_day_number + day_counter % 7
        if day_diff > 7:
            day_diff -= 7
        new_time += f', {day_list[day_diff - 1].title()}'
    
    # Adding days later counter
    if day_counter == 0:
        pass
    elif day_counter == 1:
        new_time += ' (next day)'
    elif day_counter > 1:
        new_time += f' ({day_counter} days later)'

    return new_time