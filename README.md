# Chick Magnet

Use this script to get magnet links for RARBG and automatically add them to qBittorrent.

## Requirements

You need [qBittorrent-nox](https://manpages.ubuntu.com/manpages/cosmic/man1/qbittorrent-nox.1.html) if you want the script to automatically queue torrents.

Install `requests` with `pip install requests`.

## Usage

`python3 chickmagnet.py "search term 1080p"`

## Customization

Set the variable `APP_ID` to something unique of your choosing (without spaces).

If you want to list the magnets instead of downloading them then uncomment line 26.

If you are unable to (or do not want to) use qBittorrent-nox, comment out lines 32 and 33.
