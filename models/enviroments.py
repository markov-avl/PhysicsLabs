from pylatex.base_classes import Environment


class Titlepage(Environment):
    escape = False
    content_separator = "\n"


class Sloppypar(Environment):
    escape = False
    content_separator = "\n"
