from datetime import datetime
import random
import string
import subprocess
from config import *

def torRequest():
    dateBefore = datetime.utcnow()
    circuitId = ''.join(random.choices(string.digits, k=6))
    CurlUrl="curl --socks5-hostname "+str(circuitId)+"@localhost:9050 " + (urlClear if clearnet else urlTor)
    res = subprocess.getstatusoutput(CurlUrl)
    duration = datetime.utcnow() - dateBefore
    return (duration, res)
                
def setExitNodes(exitNodes):
    exitNodeStr = ""
    for exitNode in exitNodes:
        exitNodeStr = exitNodeStr + exitNode + ","
    if len(exitNodeStr) > 1:
        exitNodeStr = exitNodeStr[:-1]
    
    return subprocess.call(torControlScript + " setconf ExitNodes="+str(exitNode) + " > /dev/null",shell=True)

def setCircuitBuildTimeout():
    return subprocess.call(torControlScript + " setconf CircuitBuildTimeout="+str(circuitBuildTimeout) + " > /dev/null",shell=True)