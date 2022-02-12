from Services.DBService import DBConnection
from Services.MiscService import dateTime
from Globals import globalVariables


def insertPaymentToDB(paymentId, billId, paymentType, date, amount, balance, remarks, createdBy):
    connection = DBConnection.DBConnectivity._connection
    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO payment_log VALUES( "+str(paymentId)+", "+str(billId)+", '"+str(paymentType)+"'," \
                                    "'"+str(date)+"', "+str(amount)+", "+str(balance)+", '"+str(remarks)+"', " \
                                    ""+str(createdBy)+", '"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', " \
                                    "'"+str(isDeleted)+"' )"
    connection.execute(qry)
    connection.commit()



def getPaymentLogByBillId(billId):
    connection = DBConnection.DBConnectivity._connection

    qry = "SELECT date, amount, balance, remarks FROM payment_log WHERE bill_id="+str(billId)+" "

    result = connection.execute(qry)
    return result

