# Instructions
 - cd in to the directory root.
 - Run `python -m importtest.b`
   - As expected, you get an error on `print a`
 - Run `python -m importtest.__init__`
   - Unexpectedly `print a` prints the package's `a`.
