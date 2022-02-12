from Services.DBService import DBConnection

def getSaleReportByInvoive(invoice):
	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT b.date, ac.name, c.name, pro.name, s.quantity, s.sale_price, s.discount, s.total_price " \
          "FROM sale s, bill b, account ac, company c, product pro , purchase pur WHERE s.is_deleted=0 " \
          "AND b.type='SALE' AND s.bill_id=b.bill_id AND s.account_id=ac.account_id AND s.company_id=c.company_id " \
          "AND s.purchase_id=pur.purchase_id AND pur.product_id= pro.product_id AND s.bill_id="+invoice+" " \
          "GROUP By s.sale_id "
	result = connection.execute(qry)
	return result

def getTotalBill(invoice):
	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT amount, discount, net_amount " \
		  "FROM bill " \
		  "WHERE is_deleted=0 AND type='SALE' " \
          "AND bill_id="+str(invoice)+" "
	result = connection.execute(qry)
	return result