from Services.DBService import DBConnection
from Globals import globalVariables

def updateActivationKey(expiryDate):
    connection = DBConnection.DBConnectivity._connection
    qry = "UPDATE expiry SET " \
          "expiry_date = '"+str(expiryDate)+"',  " \
          "updated_on = "+str(globalVariables.Variables._createdOn)+"  " \
          "WHERE id = 1  "

    connection.execute(qry)
    connection.commit()