from Globals import globalVariables
from Services.MiscService import dateTime

def gernateKey():
    cd = dateTime.getDateWithoutTime(globalVariables.Variables._createdOn) #float(globalVariables.Variables._createdOn) #current date time stamp
    # cd = dateTime.getDateWithoutTime(globalVariables.Variables._createdOn) #current date in string format
    dt = input("Enter date: ")
    dt = dateTime.getKeyTimeStamp(dt)
    # print(dt)

    #current date in seprate parts
    lst = cd.split('-')
    month = int(lst[1])

    key = int(dt)
    mnth = dateTime.getMonthByNumber(month)
    key = str(key)
    key = mnth[0] + str(key[:4]) + mnth[1] + str(key[4:]) + mnth[2]
    # print(key)
    decodeKey(key)


def decodeKey(key):
    currentDate = dateTime.getDateWithoutTime(globalVariables.Variables._createdOn)
    lst = currentDate.split('-')
    year = int(lst[2])
    # key = int(key) + 9999
    key = str(key)
    # print(key)
    key2 = "" #key without chracter values
    for ch in key:
        if(ch.isalpha() != True):
            key2 += ch
    #print(key2)
    # key2 = int(float(key2))

    # print(dateTime.getDateWithoutTime(key2))
    return float(key2)