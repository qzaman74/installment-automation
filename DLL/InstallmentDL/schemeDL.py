from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertScheme(schemeId, name, startDate,endDate,dueDate,installments, amount,remarks, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO scheme VALUES( "+str(schemeId)+", '"+str(name)+"', '"+str(startDate)+"', '"+str(endDate)+"'," \
                                   " '"+str(dueDate)+"', "+str(installments)+", "+str(amount)+", '"+str(remarks)+"'," \
                                  " "+str(createdBy)+", '"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"'," \
                                  " '"+str(isDeleted)+"' )"

    connection.execute(qry)
    connection.commit()
    notification.showRight("Scheme Added Successfully",'Success !')


def getAllSchemesFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT scheme_id, name, start_date, end_date, due_date, installments, amount, remarks " \
          "FROM scheme WHERE is_deleted=0"
    result = connection.execute(qry)
    return result

def getSchemeData(schemeID):
    connection = DBConnection.DBConnectivity._connection
    query = "SELECT scheme_id, name, start_date, end_date, due_date, installments, amount, remarks " \
            "FROM scheme " \
            "WHERE is_deleted=0 AND scheme_id =?"
    result = connection.execute(query,(schemeID,))
    result = result.fetchall()
    return result


def getSchemeDataByCSID(customerSchemeID):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT s.installments, s.amount " \
          "FROM scheme s, customer_scheme cs " \
          "WHERE s.scheme_id=cs.scheme_id AND cs.customer_scheme_id="+str(customerSchemeID)+" "
    result = connection.execute(qry)
    result = result.fetchall()
    return result


def updateScheme(schemeId, name, startDate, endDate, dueDate, installments, amount, remarks, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE scheme SET '

    if(name != ''):
        qry = qry + 'name = "'+str(name)+'", '
    if(startDate != ''):
        qry = qry + 'start_date = "'+str(startDate)+'", '
    if(endDate != ''):
        qry = qry + 'end_date = "'+str(endDate)+'", '
    if(dueDate != ''):
        qry = qry + 'due_date = "'+str(dueDate)+'", '
    if(installments != ''):
        qry = qry + 'installments = "'+str(installments)+'", '
    if(amount != ''):
        qry = qry + 'amount = "'+str(amount)+'", '
    if(remarks != ''):
        qry = qry + 'remarks = "'+str(remarks)+'", '

    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE scheme_id = '+str(schemeId)+''

    connection.execute(qry)
    connection.commit()
    notification.showRight("Changes Done Successfully","Success !")