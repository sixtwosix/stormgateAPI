## return the user data searching with name
import requests
import json

class stormgateUser():
    
    def __init__(self, name):
        self.username = name
        self.urlBase = "https://api.stormgateworld.com/v0/"
        self.userJSON = {}
        self.userFound = False
        self.noSuchUser = False
        self.__findUserByName()
        
    def getUsername(self):    

        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        username = self.userJSON['nickname']    
        return username
    
    def setUsername(self, name):
        '''
        Changes username of user
        '''
        self.userJSON = {}
        self.userFound = False
        self.username = name
        
        
    def __findUserByName(self):        
        url = self.urlBase + "leaderboards/ranked_1v1"
        pageCount = 1        
        usernameFound = False
        while not usernameFound:
            params = {"page": pageCount}
            res = self.__apiCall(url,params)
            if(res['entries'] == []):
                self.userJSON = []
                self.noSuchUser = True
                break
            for user in res['entries']:
                try:
                    if(user['nickname'] == self.username):
                        usernameFound = True
                        self.userJSON = user
                        self.userFound = True
                        break
                except:
                    continue
                
            pageCount += 1
    
    def getUserID(self):
        '''
        Returns the player ID assigned to played
        '''
        userID = ""
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        userID = self.userJSON['player_id']
        
        return userID
        
    def getRank(self):
        '''
        Returns the rank placement, 
        Eg. Aspirant 3
        '''
        rank = "" 
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        rank = f"{self.userJSON['league']} {self.userJSON['tier']}"
        
        return rank
        
    def getLeaderboardNumber(self):
        '''
        Returns the number ranked out of all the players
        '''
        leaderboardNumber = ""
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        leaderboardNumber = int(self.userJSON['rank'])
        
        
        return leaderboardNumber

    def getMMR(self):
        '''
        Returns mmr as a rounded int 
        '''
        mmr = ""
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
        
        mmr = int(round(self.userJSON['mmr']))
        
        return mmr
        
    def getWinRate(self):
        '''
        Returns winrate as string with '%' sign 2 decimal places
        '''
        winrate = ""
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        winrate = "{:.2f}%".format(self.userJSON['win_rate'])
        
        return winrate
        
    def getWinLossTiesTotal(self):
        '''
        Returns a list with [Win,Loss,Ties,Total] matches
        '''
        winLossTiesTotal = []
        
        if(not self.userFound):
            if(not self.noSuchUser):
                self.__findUserByName()
            else:
                return None
        
        if(self.userJSON == []):
            print(f"No user found with name {self.username}")
            return None
        
        winLossTotal = [self.userJSON['wins'],self.userJSON['losses'],self.userJSON['ties'],self.userJSON['matches']]
        
        return winLossTotal
        
    
    def __apiCall(self,url,params = None):
        res = requests.get(url,timeout=20,params=params)
        if(res.status_code == 200):
            resJSON = json.loads(res.text)
            return resJSON
        else :
            return None   
        
        
if __name__ == "__main__":
    newUser = stormgateUser("Transistor_ZA")
    print(f"Username: {newUser.getUsername()}")
    print(f"UserID : {newUser.getUserID()}")
    print(f"Rank : {newUser.getRank()}")
    print(f"Leaderboard number : {newUser.getLeaderboardNumber()}")
    print(f"MMR : {newUser.getMMR()}")
    print(f"Winrate : {newUser.getWinRate()}")
    res = newUser.getWinLossTiesTotal()
    res_captions = ["Wins","Loss","Ties","Total"]
    if(res != None):
        for i in range(len(res_captions)):        
            print(f"{res_captions[i]} : {res[i]}")
    
    
    
    
    