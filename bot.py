import os
import asyncio
import logging
import discord 	
from discord.ext import commands
from loid_modules.yt_loid import YTLOID
from loid_modules.controls_loid import LOIDControls

def setup_logging():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

def run_bot():
    TOKEN = os.getenv('LOID_DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="$", intents=intents)

    # Initialize modules
    yt_loid = YTLOID(bot)
    loid_controls = LOIDControls(bot)

    @bot.tree.command(name="play", description="Play a song from YouTube")
    async def play(interaction: discord.Interaction, url: str):
        await yt_loid.play(interaction, url)

    @bot.tree.command(name="pause", description="Pause the current song")
    async def pause(interaction: discord.Interaction):
    	try:
            await loid_controls.pause(interaction)
    	except Exception as e:
            logging.error(f"Error in pause command: {e}")
            await interaction.followup.send("An error occurred while trying to pause the song.")

    @bot.tree.command(name="resume", description="Resume the current song")
    async def resume(interaction: discord.Interaction):
    	try:
        	await loid_controls.resume(interaction)
    	except Exception as e:
            logging.error(f"Error in resume command: {e}")
            await interaction.followup.send("An error occurred while trying to resume the song.")

    @bot.tree.command(name="stop", description="Stop the current song and disconnect")
    async def stop(interaction: discord.Interaction):
    	try:
        	await loid_controls.stop(interaction)
    	except Exception as e:
            logging.error(f"Error in stop command: {e}")
            await interaction.followup.send("An error occurred while trying to stop the song.")

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now jamming')
        await bot.tree.sync()

    setup_logging()
    bot.run(TOKEN, log_handler=None)

if __name__=='__main__':
    run_bot()
