from Services.DBService import DBConnection
from Services.MiscService import dateTime
from Globals import globalVariables


def insertPolicyToDB(policyId, billId, policyType, dueDate, amount, balance, isPaid, createdBy):

    connection = DBConnection.DBConnectivity._connection
    date = dateTime.getStartDateWithoutTimes(dueDate)
    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO policy VALUES( "+str(policyId)+", "+str(billId)+", '"+str(policyType)+"'," \
                                    "'"+str(date)+"', "+str(amount)+", "+str(balance)+", "+str(isPaid)+", " \
                                    ""+str(createdBy)+",'"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', " \
                                    "'"+str(isDeleted)+"' )"
    connection.execute(qry)
    connection.commit()


def updatePolicy(policyId, purchaseId, saleId, policyType, dueDate, amount, balance, isPaid, createdBy, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE policy SET '

    if(isPaid != 1):
        qry = qry + 'is_paid = '+str(isPaid)+', '

    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE policy_id = '+str(policyId)+''

    connection.execute(qry)
    connection.commit()
