from Services.DBService import DBConnection

def getStockLevelFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT c.name, pr.name, sum(pu.quantity_log) as stock " \
          "FROM purchase pu, product pr, company c " \
          "WHERE pu.company_id=c.company_id AND pu.product_id=pr.product_id GROUP BY pr.product_id"

    result = connection.execute(qry)
    return result
