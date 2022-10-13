
from phase import Phase

# Tor
clearnet = False
circuitBuildTimeout = 0
exitNodesSubset = ["45.141.215.92", "185.220.103.117", "45.66.35.35"]

sampleNbRounds = 10
# these are cpu/network bound
# total nb of circuit creation and requests per phase = nbClientsInRound * nbInputsPerClient * concurrentFallbackRequests
nbClientsInRound = 5
nbInputsPerClient = 8
concurrentFallbackRequests = 1 # similar request sent at the same time, after first complete other cancel

# {phase_name, phase_duration_s}
phases = {
    Phase.InputRegistration: 30,
	Phase.ConnectionConfirmation : 30,
	Phase.OutputRegistration : 30,
	Phase.TransactionSigning : 30,
	Phase.Ended : 0,
}

torControlScript = "./torcontrol.sh"
urlClear = "https://wasabiwallet.io/WabiSabi/human-monitor"
#urlClear = "https://api.ipify.org/"
urlTor = "http://wasabiukrxmkdgve5kynjztuovbg43uxcbcxn6y2okcrsg7gb6jdmbad.onion/WabiSabi/human-monitor"