from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
#from flask_wtf.file import FileField, FileAllowed, FileRequired

fonts = [("3x5", "3x5"), ("alphabet", "alphabet"), ("standard", "standard"),
         ("3-d", "3-d"), ("graffiti", "graffiti"), ("weird", "weird"),
         ("slant", "slant"), ("5lineoblique", "5lineoblique"), ("banner3-D", "banner3-D"),
         ("doh", "doh"), ("isometric1", "isometric1"), ("letters", "letters"),
         ("alligator", "alligator"), ("dotmatrix", "dotmatrix"), ("bubble", "bubble"),
         ("bulbhead", "bulbhead"), ("digital", "digital"), ("acrobatic", "acrobatic"),
         ("alligator2", "alligator2"), ("avatar", "avatar"), ("banner", "banner"),
         ("banner3", "banner3"), ("banner4", "banner4"), ("barbwire", "barbwire"),
         ("basic", "basic"), ("bell", "bell"), ("big", "big"),
         ("bigchief", "bigchief"), ("binary", "binary"), ("block", "block"),
         ("doom", "doom"), ("calgphy2", "calgphy2"), ("caligraphy", "caligraphy"),
         ("catwalk", "catwalk"), ("chunky", "chunky"), ("coinstak", "coinstak"),
         ("colossal", "colossal"), ("computer", "computer"), ("contessa", "contessa"),
         ("contrast", "contrast"), ("cosmic", "cosmic"), ("cosmike", "cosmike"),
         ("cricket", "cricket"), ("cyberlarge", "cyberlarge"), ("cybermedium", "cybermedium"),
         ("cybersmall", "cybersmall"), ("drpepper", "drpepper"), ("eftichness", "eftichness"),
         ("diamond", "diamond"), ("eftifont", "eftipiti"), ("epic", "epic"),
         ("gothic", "gothic"), ("hollywood", "hollywood"), ("invita", "invita"), ("isometric2", "isometric2"),
         ("isometric3", "isometric3"), ("isometric4", "isometric4"), ("larry3d", "larry3d"),
         ("lcd", "lcd"), ("linux", "linux"), ("mirror", "mirror"),
         ("nancyj", "nancyj"), ("nancyj-fancy", "nancyj-fancy"), ("nancyj-underlined", "nancyj-underlined"),
         ("rowancap", "rowancap"), ("starwars", "starwars"), ("trek", "trek")]


class ConvertTextForm(FlaskForm):
  text = TextAreaField("Text to convert", validators=[DataRequired()])

  font = SelectField("Font", validators=[DataRequired()], choices=fonts)
  submit = SubmitField("Convert")
