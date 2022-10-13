
from datetime import datetime, timedelta
from config import phases
from phase import Phase

class RoundSimulator():
    success = None
    endPhase = None

    def __init__(self):
        self.inputsRegistered = []
        self.inputsConfirmed = []
        self.outputsRegistered = []
        self.signatureReceived = []
        self.currentPhase = Phase.InputRegistration
        self.dateEndPhase = datetime.utcnow() + timedelta(seconds=phases[Phase.InputRegistration])

    def endRound(self, success, endPhase):
        self.currentPhase = Phase.Ended
        self.success = success
        self.endPhase = endPhase
        self.dateEndPhase = datetime.utcnow()

    def updatePhase(self):
        if(self.currentPhase is Phase.InputRegistration):
            self.currentPhase = Phase.ConnectionConfirmation
            self.dateEndPhase = datetime.utcnow() + timedelta(seconds=phases[Phase.ConnectionConfirmation])
        elif(self.currentPhase is Phase.ConnectionConfirmation):
            self.currentPhase = Phase.OutputRegistration
            self.dateEndPhase = datetime.utcnow() + timedelta(seconds=phases[Phase.OutputRegistration])
        elif(self.currentPhase is Phase.OutputRegistration):
            self.currentPhase = Phase.TransactionSigning
            self.dateEndPhase = datetime.utcnow() + timedelta(seconds=phases[Phase.TransactionSigning])

    def checkUpdatePhase(self):
        if(self.success is not None):
            # round finished
            return

        if(datetime.utcnow() < self.dateEndPhase):
            # phase not finished
            return
        if(self.currentPhase == Phase.InputRegistration or self.currentPhase == Phase.ConnectionConfirmation):
                # no special rules for simplification
                self.updatePhase()
        elif(self.currentPhase == Phase.OutputRegistration):
            if(len(self.outputsRegistered) != len(self.inputsRegistered)):
                # round failed because not enough output registered
                # for simplification ratio input/output is 1
                self.endRound(False, Phase.OutputRegistration)
                return
            self.updatePhase()
        elif(self.currentPhase == Phase.TransactionSigning):
            if(len(self.signatureReceived) != len(self.inputsRegistered)):
                # round failed because not enough input signed
                self.endRound(False, Phase.TransactionSigning)
                return
            
            #success, this should be caught in action()
            self.endRound(True, Phase.TransactionSigning)
        return
    
    def action(self, actionPhase, actionId):
        self.checkUpdatePhase()
        if(self.currentPhase != actionPhase and not (self.currentPhase == Phase.OutputRegistration and actionPhase == Phase.ConnectionConfirmation)):
            # phase or round ended
            return
        if(actionPhase is Phase.InputRegistration):
            if not actionId in self.inputsRegistered: 
                self.inputsRegistered.append(actionId)
        elif(actionPhase is Phase.ConnectionConfirmation):
            if not actionId in self.inputsConfirmed: 
                self.inputsConfirmed.append(actionId)
        elif(actionPhase is Phase.OutputRegistration):
            if not actionId in self.outputsRegistered: 
                self.outputsRegistered.append(actionId)
        elif(actionPhase is Phase.TransactionSigning):
            if not actionId in self.signatureReceived: 
                self.signatureReceived.append(actionId)
        self.checkUpdatePhase()