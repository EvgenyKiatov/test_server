import string
digits = set(string.digits)
lowers = set(string.ascii_lowercase)
uppers = set(string.ascii_uppercase)
podch=set('_')
allowed_symbols = set()
allowed_symbols.update(digits,lowers,uppers,podch)
not_allowed_symbols = set(string.printable) - allowed_symbols

def handle(search_header:str,headers:dict)->bool:
    """
    Функция, которая проверяет, соответствует ли значение ключа определенным условиям
    :param search_header: Искомый заголовок
    :param headers: Словарь с заголовками
    :return:True, если значение соответвстует всем условиям
    """
    if search_header in headers:
        header = headers[search_header]
        if len(header)>15 or len(header)<1:
            return False
        if any(i in not_allowed_symbols for i in header):
            return False
        if any(i in allowed_symbols for i in header):
            return True
    else:
        return False

if __name__ == '__main__':
     assert handle('IMSI',{'IMSI':''}) == False
     assert handle('IMSI',{'SP':'12_321dda'}) == False
     assert handle('IMSI',{'SP':'__321','IMSI':''})==False
     assert handle('IMSI', {'SP': '__321', 'IMSI': '230llsd'}) == True
     assert handle('IMSI',{'IMSI':'oepwq%% '}) == False