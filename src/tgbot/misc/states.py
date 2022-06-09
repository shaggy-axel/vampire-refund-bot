from aiogram.dispatcher.filters.state import State, StatesGroup


class ProductForm(StatesGroup):
    product_name = State()
    shop_name = State()
    price = State()
    product_url = State()
    delivery_date = State()
    delivery_time = State()


class AddressForm(StatesGroup):
    name = State()
    line_1 = State()
    line_2 = State()
    city = State()
    state = State()
    zip_code = State()
    phone = State()
    country = State()
