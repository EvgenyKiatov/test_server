from http.server import HTTPServer,BaseHTTPRequestHandler
from server.library.handle_func import handle
class MyHandler(BaseHTTPRequestHandler):
    """
    Обработчик запросов
    """
    def do_GET(self):
        """
        Метод, который обрабатывает GET-запрос.
        :return: Если запрос соответствует заданным условиям, то возвращает ответ 200 OK,
        Если запрос не соответствует условиям, то возвращает 500 System Error
        """
        search_header = 'IMSI'
        headers = dict(self.headers)
        print(headers)
        response = handle(search_header,headers)
        if response == True:
            self.send_response(200,message='OK')
            self.log_message('OK')
        elif response == False:
            self.send_response(500,message='System Error')
        self.end_headers()
