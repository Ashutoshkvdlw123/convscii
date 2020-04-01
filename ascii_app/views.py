from . import app, db
from flask import render_template, url_for, request, redirect, flash
from ascii_app.forms import ConvertTextForm
from ascii_app.models import TextItem
from datetime import datetime
import pyfiglet


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/convert_text", methods=["GET", "POST"])
def convert_text():
    form = ConvertTextForm()
    art = ""
    if request.method == "POST":
        if form.validate_on_submit():
            print("validate_on_submit")
            figlet = pyfiglet.Figlet(font=form.font.data)
            art = f"""{figlet.renderText(form.text.data)}"""
            text_item = TextItem(dt=datetime.utcnow(), font=form.font.data, text=form.text.data)
            text_item.save()

    return render_template("convert_text.html", form=form, art=art, title="Convert Text")


@app.route("/text_history")
def text_history():
    return render_template("history_text.html", title="Text History",text_items=TextItem.query.all())
