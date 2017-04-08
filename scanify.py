#!/usr/bin/env python3
"""scanify

Usage:
  scanify <path>
  scanify <path> -o <outpath>
  scanify -e <path>
Examples:
  scanify '~/Desktop/p0.jpg'
  # output to '~/Desktop/p'~/Desktop/p0_scanify.jpg'

Options:
  -o --out      output path of the image, default output to the same path with
                sufixx
  -e --exposure adjust image exposreu
"""

from core import *
from docopt import docopt


if __name__ == "__main__":
    runnable = Scanifier()
    options = docopt(__doc__, version='scanify 0.0.1')
    context_dict = {}
    in_path = options['<path>']
    out_path = options.get('<outpath>')
    increase_exposure = True if options['--exposure'] else False

    runnable.run(in_path, out_path, increase_exposure)
