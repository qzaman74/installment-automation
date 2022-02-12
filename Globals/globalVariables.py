import time, datetime


class Variables:



    _companyName ='SALAH UD DIN TRADERS'
    _compnayAddress = 'JINAH COLONY BAHAWALNAGAR'
    _compnayMobile = '03347273602'



    _userId = str(0)

    _createdOn = str(time.mktime(datetime.datetime.now().timetuple()))
    _calendarMaxDate = datetime.datetime.now()

    _style = "Style/default.qss"
    _icon = 'Assets/icon/'

    _male = 'MALE'
    _female = 'FEMALE'

    _cashTransectionBillType = 'CASH TRANSECTION'

    _withDrawal = 'WITHDRAWAL'
    _deposit = 'DEPOSIT'

    _receivable ='RECEIVABLE'
    _payable = 'PAYABLE'

    _sale = 'SALE'
    _purchase = 'PURCHASE'

    _net = 'NET'
    _shortTerm = 'SHORTTERM'
    _lease = 'LEASE'

    _newProduct = 'NEW'
    _usedProduct = 'USED'


    _currentSale = 0
    _currentPurchase = 0
    _cashIn = 0
    _cashOut = 0



