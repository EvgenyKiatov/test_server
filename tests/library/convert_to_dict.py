def convert_to_dict(string:str)->dict:
    dictionary = {}
    string = string.split()
    for rec in string:
        rec = rec.split('=')
        dictionary[rec[0]] = rec[1]
    return dictionary

if __name__ == '__main__':
    assert convert_to_dict('ps=2') == {'ps':'2'}
    assert convert_to_dict('a=1 b=2') == {'a':'1','b':'2'}
    assert convert_to_dict('a= b=2 c=3') == {'a':'','b':'2','c':'3'}