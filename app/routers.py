from flask import render_template, flash, redirect, url_for
from app import app
from bokeh.models import ColumnDataSource, Select, Slider, DataTable, DateFormatter, TableColumn
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.models.callbacks import CustomJS
from datetime import date
from random import randint

from my_lib_work.user_full_func import get_list
from app.cod_callback import simple_table

from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from app.forms import RegistrationForm
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
#@login_required
def index():
    data = dict(
        data_X=get_list(50,2),
        data_Y=get_list(50,3)
    )

    source = ColumnDataSource(data)

    columns = [
        TableColumn(field="data_X", title="data_X"),
        TableColumn(field="data_Y", title="data_Y"),
    ]
    high_W =280
    width_W = 400
    data_table = DataTable(source=source, columns=columns, width=width_W, height=high_W, fit_columns=True)

    genre_list = ['Все ПС работающие со сбоем', 'Все ТП работающие со сбоем', 'ПС - оооо']

    controls = {
        "reviews": Slider(title="Выберите минимальное значение Х", value=max(data['data_X']), start=min(data['data_X']), end=max(data['data_X']), step=1),
        "genre": Select(title="Выберите объект работающий со сбоем", value="All", options=genre_list)
    }

    controls_array = controls.values()

    callback = CustomJS(args=dict(source=source, controls=controls), code=simple_table)

    for single_control in controls_array:
        single_control.js_on_change('value', callback)

    inputs_column = column(*controls_array, width=320, height=1000)
    layout_row = row([inputs_column, data_table])

    script, div = components(layout_row)
    #script, div = components(data_table)
    script_1, div_1 = components(data_table)

    return render_template(
        'index.html',
        script=script,
        div=div,
        script_1=script_1,
        div_1=div_1,
        js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),
        len_X=len(data['data_X']),
        high_W=high_W,
        width_W=width_W,
        max_X=max(data['data_X'])
    ).encode(encoding='UTF-8')
