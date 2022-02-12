import datetime,time

def getMonthByNumber(num):
        if(num==1):
                return "Jan"
        elif(num==2):
                return "Feb"
        elif (num == 3):
                return "Mar"
        elif (num == 4):
                return "Apr"
        elif (num == 5):
                return "May"
        elif (num == 6):
                return "Jun"
        elif (num == 7):
                return "Jul"
        elif (num == 8):
                return "Aug"
        elif (num == 9):
                return "Sep"
        elif (num == 10):
                return "Oct"
        elif (num == 11):
                return "Nov"
        elif (num == 12):
                return "Dec"

def getMonthNumber(mnth):
        mnth = mnth.lower()
        if(mnth == "Jan".lower()):
                return 1
        elif (mnth == "Feb".lower()):
                return 2
        elif (mnth == "Mar".lower()):
                return 3
        elif (mnth == "Apr".lower()):
                return 4
        elif (mnth == "May".lower()):
                return 5
        elif (mnth == "Jun".lower()):
                return 6
        elif (mnth == "Jul".lower()):
                return 7
        elif (mnth == "Aug".lower()):
                return 8
        elif (mnth == "Sep".lower()):
                return 9
        elif (mnth == "Oct".lower()):
                return 10
        elif (mnth == "Nov".lower()):
                return 11
        elif (mnth == "Dec".lower()):
                return 12


def getTimestampWithoutTimes(date):
        lst = date.split(' ')
        mnth = getMonthNumber(lst[1])
        dt = int(lst[2])
        yr = int(lst[3])
        hr = 0
        mn = 0
        sec = 0
        msec = 0
        
        timestamp = time.mktime(datetime.datetime(yr,mnth,dt,hr,mn,sec,msec).timetuple())
        return timestamp

def getKeyTimeStamp(date):
        lst = date.split('-')
        dt = int(lst[0])
        mnth = int(lst[1])
        yr = int(lst[2])
        hr = 0
        mn = 0
        sec = 0
        msec = 0

        timestamp = time.mktime(datetime.datetime(yr, mnth, dt, hr, mn, sec, msec).timetuple())
        return timestamp


def getStartDateWithoutTimes(date):
        lst = date.split(' ')
        mnth = getMonthNumber(lst[1])
        dt = int(lst[2])
        yr = int(lst[3])
        hr = 0
        mn = 0
        sec = 0
        msec = 0

        timestamp = time.mktime(datetime.datetime(yr, mnth, dt, hr, mn, sec, msec).timetuple())
        return timestamp


def getEndDateWithoutTimes(date):
        lst = date.split(' ')
        mnth = getMonthNumber(lst[1])
        dt = int(lst[2])
        yr = int(lst[3])
        hr = 23
        mn = 59
        sec = 59
        msec = 999

        timestamp = time.mktime(datetime.datetime(yr, mnth, dt, hr, mn, sec, msec).timetuple())
        return timestamp

def getDateWithoutTime(num):
        p = time.ctime(int(float(num)))
        s = str(datetime.datetime.fromtimestamp(int(float(num)))).split(' ')[0]
        s = s.split('-')
        year = s[0]
        month = s[1]
        dt = s[2]
        return dt+" - "+month+" - "+year

def getCurrentStartDate():
    d = str(datetime.datetime.now())
    d = d.split(' ')
    lst = d[0]

    lst = lst.split('-')

    _year = int(lst[0])
    _month = int(lst[1])
    _date = int(lst[2])
    hours = 0
    minuts = 0
    seconds = 0
    mseconds = 0

    return time.mktime(datetime.datetime(_year, _month, _date, hours, minuts, seconds, mseconds).timetuple())

def getCurrentEndDate():
    d = str(datetime.datetime.now())
    d = d.split(' ')
    lst = d[0]

    lst = lst.split('-')

    _year = int(lst[0])
    _month = int(lst[1])
    _date = int(lst[2])
    hours = 23
    minuts = 59
    seconds = 59
    mseconds = 0
    return time.mktime(datetime.datetime(_year, _month, _date, hours, minuts, seconds, mseconds).timetuple())

##This function returns number for last year
'''
This function takes current date in string form
seprated by quomas, and returns a tuple
consisting of start and end numbers for last year
i.e:
input: 25 11 2018
output: (startNum,endNum)

'''
def getLastYearNumbers(date):
        lst = date.split(' ')
        mnth = 1
        dt = 1
        yr = int(lst[3])-1
        hr = 0
        mn = 0
        sec = 0
        msec = 0
        lastYearStart = time.mktime(datetime.datetime(yr, mnth, dt, hr, mn, sec, msec).timetuple())

        mnth = 12
        dt = 31
        lastYearEnd = time.mktime(datetime.datetime(yr, mnth, dt, hr, mn, sec, msec).timetuple())
        dates = Tuple()
        dates = (lastYearStart,lastYearEnd)
        return dates
    
