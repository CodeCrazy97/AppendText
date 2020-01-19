'''                          
 This program will allow me to send a weekly summary of events to a   
 simple text file.

 Script must be ran the week after the week that the report is for.
 So, you can run this script any day during the week following the 
 week that the script is for.
 
 Created: 02/02/2019

 07/21/2019 - Discovered a bug with the program computing the correct date.
 10/20/2019 - Added functionality for the script to open the "Weekly Report.txt" file for user to type,
 instead of prompting user to enter events from command line.
 1/18/2019 - Checking to see if entries were made for two weeks ago.
'''

import webbrowser, os
from datetime import date

# Before running this script, please change the below file path to point to your journal file.
JOURNAL_FILE = "C:\\Users\\Ethan\\Documents\\Writings\\Weekly Report.txt"


'''

 get_date - returns a string of form "Month, Day Year"
 n - the number of weeks backwards to traverse to get the date of the Sunday of that week.
 
Example: suppose today is Wednesday, November 20, 2019. If get_date is called, with
2 being n, then this function will return the date of the first Sunday from two weeks prior.
The return value would be "November 3, 2019".

'''
def get_date(n):
    # Get the "week of" date in the form: Month Day, Year.
    curr_date = date.today()

    day = curr_date.day
    month = curr_date.month
    year = curr_date.year

    sunday_count = 0

    new_date = curr_date

    while (sunday_count < n + 1):
        new_date = date(year, month, day)  # Create a new date based on the day.
        if (new_date.weekday() == 6):  # Check if it is a Sunday.
            sunday_count += 1
            if (sunday_count == n):
                break
        if (new_date.day == 1):  # First day of the month. Will have to handle the previous month.
            if curr_date.month > 1:
                month -= 1
            else:
                year -= 1
                month = 12

            # Find out what the previous month is. From there, you will find the last day of the month (30 for April, 31 for December, for example)

            if curr_date.month == 1:  # January is the current month.
                day = 31
            elif curr_date.month == 2:  # February is the current month.
                day = 31
            elif curr_date.month == 3:
                day = 28
            elif curr_date.month == 4:
                day = 31
            elif curr_date.month == 5:
                day = 30
            elif curr_date.month == 6:
                day = 31
            elif curr_date.month == 7:
                day = 30
            elif curr_date.month == 8:
                day = 31
            elif curr_date.month == 9:
                day = 31
            elif curr_date.month == 10:
                day = 30
            elif curr_date.month == 11:
                day = 31
            elif curr_date.month == 12:
                day = 30
        else:  # Simply subtract one from the day.
            day -= 1

    week_of = ""
    if month == 1:
        week_of = "January"
    elif month == 2:
        week_of = "February"
    elif month == 3:
        week_of = "March"
    elif month == 4:
        week_of = "April"
    elif month == 5:
        week_of = "May"
    elif month == 6:
        week_of = "June"
    elif month == 7:
        week_of = "July"
    elif month == 8:
        week_of = "August"
    elif month == 9:
        week_of = "September"
    elif month == 10:
        week_of = "October"
    elif month == 11:
        week_of = "November"
    elif month == 12:
        week_of = "December"

    week_of = week_of + " " + str(new_date.day) + ", " + str(new_date.year)
    return week_of

'''
entry_made_for_week - checks if a journal entry has been made for a particular week.
If one has not been entered for week_of, then the initial prompt is written to the file.
    This would be written to the file if an entry had not been made for the week of January 5, 2020:
        *** Week of January, 5, 2020 ***

The function returns true or false, based on whether or not the journal entries file contains
an entry for the week_of.
'''
def entry_made_for_week(week_of):
    fo = open(JOURNAL_FILE, 'r')
    content = fo.read()
    if ('*** Week of ' + week_of + ' ***') not in content:
        experiences = open(JOURNAL_FILE, 'a')
        experiences.writelines(str("\n\n*** Week of " + week_of + " ***\n"))
        experiences.close()
        fo.close()
        return False
    fo.close()
    return True

if not os.path.exists(JOURNAL_FILE):
    print("Looks like you don't have a journal started. The file ", JOURNAL_FILE, " does not exist!")
    exit(0)

# Check if a journal entry was made for two weeks ago as well as last week.

two_weeks_ago = get_date(3)
last_week = get_date(2)

if not entry_made_for_week(two_weeks_ago) or not entry_made_for_week(last_week):
    # Open the file so the user can journal about stuff.
    webbrowser.open(JOURNAL_FILE)
    exit(0)
else:
    input("\n\n You're all up-to-date on your journal! ")
