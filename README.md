# xpss
X-Plane Scenery Sorter

## About

xpss is a free lightweight scenery_packs.ini sorter for X-Plane.

## Usage
Advise: Place it in your `Custom  Scenery` - Folder

`python xpss.py ` 
This will read `scenery_packs.ini` and `config.txt` in current directory and print out new config

## configuration
`config.txt` is a simple config file where each line is a sorting number and a substring. 
e.g.: `9 Library` moves all sceneries containing the substring `Library` to category 9
