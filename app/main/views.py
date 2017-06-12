# -*- coding: utf-8 -*-
__author__ = 'lenovo'

from datetime import datetime
from flask import render_template, sessions, redirect, url_for


from . import main
from .forms import NameForm
from .. import db
from ..models import Users


@main.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.inxde'))
    return render_template('index.html', form=form, name=sessions.get('name'), known=sessions.get('known', False),
                           current_time=datetime.utcnow())
