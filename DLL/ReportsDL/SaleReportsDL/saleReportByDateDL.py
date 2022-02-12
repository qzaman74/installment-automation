from Services.DBService import DBConnection

from Services.MiscService import dateTime


def getSaleReportByDates(startDate, endDate):

	sDate = dateTime.getStartDateWithoutTimes(str(startDate))
	eDate = dateTime.getEndDateWithoutTimes(str(endDate))

	connection = DBConnection.DBConnectivity._connection
	qry = "SELECT b.bill_id, b.date,  a.name, a.mobile_no, c.name, pro.name, pur.engine, pur.chassis, " \
          " pur.sale_price, b.amount,b.discount,b.net_amount, s.remarks " \
          "FROM bill b, sale s, account a, purchase pur, company c, product pro " \
          "WHERE b.bill_id=s.bill_id AND s.account_id=a.account_id AND s.purchase_id=pur.purchase_id " \
          "AND pur.company_id=c.company_id AND pur.product_id=pro.product_id AND b.type='SALE' " \
          "AND b.created_on > '"+str(sDate)+"' AND b.created_on < '"+str(eDate)+"' "

	result = connection.execute(qry)
	return result