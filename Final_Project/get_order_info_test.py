#Кристина Заморская, 26-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

#Тест
def test_get_order_info():
    #Создание заказа и получение его трека
    track_number = sender_stand_request.create_new_order(data.body).json()["track"]
    #Получение информации о заказе по треку
    response = sender_stand_request.get_order_info(track_number)
    #Проверка статуса ответа
    assert response.status_code == 200