
class AvalonGame():
    def __init__(self):
        self.player_list = {}
        self.role_dict = {'ls': 'Loyal Servents of Arthur', 'me': 'Merlin','pe':'Percival','mm':'Minion of Morederd','md':'Mordered','mg':'Morgana','as':'Assassin','ob':'Oberon'}

    def add_player(self,player,role):
        self.player_list[player] = role
        message = 'Du har blivit tillagd som {}. Väntar in övriga spelare'.format(self.role_dict[role])
        return message

    def help(self):
        message = 'Hej!\n Skicka in vilken karaktär du är genom att skicka följande kod för de olika karaktärerna:\n Loyal Servents of Arthur = .ab ls\n Merlin = .ab me\n Percival = .ab pe\n Minion of Mordered = .ab mm\n Mordered = .ab md\n Morgana = .ab mg\n Assassin = .ab as\n Oberon = .ab ob'
        return message

    def evil_see(self):
        message = 'De onda du kan se är:\n'
        for player in self.player_list:
            player_role = self.player_list[player]
            if player_role == 'mm' or player_role == 'as' or player_role == 'md' or player_role == 'mg':
                message += player.name+'\n'
        return message

    def merlin_see(self):
        message = 'De onda du kan se är:\n'
        for player in self.player_list:
            player_role = self.player_list[player]
            if player_role == 'mm' or player_role == 'as' or player_role == 'mg' or player_role == 'ob':
                message += player.name+'\n'
        return message

    def percival_see(self):
        message = 'Du som Percival ser följande:\n'
        for player in self.player_list:
            player_role = self.player_list[player]
            if player_role == 'me' or player_role == 'mg':
                message += player.name+'\n'
        return message
  
    def get_player_messages(self):
        player_messages = {}
        for player in self.player_list:
            player_role = self.player_list[player]
            if player_role == 'mm' or player_role == 'as' or player_role == 'md' or player_role == 'mg':
                player_messages[player] = self.evil_see()
            elif player_role == 'me':
                player_messages[player] = self.merlin_see()
            elif player_role == 'pe':
                player_messages[player] = self.percival_see()
        return player_messages
        
