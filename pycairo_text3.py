#!/usr/bin/python
#-*- coding:utf8 -*-
import cairo
import pango
import pangocairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 100)
context = cairo.Context(surface)

pango_cairo = pangocairo.CairoContext(context)

layout = pango_cairo.create_layout()
layout.set_font_description(pango.FontDescription('Serif Normal 12'))
layout.set_text('മലയാളം हिन्दी ଓଡ଼ିଆ தமிழ்as');
# Next four lines take care of centering the text. Feel free to ignore ;-)
width, height = surface.get_width(), surface.get_height()
print width,height
w, h = layout.get_pixel_size()
position = (width/2.0 - w/2.0, height/2.0 - h/2.0)
position = (w,h)
context.move_to(*position)
pango_cairo.show_layout(layout)
surface.write_to_png('malayalam.png')
