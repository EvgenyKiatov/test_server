import server.library.handler as server
def main():
    """
    Создает HTTP-сервер, который ожидает запросов на заданный адрес
    """
    addr=('',80)
    with server.HTTPServer(addr,server.MyHandler) as srv:
        srv.serve_forever()

if __name__ == '__main__':
    main()