# xpss
X-Plane Scenery Sorter

## About

xpss is a free lightweight scenery_packs.ini sorter/manager  for X-Plane.

## Usage
Advise: Place it in your `Custom  Scenery` - Folder

`python xpss.py ` or `./xpss.py`This will read `scenery_packs.ini` and `config.txt` in current directory and print out new config

### or

`./xpss.py <INFILE> <OUTFILE>`

e.g.: 
`./xpss.py scenery_packs.ini scenery_packs.ini`  

This replaces scenerypacks file




it will remove doublettes automatically


## configuration
`config.txt` is a simple config file where each line is a sorting number and a substring. 
e.g.: `9 Library` moves all sceneries containing the substring `Library` to category 9

see [Example Config File](config.txt)
