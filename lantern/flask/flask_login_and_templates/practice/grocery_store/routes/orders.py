from flask import Blueprint, render_template
from grocery_store.models import User, Order, OrderLine
from flask_login import current_user

list_of_orders = Blueprint('/orders', __name__)


@list_of_orders.route('/orders', methods=["GET", "POST"])
def user_orders():
    if current_user:
        name = User.query.filter_by(name=current_user.name).first()
        orders = [order for order in name.orders]
        for order in orders:
            print(dir(order))
        return render_template('orders.html', name=name, orders=orders)
