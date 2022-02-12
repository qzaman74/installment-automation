from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertAssignScheme(assignSchemeId, schemeId, accountId, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO customer_scheme VALUES( "+str(assignSchemeId)+", "+str(schemeId)+", "+str(accountId)+", " \
                                        ""+str(createdBy)+", '"+str(createdOn)+"', '"+str(updatedOn)+"'," \
                                        " '"+str(deletedOn)+"', '"+str(isDeleted)+"' )"

    connection.execute(qry)
    connection.commit()
    notification.showRight("Scheme Assigned Successfully",'Success !')

def getAllAssignedSchemesById(accountId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT s.scheme_id, s.name, s.start_date, s.end_date, s.due_date, s.installments, s.amount, s.remarks " \
          "FROM scheme s, customer_scheme cs " \
          "WHERE s.is_deleted=0 AND s.scheme_id=cs.scheme_id AND cs.account_id="+str(accountId)+" GROUP BY cs.customer_scheme_id "
    result = connection.execute(qry)
    result = result.fetchall()
    return result


def getAssignedSchemesById(accountId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT cs.customer_scheme_id, s.name " \
          "FROM scheme s, customer_scheme cs " \
          "WHERE s.scheme_id=cs.scheme_id AND cs.account_id="+str(accountId)+" "
    result = connection.execute(qry)
    return result
