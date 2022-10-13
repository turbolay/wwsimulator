## WWSimulaTOR

Basic simulation of a WabiSabi making test request through new tor circuits every time.  
Some specificities are not replicated for sake of simplicity but it should be pretty representative.  
Sorry for code in Python, if you want to change behavior, add parameters or functionnalities (like A/B testing) please contact me or PR.
Insight: https://lontivero.github.io/Wiki/html/tor.html

Past runs in `testruns.txt`

### Usage
Prerequisites: tor, python3. 

`tor --controlport 9051`  
`python3 main.py`

### Test Config
Config in `config.py`:

`clearnet`: if true use `urlClear` if false use `urlTor`  
`circuitBuildTimeout`: `CircuitBuildTimeout` tor setting  
`exitNodesSubset`: `ExitNodesSubset` tor setting. Use [""] for all or ["exitnode1", "exitnode2", ...]  

`sampleNbRounds`: Nb of mock up rounds that will be created during test (number of loops)  
`nbClientsInRound`: In each rounds, how much different clients will be simulated  
`nbInputsPerClient`: Nn inputs each clients will register  
`concurrentFallbackRequests`: Nb of Similar requests sent at the same time, after first complete other cancel (on master = 1)  

`phases`: Duration of each phase can be tweaked here  
