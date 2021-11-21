from .bot_sender import BotSender
import discord
from datetime import datetime

class ChannelsSender(BotSender):
    async def sendMessage(self, channels):
        a = await self.bot.fetch_guild(self.guild_id)
        guild_channels = await a.fetch_channels()
        for guild_channel in guild_channels:
            if guild_channel.name in channels:
                await guild_channel.send('ding ding', embed=discord.Embed(title="Bell", description="the Act of Ringing", url="https://github.com/maged1995", timestamp=datetime.now(), color=discord.Colour(0x992d22)))