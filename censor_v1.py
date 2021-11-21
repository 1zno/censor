import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        filename = f"hmm.txt"  # txtfile and code in same root folder
        with open(filename, "r") as file:
            words = [word.strip().lower() for word in file.readlines()]
        if message.author == self.user:
            return
        messageContent = message.content
        for word in words:
            if word in messageContent.lower():
                await message.delete()
                await message.channel.send("{}, ayy not allowed".format(message.author.mention))


client = MyClient()
client.run('token')
