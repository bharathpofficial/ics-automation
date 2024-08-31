from icalendar import Calendar, Event, vDatetime, Timezone, TimezoneStandard
from datetime import datetime, timedelta
import pytz
import pandas as pd
import uuid

# AUTHOR: BHARATH P [& also AI DRIVEN DEVELOPMENT]


# Load the cleaned schedule
df = pd.read_csv("./files/cleaned_schedule-2a.csv")

# Define the IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Time slots in the format (start_time, end_time)
time_slots = {
    "Morning": ("09:00", "12:30"),
    "Afternoon": ("13:30", "16:30")
}

# Create a VTIMEZONE component for IST
timezone = Timezone()
timezone.add('TZID', 'Asia/Kolkata')

# Define standard time
standard = TimezoneStandard()
standard.add('DTSTART', datetime(1970, 1, 1, 0, 0, 0))
standard.add('TZOFFSETFROM', timedelta(hours=5, minutes=30))
standard.add('TZOFFSETTO', timedelta(hours=5, minutes=30))
standard.add('TZNAME', 'IST')

timezone.add_component(standard)

# Group by batch (session) and create an ICS file for each batch
for batch in df['Session'].unique():
    # Create a new calendar
    cal = Calendar()
    cal.add('prodid', '-//Your Training Schedule//mxm.dk//')
    cal.add('version', '2.0')
    cal.add_component(timezone)  # Add the timezone component

    # Filter events for the current batch
    batch_events = df[df['Session'] == batch]

    for _, event_info in batch_events.iterrows():
        # Create an event
        event = Event()

        # Parse date and time
        session_date = event_info['Date']
        time_of_day = event_info['Time']

        # Get start and end times
        start_time_str, end_time_str = time_slots[time_of_day]
        start_time = datetime.strptime(f"{session_date} {start_time_str}", "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(f"{session_date} {end_time_str}", "%Y-%m-%d %H:%M")

        # Localize the times to IST
        start_time_ist = ist.localize(start_time)
        end_time_ist = ist.localize(end_time)

        # Set event properties with localized times
        event.add('summary', f"{event_info['Type']} - {batch}")
        event.add('dtstart', vDatetime(start_time_ist))
        event.add('dtend', vDatetime(end_time_ist))
        event.add('dtstamp', vDatetime(datetime.now(pytz.UTC)))
        event.add('location', event_info['Location'])
        event.add('uid', str(uuid.uuid4()))  # Add a unique UID for each event

        # Add event to calendar
        cal.add_component(event)

    # Write the calendar to an .ics file
    filename = f"{batch.replace(' ', '_')}.ics"
    with open(f"./files/{filename}", 'wb') as f:
        f.write(cal.to_ical())

    print(f"ICS file created for batch {filename}")

print("All ICS files have been created successfully!")
