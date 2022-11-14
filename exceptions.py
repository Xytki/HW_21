class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'


class TooManyDifferentError(BaseError):
    message = 'Много разных товаров'
