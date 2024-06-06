# Loid-bot
### A simple Discord music player written in Python

Loid-bot is a Discord music player that allows you to play music from YouTube links in your Discord server. This bot is still a work in progress, and more features are planned for the future.

## Features

* Play music from YouTube links
* Basic playback controls (play, pause, resume, stop)

## Requirements

* `discord.py`
* `yt-dlp`
* `ffmpeg`

### Operating System-specific instructions

#### Windows

* Install `discord.py` using `pip install discord.py`
* Install `yt-dlp` using `pip install yt-dlp`
* Install `ffmpeg` from the official website
* Clone the repository using `git clone https://github.com/AmirAndikfar/Loid-bot.git`
* Configure the bot by creating a `.env` file with your Discord bot token
* Run the bot using `python bot.py`

#### Linux

* Install `discord.py` using `pip install discord.py`
* Install `yt-dlp` using `pip install yt-dlp`
* Install `ffmpeg` using your distribution's package manager (e.g., `sudo apt-get install ffmpeg` on Ubuntu)
* Clone the repository using `git clone https://github.com/AmirAndikfar/Loid-bot.git`
* Configure the bot by creating a `.env` file with your Discord bot token
* Run the bot using `python3 bot.py`

#### Mac

* Install `discord.py` using `pip install discord.py`
* Install `yt-dlp` using `pip install yt-dlp`
* Install `ffmpeg` using Homebrew (e.g., `brew install ffmpeg`)
* Clone the repository using `git clone https://github.com/AmirAndikfar/Loid-bot.git`
* Configure the bot by creating a `.env` file with your Discord bot token
* Run the bot using `python3 bot.py`

## Environment Variables

To run the bot, you need to define the `LOID_DISCORD_TOKEN` environment variable. This variable should contain your Discord bot token.

### Windows

* Right-click on "Computer" or "This PC" and select "Properties".
* Click on "Advanced system settings" on the left side.
* Click on "Environment Variables".
* Under "System Variables", click "New".
* In the "Variable name" field, enter `LOID_DISCORD_TOKEN`.
* In the "Variable value" field, enter your Discord bot token.
* Click "OK" to close all the windows.

### Linux (Bash)

* Open your shell configuration file (e.g., `~/.bashrc`) in a text editor.
* Add the following line to the end of the file:
```
export LOID_DISCORD_TOKEN="your_discord_token_here"
```
* Replace `your_discord_token_here` with your actual Discord bot token.
* Save the file and restart your terminal or run `source ~/.bashrc` to apply the changes.

### Linux (Zsh)

* Open your shell configuration file (e.g., `~/.zshrc`) in a text editor.
* Add the following line to the end of the file:
```
export LOID_DISCORD_TOKEN="your_discord_token_here"
```
* Replace `your_discord_token_here` with your actual Discord bot token.
* Save the file and restart your terminal or run `source ~/.zshrc` to apply the changes.

### Mac (using `launchd`)

* Open the Terminal app.
* Run the following command to set the environment variable:
```
launchctl setenv LOID_DISCORD_TOKEN your_discord_token_here
```
* Replace `your_discord_token_here` with your actual Discord bot token.
* Restart your terminal or run `launchctl stop` and `launchctl start` to apply the changes.


## Usage

Run the bot:
```bash
python3 bot.py
```

## Commands

* `/play <url>`: Play a song from the provided YouTube URL
* `/pause`: Pause the current song
* `/resume`: Resume the paused song
* `/stop`: Stop the current song and clear the queue

## Troubleshooting

* If you encounter issues with the bot, check the console output for error messages.
* Make sure you have the latest versions of `discord.py`, `yt-dlp`, and `ffmpeg` installed.
* If you're still having issues, feel free to open an issue on GitHub.

## Contributing

If you'd like to contribute to Loid-bot, please follow these guidelines:

* Submit issues and pull requests to the GitHub repository.
* Follow the code style and conventions used in the project.
* Provide detailed explanations for your changes and fixes.
