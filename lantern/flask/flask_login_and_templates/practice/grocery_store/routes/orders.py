from flask import Blueprint, render_template
from flask_login import current_user
from grocery_store.models import User

list_of_orders = Blueprint('/orders', __name__)


@list_of_orders.route('/orders', methods=["GET", "POST"])
def user_orders():
    if current_user:
        user = User.query.filter_by(user_id=current_user.user_id).first()
        orders = user.orders
        for order in orders:
            order.created_time
        return render_template('orders.html', name=user, orders=orders)
