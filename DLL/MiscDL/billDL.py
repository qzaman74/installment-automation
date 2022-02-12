from Services.DBService import DBConnection
from Services.MiscService import dateTime
from Globals import globalVariables


def insertBillToDB(billId, accountId,refAccountId, date, dueDate,endDate, manualInvoiceNo, billType,isInstallment,
                   amount, discount, netAmount, payment, balance, remarks, image, createdBy):
    connection = DBConnection.DBConnectivity._connection
    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO bill VALUES( "+str(billId)+", "+str(accountId)+", "+str(refAccountId)+", '"+str(date)+"'," \
                                    "'"+str(dueDate)+"','"+str(endDate)+"', '"+str(manualInvoiceNo)+"', " \
                                    "'"+str(billType)+"', "+str(isInstallment)+", "+str(amount)+", "+str(discount)+",  "+str(netAmount)+", " \
                                    ""+str(payment)+", "+str(balance)+", '"+str(remarks)+"',"+str(image)+", "+str(createdBy)+"," \
                                    "'"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', " \
                                    "'"+str(isDeleted)+"' )"
    connection.execute(qry)
    connection.commit()


def updateBill(billId, accountId, refAccountId, date, dueDate, endDate,  manualInvoiceNo, _type, isInstallment, amount, discount, netAmount, payment, balance, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE bill SET '

    if(payment != ''):
        qry = qry + 'payment = '+str(payment)+', '
    if(balance != ''):
        qry = qry + 'balance = '+str(balance)+', '

    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE bill_id = '+str(billId)+''

    connection.execute(qry)
    connection.commit()




def getBillByAccountID(accountId,billType):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT bill_id, account_id, date, manual_invoice_no, type, amount, discount, net_amount, payment, balance, remarks " \
            "FROM bill " \
            "WHERE is_deleted=0 AND type='"+str(billType)+"' AND account_id="+str(accountId)+" "
    result = connection.execute(qry)
    return result

def getMaxBillId():
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT MAX(bill_id)+1 FROM bill "
    result = connection.execute(qry)
    result = result.fetchone()
    return result


def getBillByInvoice(invoice, billType):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT a.name, a.father_name, a.cnic, a.mobile_no, b.amount, b.discount, " \
          "b.net_amount, b.balance,b.created_on  " \
          "FROM bill b, account a WHERE b.is_deleted=0 AND b.account_id=a.account_id " \
          "AND b.is_deleted=0 AND b.type='"+str(billType)+"' "

    if(billType == globalVariables.Variables._sale):
        qry = qry +"AND b.bill_id="+str(invoice)+" "

    if(billType == globalVariables.Variables._purchase):
        qry = qry +"AND b.manual_invoice_no="+str(invoice)+" "

    result = connection.execute(qry)
    return result

def getCurrentBill(billType, startDate, endData):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT sum(net_amount) " \
          "FROM bill " \
          "WHERE type = '"+str(billType)+"' AND created_on>"+str(startDate)+" AND created_on <"+str(endData)+" "
    result = connection.execute(qry)
    return result.fetchone()[0]



def getSaleItemByAccountId(accountId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT b.bill_id, c.name, pro.name " \
          "FROM account a, bill b, sale s, purchase pur, company c, product pro " \
          "WHERE a.account_id=b.account_id AND b.bill_id=s.bill_id AND s.purchase_id=pur.purchase_id AND " \
          "pur.company_id=c.company_id AND pur.product_id=pro.product_id AND b.type='SALE' AND b.is_installment=1 AND " \
          "b.balance>0 AND b.account_id="+str(accountId)+" GROUP BY b.bill_id"

    result = connection.execute(qry)
    return result


def getItemDetailById(billId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT bill_id, account_id, date, due_date, end_date, manual_invoice_no, type, is_installment, amount, discount, net_amount, payment, balance, remarks " \
            "FROM bill " \
            "WHERE is_deleted=0 AND bill_id="+str(billId)+" "

    result = connection.execute(qry)
    return result

def getBillByDate(startDate, endDate, billType):
    sDate = dateTime.getStartDateWithoutTimes(startDate)
    eDate = dateTime.getEndDateWithoutTimes(endDate)

    connection = DBConnection.DBConnectivity._connection

    qry = "SELECT SUM(amount), SUM(discount), SUM(net_amount) " \
          "FROM bill " \
          "WHERE is_deleted=0 AND type='"+str(billType)+"' " \
          "AND created_on > '"+str(sDate)+"' AND created_on < '"+str(eDate)+"' "

    result = connection.execute(qry)
    return result