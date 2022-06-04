from aiogram.dispatcher.filters.state import State, StatesGroup


class ProductForm(StatesGroup):
    product_name = State()
    shop_name = State()
    price = State()
    product_url = State()
    delivery_date = State()
    delivery_time = State()
