from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertProduct(productId, companyId, productType, name, code, remarks, image, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO product VALUES( "+str(productId)+", "+str(companyId)+", '"+str(productType)+"', '"+str(name)+"', '"+str(code)+"', '"+str(remarks)+"', "+str(image)+", "+str(createdBy)+", '"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', '"+str(isDeleted)+"' )"
    connection.execute(qry)
    connection.commit()
    notification.showRight("Product Saved Successfully",'Success !')

def updateProduct(productId, companyId, productType, productName, productCode, remarks, imageCode, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE product SET '

    if (companyId != ''):
        qry = qry + 'company_id = "' + str(companyId) + '", '
    if (productType != ''):
        qry = qry + 'type = "' + str(productType) + '", '
    if (productName != ''):
        qry = qry + 'name = "' + str(productName) + '", '
    if (productCode != ''):
        qry = qry + 'code = "' + str(productCode) + '", '
    if (remarks != ''):
        qry = qry + 'remarks = "' + str(remarks) + '", '
    if (imageCode != ''):
        qry = qry + 'image = '+str(imageCode)+', '

    if (int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if (int(isDeleted) == 0):
        qry = qry + 'updated_on = "' + globalVariables.Variables._createdOn + '", '

    qry = qry + 'is_deleted = ' + str(isDeleted) + ' '
    qry = qry + ' WHERE product_id = ' + str(productId) + ''

    connection.execute(qry)
    connection.commit()
    notification.showRight("Changes Done Successfully", "Success !")


def getProductFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT p.product_id, c.name, p.type, p.name, p.code, p.remarks " \
            "FROM product p, company c " \
            "WHERE p.company_id=c.company_id AND p.is_deleted=0"
    result = connection.execute(qry)
    return result

def getProductByCompanyIDFromDB(companyId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT p.product_id, p.company_id, p.type, p.name, p.code, p.remarks " \
          "FROM product p, company c " \
          "WHERE p.company_id=c.company_id AND p.is_deleted=0 AND p.company_id="+str(companyId)+" GROUP By p.product_id"
    result = connection.execute(qry)
    return result


def getProductByProductID(productId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT p.product_id, c.name, p.type, p.name, p.code, p.remarks, p.image " \
          "FROM product p, company c " \
          "WHERE p.company_id=c.company_id AND p.is_deleted=0 AND p.product_id="+str(productId)+" GROUP By p.product_id"
    result = connection.execute(qry)
    return result