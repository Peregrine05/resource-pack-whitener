# resource-pack-whitener

A script that modifies all textures in a resource pack to be white

## Setup

This is a Python script. Make sure that you have the latest available version of Python 3.x installed.

The resource pack that you intend to modify with this script must be extracted for the script to successfully operate; it cannot be in ZIP form. 

## Usage

Simply run the script by double-clicking it or by running the command:

```
python resource_pack_whitener.py
```

You will be prompted for the path to the resource pack directory. Enter the directory of the resource pack, which is the folder that contains the `pack.mcmeta` file of the resource pack, and then press Enter. You will be asked whether or not the script should continue.

**Note that this script will attempt to modify every file with the file extension ".png" in the selected directory. Ensure that you have selected the correct directory before continuing to prevent unintended loss of your files.**

To abort the script at this point, type "n" or "N" and then press Enter. To continue the script, type "y" or "Y" and then press Enter. After all modifications have been completed, the script will report the number of files modified and then exit.

### Advanced

As this script will only modify files in the target directory and its subdirectories, you can be more specific about which textures the script should modify. For example, to modify only block textures, pass to the script the path to the `block` directory of the resource pack. To modify only item textures, pass to the script the path to the `item` directory. The same applies for other texture classes.
