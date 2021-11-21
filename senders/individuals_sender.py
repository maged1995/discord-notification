from .bot_sender import BotSender
import discord
from datetime import datetime

class IndividualsSender(BotSender):
    async def sendMessage(self, users):
        a = await self.bot.fetch_guild(self.guild_id)
        async for member in a.fetch_members():
            if member.display_name in users:
                await member.send('ding ding', embed=discord.Embed(title="Bell", description="the Act of Ringing", url="https://github.com/maged1995", timestamp=datetime.now(), color=discord.Colour(0x992d22)))