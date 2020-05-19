from flask import Blueprint, render_template
from grocery_store.models import Good

list_of_goods = Blueprint('/list_of_goods', __name__)


@list_of_goods.route('/list_of_goods')
def get_list_of_goods():
    return render_template('list_of_goods.html', goods=Good.query.all())
