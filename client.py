
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait
import time
import string
import statistics
import random
from config import *
from backend import RoundSimulator
from tor import torRequest

def clientAction(executor, phase, round):
    futures = []
    requestId = ''.join(random.choices(string.digits, k=12))
    for i in range(0, concurrentFallbackRequests):
        futures.append(executor.submit(torRequest))
    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
    round.action(phase, requestId)
    if(len(done) > 0):
        return done.pop().result()
    return -1

def client(executor, round):
    done = []
    currentPhase = None
    futures = []
    while(round.success is None):
        if(round.currentPhase != currentPhase):
            currentPhase = round.currentPhase
            for k in range(0, nbInputsPerClient):
                futures.append(executor.submit(clientAction, executor, currentPhase, round))

        done, not_done = wait(futures, return_when=FIRST_COMPLETED)
        time.sleep(1)
    requestDuration = []
    for requestDone in done:
        requestDuration.append(requestDone.result())

    return requestDuration
                    
def performTestAsync():
    roundsResults = []
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for i in range(0, sampleNbRounds):
            rnd = RoundSimulator()
            roundRequestTiming = []
            futures = []
            for j in range(0, nbClientsInRound):
                futures.append(executor.submit(client, executor, rnd))
            while(rnd.currentPhase != Phase.Ended):
                rnd.checkUpdatePhase()
                time.sleep(1)
            wait(futures)
            for future in futures:
                roundRequestTiming.append(future.result())

            durationList = [item[0].total_seconds() for sublist in roundRequestTiming for item in sublist]
            requestResultList = [item[1] for sublist in roundRequestTiming for item in sublist]
            roundResult = {}
            roundResult["avg"] = statistics.mean(durationList)
            roundResult["max"] = max(durationList)
            roundResult["sd"] = statistics.stdev(durationList)
            roundResult["round"] = rnd
            roundResult["durations"] = durationList
            roundResult["results"] = requestResultList

            roundsResults.append(roundResult)
            print("Round " + str(len(roundsResults)) + ": " + ("SUCCESS" if rnd.success else ("FAIL " + str(rnd.endPhase)))
                + " / Requests: Avg: " + "%.2f" % round(roundResult["avg"], 2)
                + " - Max: " + "%.2f" % round(roundResult["max"], 2)
                + " - sd: " + "%.2f" % round(roundResult["sd"], 2))

    return roundsResults