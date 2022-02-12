from Services.DBService import DBConnection

def getPurchasesReportByInvoive(invoice):
	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT b.date, ac.name, c.name, pro.name, p.combine_quantity, p.combine_unit, " \
            "p.single_quantity, p.single_unit, p.cost_price, p.sale_price, p.discount, p.total_price " \
            "FROM purchase p, bill b, account ac, company c, product pro " \
            "WHERE p.is_deleted=0 AND p.bill_id=b.bill_id AND p.supplier_id=ac.account_id AND p.company_id=c.company_id " \
            "AND p.product_id=pro.product_id AND b.type='purchase' AND b.manual_invoice_no="+str(invoice)+" "
	result = connection.execute(qry)
	return result

def getTotalBill(invoice):
	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT amount, discount, net_amount " \
		  "FROM bill " \
		  "WHERE is_deleted=0 AND type='purchase' " \
          "AND manual_invoice_no="+str(invoice)+" "
	result = connection.execute(qry)
	return result