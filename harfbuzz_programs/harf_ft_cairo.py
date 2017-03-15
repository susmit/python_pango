#!/usr/bin/python3

import sys
import os
import math
import warnings
import qahirah as qah
from qahirah import \
    CAIRO, \
    Colour, \
    Glyph, \
    Vector
import harfbuzz as hb

ft = qah.get_ft_lib()

_text = "Kivy is Awesome !"
_font = "DejaVu Serif"

text_size = 50
label_font = \
    (qah.Context.create_for_dummy()
        .set_font_face(qah.FontFace.create_for_pattern("DejaVu Serif"))
        .set_font_size(text_size / 2)
    ).scaled_font
buf = hb.Buffer.create()

line_pos = Vector(0, 0)
ft_face = ft.find_face(_font)
ft_face.set_char_size(size = text_size, resolution = qah.base_dpi)
hb_font = hb.Font.ft_create(ft_face)

buf.reset()
buf.add_str(_text)
buf.guess_segment_properties()
hb.shape(hb_font, buf)
line, line_end = buf.get_glyphs(line_pos)
lines =\
    {
        "font" :
            (qah.Context.create_for_dummy()
                .set_font_face(qah.FontFace.create_for_ft_face(ft_face))
                .set_font_size(text_size)
            ).scaled_font,
        "text" : line,
    }
line_pos = Vector(0, line_pos.y + ft_face.size["metrics"]["height"])


margin = Vector(10, 10)
figure_size = Vector(line_end.x, line_pos.y) + 2 * margin
img = qah.ImageSurface.create \
  (
    format = CAIRO.FORMAT_RGB24,
    dimensions = round(figure_size)
  )
ctx = \
    (qah.Context.create(img)
        .translate(margin + Vector(0, text_size ))
        .set_source_colour(Colour.grey(1))
        .paint()
        .set_source_colour(Colour.grey(0))
    )

ctx.set_scaled_font(label_font)
ctx.set_scaled_font(lines["font"])
ctx.show_glyphs(tuple(qah.offset_glyphs(lines["text"], Vector(0, 0))))
img.flush().write_to_png("output.png")
hb_font = None # prevents crash at end?