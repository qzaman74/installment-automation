from Services.DBService import DBConnection
from Globals import globalVariables
from Services.MiscService import dateTime


def insertSaleToDB(saleId, billId, accountId, companyId, purchaseId, quantity, salePrice, discount, totalPrice, remarks, createdBy):

    connection = DBConnection.DBConnectivity._connection
    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'

    qry = "INSERT INTO sale VALUES( "+str(saleId)+", "+str(billId)+", "+str(accountId)+", "+str(companyId)+", " \
                                    ""+str(purchaseId)+", "+str(quantity)+", "+str(salePrice)+", "+str(discount)+", " \
                                    ""+str(totalPrice)+", '"+str(remarks)+"', "+str(createdBy)+", '"+str(createdOn)+"', " \
                                    "'"+str(updatedOn)+"', '"+str(deletedOn)+"',  "+str(isDeleted)+" )"

    # print("sale: " + qry)
    connection.execute(qry)
    connection.commit()

def getSaleByInvoice(invoice, billType):
	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT  c.name, pro.name,  pur.engine, pur.chassis, s.sale_price, s.discount, s.total_price, s.remarks " \
          "FROM sale s, bill b, company c, product pro , purchase pur " \
          "WHERE s.is_deleted=0 AND b.type='"+str(billType)+"' AND s.bill_id=b.bill_id AND s.purchase_id=pur.purchase_id " \
            "AND pur.company_id=c.company_id AND pur.product_id=pro.product_id AND b.bill_id="+str(invoice)+" "
	result = connection.execute(qry)
	return result
