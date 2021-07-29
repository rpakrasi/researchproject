# izhikevich cell
import numpy as np
import matplotlib.pyplot as plt


class izhCell():
    def __init__(self,stimVal):
        # Define Neuron Parameters
        self.celltype='Generic Izhikevich' # Regular spiking
        self.C=100
        self.vr=-60
        self.vt=-40
        self.k=0.7
        self.a=0.03
        self.b=-2
        self.c=-50 
        self.d=100
        self.vpeak=35
        self.stimVal = stimVal
    
        
        # Set up the simulation
        self.T=1000 # ms
        self.tau=1 # ms - time step
        self.n=int(np.round(self.T/self.tau))
        
        # Set up the stimulation
#        self.I = np.concatenate((np.zeros((1,int(0.1*self.n))),self.stimVal*np.ones((1,int(0.01*self.n))),self.stimVal*.1*np.ones((1,int(0.89*self.n)))), axis=1)
        self.I = np.concatenate((np.zeros((1,int(0.1*self.n))), 
                 self.stimVal*np.ones((1,int(0.9*self.n)))), axis=1)

        # Set up placeholders for my outputs from the simulation              
        self.v=self.vr*np.ones((1,self.n))
        self.u=0*self.v
        
    def __repr__(self):
        return self.celltype +' Cell with StimVal=' + str(self.stimVal)

    def simulate(self):    
        # Run the simulation
        # print("vpeak = ", self.vpeak)
        for i in range(1,self.n-1):
            self.v[0,i+1]=self.v[0,i]+self.tau*(self.k*(self.v[0,i]-self.vr)*(self.v[0,i]-self.vt)-self.u[0,i]+self.I[0,i])/self.C
            self.u[0,i+1]=self.u[0,i]+self.tau*self.a*(self.b*(self.v[0,i]-self.vr)-self.u[0,i])
            
            if self.v[0,i+1]>=self.vpeak:
                    self.v[0,i]=self.vpeak
                    self.v[0,i+1]=self.c
                    self.u[0,i+1]=self.u[0,i+1]+self.d 
                    
def plotMyData(somecell, upLim = 1000):
    tau = somecell.tau
    n = somecell.n
    v = somecell.v
    celltype = somecell.celltype

    # Plot the results
    #fig = plt.figure()
    plt.plot(tau*np.arange(0,n),v[0,:].transpose(), 'k-')
    plt.xlabel('Time Step')
    plt.xlim([0, upLim])
    plt.ylabel(celltype + ' Cell Response')
    plt.show()

def createCell():
    myCell = izhCell(stimVal=200)        
    myCell.simulate()
    plotMyData(myCell)
    
if __name__=='__main__':
    createCell()

