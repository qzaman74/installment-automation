from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables


def insertPurchaseToDB(purchaseId, billId, accountId, companyId, productId, productType, engine, chassis, registration,
                       costPrice, salePrice, discount, totalPrice, quantityLog, remarks, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO purchase VALUES( "+str(purchaseId)+", "+str(billId)+", "+str(accountId)+", "+str(companyId)+", " \
                                       ""+str(productId)+", '"+str(productType)+"', '"+str(engine)+"', '"+str(chassis)+"'," \
                                       "'"+str(registration)+"', "+str(costPrice)+",  "+str(salePrice)+", "+str(discount)+", " \
                                      ""+str(totalPrice)+", "+str(quantityLog)+", '"+str(remarks)+"', "+str(createdBy)+", " \
                                       "'"+str(createdOn)+"', '"+str(updatedOn)+"', '"+str(deletedOn)+"', '"+str(isDeleted)+"' )"

    connection.execute(qry)
    connection.commit()

def updatePurchase(purchaseId, billId, accountId, companyId, productId, engine, chassis, costPrice, salePrice, discount,
                   totalPrice,quantityLog, remarks,isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE purchase SET '

    if(engine != ''):
        qry = qry + 'engine = "'+str(engine)+'", '
    if(chassis != ''):
        qry = qry + 'chassis = "'+str(chassis)+'", '
    if(costPrice != ''):
        qry = qry + 'cost_price = '+str(costPrice)+', '
    if(salePrice != ''):
        qry = qry + 'sale_price = '+str(salePrice)+', '
    if(discount != ''):
        qry = qry + 'discount = '+str(discount)+', '
    if(totalPrice != ''):
        qry = qry + 'total_price = '+str(totalPrice)+', '
    if(quantityLog != ''):
        qry = qry + 'quantity_log = '+str(quantityLog)+', '
    if(remarks != ''):
        qry = qry + 'remarks = "'+str(remarks)+'", '

    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE purchase_id = '+str(purchaseId)+''


    # print("update purchase: " + qry)
    connection.execute(qry)
    connection.commit()


def getPurchaseByProductID(productId,productType):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT purchase_id, engine, chassis, registration " \
          "FROM purchase " \
          "WHERE is_deleted=0 AND quantity_log!=0 AND product_id="+str(productId)+" AND type='"+str(productType)+"' GROUP BY purchase_id "

    result = connection.execute(qry)
    return result

def getPurchaseByPurchaseID(purchaseId):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT purchase_id, engine, chassis, registration, sale_price " \
          "FROM purchase " \
          "WHERE is_deleted=0 AND quantity_log!=0 AND purchase_id="+str(purchaseId)+" "

    result = connection.execute(qry)
    return result


def getPurchaseByInvoice(invoice, billType):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT  c.name, pro.name, pur.engine, pur.chassis, pur.cost_price, pur.sale_price, " \
          "pur.discount, pur.total_price, pur.remarks " \
          "FROM bill b, company c, product pro , purchase pur " \
          "WHERE pur.is_deleted=0 AND b.type='"+str(billType)+"' AND b.bill_id=pur.bill_id AND pur.company_id=c.company_id " \
          "AND pur.product_id=pro.product_id AND b.manual_invoice_no="+str(invoice)+" "

    result = connection.execute(qry)
    return result


def getCurrentPurchase():
    pass