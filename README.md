# Chick Magnet

Use this script to list magnet links for RARBG searches.

## Requirements
- `python` version >= 3
- `requests` (`pip install requests`)

## Usage
Edit chickmagnet.py and set the variable `APP_ID` to something unique of your choosing (without spaces).


Get magnet links by `python3 chickmagnet.py "search term"`

*Note: You can only get a maximum of 100 magnet links. This is a restriction of the RARBG API.*

The list of magnet links of your most recent search is output in **recent_results.txt**.

A cumulative list of magnet links is stored in **magnets.txt**.

A history of your search terms is stored in **history.txt**.
