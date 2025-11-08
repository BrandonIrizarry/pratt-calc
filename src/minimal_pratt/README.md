# Introduction

An arithmetic expression calculator in Python, demoing the Pratt
parsing algorithm.

This takes inspiration from [this 2010 blog
post](https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing)
by Eli Bendersky, as well as a few other sources, which I'll touch on
in a future blog post.

# Installation

Dependencies:

The
[more_itertools](https://more-itertools.readthedocs.io/en/stable/index.html)
library is used to convert a list of tokens into a peekable stream
used by the expression parser.

Using uv:


# Example Usage

Try

`python calculator 3+4*2^(5-1)+1`

or alternatively,

`./calculator 3+4*2^(5-1)+1`

which should print 68 at the console.


