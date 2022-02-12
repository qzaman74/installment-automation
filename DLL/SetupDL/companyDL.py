from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertCompany(companyid, name, code, representative, contact, location,  image, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO company VALUES( "+str(companyid)+", '"+str(name)+"', '"+str(code)+"', '"+str(representative)+"'," \
                                        " '"+str(contact)+"', '"+str(location)+"', "+str(image)+", "+str(createdBy)+", " \
                                        "'"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', '"+str(isDeleted)+"' )"
    connection.execute(qry)
    connection.commit()
    notification.showRight("Company Saved Successfully",'Success !')

def getCompanyFromDB():
    connection = DBConnection.DBConnectivity._connection
    query = "SELECT company_id, name, code, representative, contact, location FROM company WHERE is_deleted=0"
    result = connection.execute(query)
    return result

def getCompanyByID(companyId):
    connection = DBConnection.DBConnectivity._connection
    query = "SELECT company_id, name, code, representative, contact, location " \
            "FROM company " \
            "WHERE is_deleted=0 AND company_id="+str(companyId)+""
    result = connection.execute(query)
    return result.fetchall()

def updateCompany(companyId, name, code, agent, contact, location, image, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE company SET '

    if (name != ''):
        qry = qry + 'name = "' + str(name) + '", '
    if (code != ''):
        qry = qry + 'code = "' + str(code) + '", '
    if (agent != ''):
        qry = qry + 'representative = "' + str(agent) + '", '
    if (contact != ''):
        qry = qry + 'contact = "' + str(contact) + '", '
    if (location != ''):
        qry = qry + 'location = "' + str(location) + '", '
    if (image != ''):
        qry = qry + 'image = "' + str(image) + '", '
    if (int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if (int(isDeleted) == 0):
        qry = qry + 'updated_on = "' + globalVariables.Variables._createdOn + '", '

    qry = qry + 'is_deleted = ' + str(isDeleted) + ' '
    qry = qry + ' WHERE company_id = ' + str(companyId) + ''


    connection.execute(qry)
    connection.commit()

