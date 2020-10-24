class Account:

    def __init__(self):
        self.games = []

class XAccount(Account):

    def __init__(self, gamertag, xuid):
        self.gamertag = gamertag
        self.xuid = xuid

class PSAccount(Account):

    def __init__(self, onlineId):
        self.onlineId = onelineId

class Game:

    def __init__(self, name, achievements, stats):
        self.name = name
        self.achievements = []
        self.stats = stats