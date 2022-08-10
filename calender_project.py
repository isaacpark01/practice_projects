from time import time
import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

#loop to get a year from the user. 
while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("please enter a numeric year, like 2023")

    continue
#loop to get a month from the user. 
while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for march.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number form 1 to 12.')

def getCalendarFor(year, month):
    calText = ''
    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

# Add the days of the week labels to the calendar:
# (!) Try changing this to abbreviations: SUN, MON, TUE, etc.

    calText += '...Sunday.... Monday....Tuesday...Wednesday..thursday...Friday...Saturday..\n'
    #the horizontal line string that separate weeks:
    weekSeparator = ('+---------' * 7) + '+\n'

    blankRow = ('|        ' * 7) + '|\n'

    #Get the first date in the month. (the datime module handles all the complacated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)
    #Roll back currentdate until it is sunda. (weekda()returns 6 for sunday, not 0)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True:
        calText += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' +  dayNumberLabel  + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        
        calText += dayNumberRow 
        for i in range(3):
            calText += blankRow 
        
        if currentDate.month != month:
            break

    calText += weekSeparator 
    return calText

calText = getCalendarFor(year, month)
print(calText)

#save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('saved to ' + calendarFilename)

