#Planets class

class Exoplanet:
    #A class to hold Exoplanet characteristics
    
    def __init__(self,ID,attributes) :
        self.ID=attributes[0]
        
    def set_hostname(self,pl_hostname) :
        self.pl_hostname = pl_hostname

