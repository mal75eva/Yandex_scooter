import configuration
import requests

#Создание заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = body)

#Получение данных о заказе по треку
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH + str(track))