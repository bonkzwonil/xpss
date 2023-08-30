# xpss
X-Plane Scenery Sorter

## About

xpss is a free lightweight scenery_packs.ini sorter/manager  for X-Plane.

## Usage
Place it in your `Custom  Scenery` - Folder

`python xpss.py -h` or `./xpss.py -h`

## Example

### Scan mode
`./xpss.py -s . -o scenery_packs.ini`

This will scan the current directory (should be your `Custom Scenery`) and replaces scenerypacks ini file

### Transform/Tidy up mode
`./xpss.py -i scenery_packs.ini -o scenery_packs.ini`

This will read in scenery_packs.ini and replaces it withj a sorted version



## configuration
`config.txt` is a simple config file where each line is a sorting number and a substring. 
e.g.: `9 Library` moves all sceneries containing the substring `Library` to category 9

see [Example Config File](config.txt)
