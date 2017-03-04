#!/usr/bin/env python

import sys
import math
import cairo
import pango
import pangocairo as pc

RADIUS = 150
N_WORDS = 10
FONT = "Serif 27"

def draw_text(cairo_ctx):
    # Center coordinates on the middle of the region we are drawing
    cairo_ctx.translate(RADIUS, RADIUS)

    # Create a Pango Context and Layout, set the font and text
    pc_ctx = pc.CairoContext(cairo_ctx)
    pc_layout = pc_ctx.create_layout()

    pc_layout.set_text("Text")
    desc = pango.FontDescription(FONT)
    pc_layout.set_font_description(desc)

    # Draw the layout N_WORDS times in a circle
    for i in range(N_WORDS):
        angle = (360. * i) / N_WORDS

        cairo_ctx.save()

        # Gradient from red at angle == 60 to blue at angle == 240
        red = (1 + math.cos((angle - 60) * math.pi / 180.)) / 2
        pc_ctx.set_source_rgb(red, 0, 1.0 - red);

        pc_ctx.rotate(angle * math.pi / 180.)

        # Inform Pango to re-layout the text with the new transformation
        pc_ctx.update_layout(pc_layout)

        width, height = pc_layout.get_size()
        cairo_ctx.move_to(-(float(width) / pango.SCALE) / 2, -RADIUS)
        pc_ctx.show_layout(pc_layout)

        cairo_ctx.restore()


def main():
    if len(sys.argv) != 2:
        print "Usage: cairosimple OUTPUT_FILENAME\n"
        return 1

    filename = sys.argv[1]

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 2 * RADIUS, 2 * RADIUS)
    cairo_ctx = cairo.Context(surface)

    cairo_ctx.set_source_rgb(1.0, 1.0, 1.0)
    cairo_ctx.paint()
    draw_text(cairo_ctx)

    try:
        status = surface.write_to_png(filename)
    except:
        print "Could not save png to '%s'\n" % filename
        return 1

    return 0

main()
