from Services.DBService import DBConnection
from Services.NotificationService import notification
from Services.ImgService import image
from Globals import globalVariables


def insertAccountToDB(accountId, name, fatherName, cnic, mobileNo,  gender, address, accountType, accountStatus, balance, image, createdBy):
    connection = DBConnection.DBConnectivity._connection

    userName =  '0'
    password = '0'
    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = '0'
    qry = "INSERT INTO account VALUES( "+str(accountId)+", '"+str(name)+"', '"+str(fatherName)+"', '"+str(userName)+"'," \
                                        " '"+str(cnic)+"', '"+str(mobileNo)+"', '"+str(gender)+"', '"+str(address)+"', " \
                                        "'"+str(password)+"', '"+str(accountType)+"','"+str(accountStatus)+"', " \
                                        ""+str(balance)+", '"+image+"', "+str(createdBy)+", '"+str(createdOn)+"', " \
                                        "'"+str(updatedOn)+"', '"+str(deletedOn)+"', '"+str(isDeleted)+"' )"


    connection.execute(qry)
    connection.commit()
    notification.showInformative("Account Saved Successfully",'Successfully !')




def getAllAccountsFromDB():
    connection = DBConnection.DBConnectivity._connection
    query = "SELECT account_id, name, father_name, cnic, mobile_no, address, type, status, balance FROM account WHERE is_deleted=0"
    result = connection.execute(query)
    return result


def getAccountImage(accountID):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT image FROM account  WHERE account_id ="+str(accountID)+""
    result = connection.execute(qry)
    data = result.fetchone()[0]
    basimg = image.getPixmap(data)
    return basimg




def getAccountData(accountID):
    connection = DBConnection.DBConnectivity._connection
    query = "SELECT account_id, name, father_name, user_name, cnic, mobile_no, gender, address, password," \
            " type, status, balance FROM account WHERE is_deleted=0 AND account_id =?"
    result = connection.execute(query,(accountID,))
    result = result.fetchall()
    return result


def updateAccount(accountId, name, fatherName, cnic, mobileNo,  gender, address, accountType, accountStatus, balance,isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE account SET '

    if(name != ''):
        qry = qry + 'name = "'+str(name)+'", '
    if(fatherName != ''):
        qry = qry + 'father_name = "'+str(fatherName)+'", '
    if(cnic != ''):
        qry = qry + 'cnic = "'+str(cnic)+'", '
    if(mobileNo != ''):
        qry = qry + 'mobile_no = "'+str(mobileNo)+'", '
    if(gender != ''):
        qry = qry + 'gender = "'+str(gender)+'", '
    if(address != ''):
        qry = qry + 'address = "'+str(address)+'", '
    if(accountType != ''):
        qry = qry + 'type = "'+str(accountType)+'", '
    if(accountStatus != ''):
        qry = qry + 'status = "'+str(accountStatus)+'", '
    if(balance != ''):
        qry = qry + 'balance = '+str(balance)+', '
    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE account_id = '+str(accountId)+''

    # print("update account: " + qry)
    connection.execute(qry)
    connection.commit()


def getAccountByTypeFromDB(accountType):
    connection = DBConnection.DBConnectivity._connection
    qry = "SELECT account_id, name, mobile_no FROM account WHERE is_deleted='0' AND  type='"+str(accountType)+"' "
    result = connection.execute(qry)
    return result


def getAccountsReceivableFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = " SELECT name, father_name, cnic, mobile_no, gender, address, type, status, balance " \
          "FROM account " \
          "WHERE balance > 0 AND account_id != 1 "
    result = connection.execute(qry)
    return result

def getAccountsPayableFromDB():
    connection = DBConnection.DBConnectivity._connection
    qry = " SELECT name, father_name, cnic, mobile_no, gender, address, type, status, balance " \
          "FROM account " \
          "WHERE balance < 0 AND account_id != 1 "
    result = connection.execute(qry)
    return result