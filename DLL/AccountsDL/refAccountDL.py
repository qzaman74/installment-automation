from Services.DBService import DBConnection
from Services.NotificationService import notification
from Services.ImgService import image
from Globals import globalVariables

def insertRefAccountToDB(refAccountId, name, fatherName, cnic, mobileNo,  gender, address, image, createdBy):
    connection = DBConnection.DBConnectivity._connection

    createdOn = globalVariables.Variables._createdOn
    updatedOn = '0'
    deletedOn = '0'
    isDeleted = 0
    qry = "INSERT INTO ref_account VALUES( "+str(refAccountId)+", '"+str(name)+"', '"+str(fatherName)+"'," \
                                        " '"+str(cnic)+"', '"+str(mobileNo)+"', '"+str(gender)+"', '"+str(address)+"', " \
                                        "'"+str(image)+"', "+str(createdBy)+", '"+str(createdOn)+"', " \
                                        "'"+str(updatedOn)+"', '"+str(deletedOn)+"', "+str(isDeleted)+" )"

    connection.execute(qry)
    connection.commit()
    notification.showInformative("Referemce Account Saved Successfully",'Success !')



def updateRefAccount(refAccountId, name, fatherName, cnic, mobileNo,  gender, address, isDeleted):
    connection = DBConnection.DBConnectivity._connection

    qry = ' UPDATE ref_account SET '

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
    if(int(isDeleted) == 1):
        qry = qry + 'deleted_on = "' + globalVariables.Variables._createdOn + '", '

    if(int(isDeleted) == 0):
        qry = qry + 'updated_on = "'+globalVariables.Variables._createdOn +'", '

    qry = qry + 'is_deleted = '+str(isDeleted)+' '
    qry = qry + ' WHERE ref_account_id = '+str(refAccountId)+''

    connection.execute(qry)
    connection.commit()



def getAllRefAccounts():
    connection = DBConnection.DBConnectivity._connection

    qry = "SELECT ref_account_id, name, father_name, cnic, mobile_no, gender, address " \
          "FROM ref_account " \
          "WHERE is_deleted=0 "
    result = connection.execute(qry)
    return result