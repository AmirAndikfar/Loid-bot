import yt_dlp
import asyncio
import discord
import logging

class YTLOID:
    def __init__(self, bot):
        self.bot = bot
        self.yt_dl_options = {"format": "bestaudio/best"}
        self.ytdl = yt_dlp.YoutubeDL(self.yt_dl_options)
        self.ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn -filter:a "volume=0.15"'}
        self.queues = {}
        self.voice_clients = {}

    async def play(self, interaction, url):
        await interaction.response.defer()
        try:
            voice_client = self.voice_clients.get(interaction.guild.id)
            if not voice_client or not voice_client.is_connected():
                voice_client = await interaction.user.voice.channel.connect()
                self.voice_clients[interaction.guild.id] = voice_client

            data = await self._extract_info(url)

            song = data['url']
            player = discord.FFmpegOpusAudio(song, **self.ffmpeg_options)

            voice_client.play(player)
            await interaction.followup.send(f"Now playing: {data['title']}")
        except discord.errors.ClientException as e:
            logging.error(f"ClientException in play command: {e}")
            await interaction.followup.send("An error occurred while trying to play the song. Please make sure I have permission to connect to the voice channel.")
        except yt_dlp.utils.DownloadError as e:
            logging.error(f"DownloadError in play command: {e}")
            await interaction.followup.send("An error occurred while downloading the song. Please check the URL and try again.")
        except Exception as e:
            logging.error(f"Unexpected error in play command: {e}")
            await interaction.followup.send(f"An unexpected error occurred while trying to play the song.\nError: {e}")

    async def _extract_info(self, url):
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(url, download=False))
        return data
