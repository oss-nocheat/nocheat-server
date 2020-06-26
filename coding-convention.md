Coding convention rule for python
==================================
follows PEP 8 python style guide

# 1. Code Lay-out
----------------
## Indentation
Use 4 spaces per indentation level.
Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line

## Maximum Line Length
Limit all lines to a maximum of 79 characters.

## Blank Lines
Surround top-level function and class definitions with two blank lines.
Method definitions inside a class are surrounded by a single blank line.
Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
Use blank lines in functions, sparingly, to indicate logical sections.
Python accepts the control-L (i.e. ^L) form feed character as whitespace; Many tools treat these characters as page separators, so you may use them to separate pages of related sections of your file. Note, some editors and web-based code viewers may not recognize control-L as a form feed and will show another glyph in its place.

## import
Imports should usually be on separate lines.
<pre>
<code>
# Correct:
import os
import sys
</code>
</pre>
<pre>
<code>
# Correct:
# Wrong:
import sys, os
</code>
</pre>

## Comments
Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).
An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
