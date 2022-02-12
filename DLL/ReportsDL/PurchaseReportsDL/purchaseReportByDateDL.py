from Services.MiscService import dateTime
from Services.DBService import DBConnection

def getPurchasesReportByDates(startDate, endDate):

	sDate = dateTime.getStartDateWithoutTimes(str(startDate))
	eDate = dateTime.getEndDateWithoutTimes(str(endDate))

	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT b.manual_invoice_no, b.date,  a.name, a.mobile_no, c.name, pro.name, pur.engine, " \
		  "pur.chassis, pur.cost_price, pur.sale_price, pur.discount, pur.total_price, pur.remarks " \
		  "FROM bill b, purchase pur, account a, company c, product pro " \
		  "WHERE b.bill_id=pur.bill_id AND pur.account_id=a.account_id AND pur.company_id=c.company_id " \
		  "AND pur.product_id=pro.product_id AND b.type='PURCHASE' " \
		  "AND b.created_on > '"+str(sDate)+"' AND b.created_on < '"+str(eDate)+"' "



	result = connection.execute(qry)
	return result
