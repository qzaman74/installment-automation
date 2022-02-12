from Services.DBService import DBConnection
from Globals import globalVariables


def insertTransectionToDB(transectionId, accountId, billId, billType,transectionType,dr,cr,balance,remarks,createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO transection VALUES( "+str(transectionId)+", "+str(accountId)+", "+str(billId)+", '"+str(billType)+"'," \
                                  "'"+str(transectionType)+"', "+str(dr)+","+str(cr)+", "+str(balance)+", " \
                                "'"+str(remarks)+"', "+str(createdBy)+", '"+str(createdOn)+"', '"+str(updatedOn)+"', " \
                                "'"+str(deletedOn)+"', '"+str(isDeleted)+"' )"


    # print("trans: " + qry)
    connection.execute(qry)
    connection.commit()

def getTransetionByAccountId(accountId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT a.name,a.mobile_no, t.type,t.dr, t.cr, t.balance,t.remarks " \
          "FROM account a, transection t " \
          "WHERE a.account_id=t.account_id AND t.account_id="+str(accountId)+""
    result = connection.execute(qry)
    return result

def getCurrentCashIn(startDate, endDate):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT sum(dr) " \
          "FROM transection " \
          "WHERE type = 'DEPOSIT' AND created_on>"+str(startDate)+" AND created_on <"+str(endDate)+" AND account_id=1"
    result = connection.execute(qry)
    return result.fetchone()[0]

def getCurrentCashOut(startDate, endDate):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT sum(cr) " \
          "FROM transection " \
          "WHERE type = 'WITHDRAWAL' AND created_on>"+str(startDate)+" AND created_on <"+str(endDate)+" AND account_id=1"
    result = connection.execute(qry)
    return result.fetchone()[0]