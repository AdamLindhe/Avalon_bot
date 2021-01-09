import os
import AvalonGame
import discord
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'NzkyMTcwMDIwMzU2MDk2MDEw.X-Zz0g.BiZyEiCC3hYuTfChW_wWxSCN4aA'


class AvalonClient(discord.Client):
    
    def __init__(self):
        super(AvalonClient,self).__init__()
        self.setUp = False
        self.codes = ['start','help','go','number','ls','me','pe','mm','md','mg','as','ob',]

    async def on_message(self,message):
        if message.author == client.user:
            return
        if message.content[0:3] == '.ab':
            if len(message.content.split(' '))<2:
                await message.channel.send('Felaktig input')
                return
            code = message.content.split(' ')[1]
            if code in self.codes:
                if code == 'start':
                    #await self.send_message(message.channel,'setting upp game')
                    await message.channel.send('setting upp game')
                    self.setUp = True
                    self.avGame = AvalonGame.AvalonGame()
                elif code =='go' and self.setUp:
                    player_messages = self.avGame.get_player_messages()
                    for player in player_messages:
                        await player.send(player_messages[player])

                elif code == 'help' and self.setUp:
                    await message.channel.send(self.avGame.help())
                
                elif self.setUp and code == 'number':
                    await message.channel.send('Antal spelare klara: {}'.format(len(self.avGame.player_list)))

                elif self.setUp and code !='go':
                    text = self.avGame.add_player(message.author,code)
                    #await self.send_message(message.channel,text)
                    await message.author.send(text)


            else:
                await message.channel.send('Felaktig input')
                
        

client = AvalonClient()

client.run(TOKEN)
