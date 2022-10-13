
from config import exitNodesSubset
from client import performTestAsync
from tor import setCircuitBuildTimeout, setExitNodes

# main
setCircuitBuildTimeout()
setExitNodes(exitNodesSubset)

results = performTestAsync()
pass
