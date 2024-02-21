# Pyxreser
**Pyxreser** is a small Python library designed to simplify the creation of **[Pyxel](https://github.com/kitao/pyxel)** image by converting 256x256 pixel 16-color PNG or JPG images into **.pyxres** files.

## Why? 
This library was born out of frustration with the inconvenient use of Pyxel's built-in editor and aims to provide a simpler alternative for generating custom images for your games. It's mainly a personal desire to easily create a tile map using image software such as [Microsoft Paint](https://www.microsoft.com/windows/paint) or pixel-editing software such as [PyxelEdit](https://pyxeledit.com/), [PixelEditor](https://pixieditor.net) which makes my life a lot easier when creating games. If you're on this page, you're probably looking for a solution to do just that, and I think pyxreser is it.

## Features

- Converts 16-color 256-pixel PNG or JPG images into Pyxel image.

## Installation

```bash
pip install pyxreser
```

## Usage

To use Pyxreser, you can run the following command in your terminal:

```
pyxreser image [-h | --help] [TYPE] [N | -n N] [IMAGE | -i IMAGE | --image IMAGE] [OUTPUT | -o OUTPUT | --output OUTPUT] [-v | --version]

Optional options :
  -h, --help Displays this help message and quits
  -v, --version Displays Pyxreser version
  OUTPUT: Pyxres output path and .pyxres file name (default: input image name without extension)

Arguments :
  TYPE, there is only the "image" type for the moment. (future versions will include "tilemap", "sound", "music")
  N, image number (1-3) (default: 1)
  IMAGE, Image input path, 

```

It's important to note that the provided image must adhere to the following criteria:

- It must contain exactly 16 different colors.
- Its size must be 256x256 pixels.

If a .pyxres file already exists at the specified location, Pyxreser will modify it by replacing the existing image with the new one.

If your image does not contain the same default colors on Pyxel, Pyxreser will automatically generate or replace a .pyxpal file in addition to your .pyxres file.

### Example

```
pyxreser image 0 picture.png resource.pyxres
```

## Future Features Checklist

- [ ] Image Conversion: Convert tilemap files into Pyxel-compatible tilemap.
- [ ] Sound Conversion from MP3: Convert MP3 audio files for integration into games.
- [ ] Music Conversion from MP3: Convert MP3 music files into Pyxel-compatible audio formats.
