import uuid,re

def getMac():
    mac = uuid.getnode()
    return ('-'.join(re.findall('..', '%012x' % uuid.getnode())))