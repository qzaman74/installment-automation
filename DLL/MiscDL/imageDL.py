from Services.DBService import DBConnection
from Services.ImgService import image


def insertImage(imageId, image):
    connection = DBConnection.DBConnectivity._connection
    qry = 'INSERT INTO image VALUES('+str(imageId)+', "'+str(image)+'" )'
    print(qry)
    connection.execute(qry)
    connection.commit()