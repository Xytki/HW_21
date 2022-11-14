from exceptions import BaseError
from property.courier import Courier
from property.request import Request
from property.shop import Shop
from property.store import Store

shop = Shop(
    items={
        'печенька': 3,
        'компьютер': 2,
    }
)

store = Store(
    items={
        'печенька': 10,
        'компьютер': 20,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "стоп" чтобы продолжить.\n',
        )

        if user_input in ('стоп'):
            break
        try:
            request = Request(request_str=user_input, storages=storages)

            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()

