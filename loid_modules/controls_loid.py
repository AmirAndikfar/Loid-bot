import discord
import logging

class LOIDControls:
    def __init__(self, bot):
        self.bot = bot

    async def pause(self, interaction):
        await interaction.response.defer()
        voice_client = discord.utils.get(self.bot.voice_clients, guild=interaction.guild)
        if voice_client:
            voice_client.pause()
            await interaction.followup.send("Paused the song.")
        else:
            await interaction.followup.send("No voice client found for this guild.")
                        
    async def resume(self, interaction):
        await interaction.response.defer()
        voice_client = discord.utils.get(self.bot.voice_clients, guild=interaction.guild)
        if voice_client:
            voice_client.resume()
            await interaction.followup.send("Resumed the song.")
        else:
            await interaction.followup.send("No voice client found for this guild.")
                
    async def stop(self, interaction):
        await interaction.response.defer()
        voice_client = discord.utils.get(self.bot.voice_clients, guild=interaction.guild)
        if voice_client:
            voice_client.stop()
            await voice_client.disconnect()
            await interaction.followup.send("Stopped the song and disconnected.")
        else:
            await interaction.followup.send("No voice client found for this guild.")
        
