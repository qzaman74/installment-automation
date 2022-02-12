from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertInstallmentLog(installmentLogId, customerSchemeId, date, amount, balance, remarks, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO installment_log VALUES( "+str(installmentLogId)+", "+str(customerSchemeId)+", '"+str(date)+"', " \
                                                ""+str(amount)+", "+str(balance)+", '"+str(remarks)+"', "+str(createdBy)+"," \
                                                " '"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', " \
                                                "'"+str(isDeleted)+"' )"

    connection.execute(qry)
    connection.commit()
    notification.showRight("Scheme Assigned Successfully",'Success !')


def getInstallmentHistoryFromDB(accountId, customerSchemeId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT il.date, il.amount, il.balance, il.remarks " \
          "FROM scheme s, customer_scheme cs, installment_log il " \
          "WHERE s.scheme_id=cs.scheme_id AND cs.customer_scheme_id=il.customer_scheme_id " \
          "AND cs.customer_scheme_id="+str(customerSchemeId)+" AND cs.account_id="+str(accountId)+" "
    result = connection.execute(qry)
    result = result.fetchall()
    return result