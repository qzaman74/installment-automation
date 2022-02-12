
from Services.DBService import DBConnection
from Services.NotificationService import notification
from Globals import globalVariables

def getExpiryFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT expiry_date FROM expiry WHERE id=1 "
    result = connection.execute(qry)
    return result.fetchone()