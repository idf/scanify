# scanify
A command line for applying image scanning effect. 

Make a document page taken with a phone camera appear to be scanned:
![demo](./demo/demo.jpg)  

# Usage
```bash
Usage:
  scanify <path>
  scanify <path> -o <outpath>
Examples:
  scanify '~/Desktop/p0.jpg'

Options:
  -o --out      output path of the image, default output to the same path with
                sufixx
```

# Install
## pip

```bash
pip3 install scanify
```
## Manual
```bash
git clone https://github.com/idf/scanify.git
cd scanify
sudo python setup.py install
```

