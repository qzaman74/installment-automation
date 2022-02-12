import sqlite3
from Globals import config

class DBConnectivity:
    _connection = sqlite3.connect(config.Config._dbPath)
    # _commit = _connection.commit()
    # _close = _connection.close()