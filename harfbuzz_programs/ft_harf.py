import sys
import qahirah as qah
import harfbuzz as hb

ft = qah.get_ft_lib()
text = "kivy"
buf = hb.Buffer.create()
buf.add_str(text)
buf.guess_segment_properties()
ft_face = ft.find_face("Scheherazade")
ft_face.set_char_size(size=1,resolution = qah.base_dpi)
hb_font = hb.Font.ft_create(ft_face)
hb.shape(hb_font,buf)

print (buf.glyph_infos)
print (buf.glyph_positions) 