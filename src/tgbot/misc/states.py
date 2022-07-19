from aiogram.dispatcher.filters.state import State, StatesGroup


class ProductForm(StatesGroup):
    product_name = State()
    shop_name = State()
    price = State()
    product_url = State()
    track_number = State()
    delivery_date = State()
    delivery_time = State()


class AddressForm(StatesGroup):
    name = State()
    street = State()
    house = State()
    apartments = State()
    city = State()
    state = State()
    zip_code = State()
    phone = State()
    country = State()
