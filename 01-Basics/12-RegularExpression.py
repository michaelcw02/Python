from re import search

dateformatdict = {
        'yyyy-mm-dd' :  r'(?P<year>\d{4})-'
                        r'(?P<month>\d{2})-'
                        r'(?P<day>\d{2}).?'
                        r'(?P<hour>\d{2})?:?'
                        r'(?P<minute>\d{2})?:?'
                        r'(?P<second>\d{2})?.?'
                        r'(?P<microsecond>\d{0,6})?'}

show_re = (dateformatdict['yyyy-mm-dd'])

input_string = '2017-06-26 12:11:12'

re_result_dict = search(show_re, input_string).groupdict()

print(str(re_result_dict))

'''
Estructura de dato: diccionario (llave-dato)
Para obtener datos específicos:
    re_result_dict[year] -> retorna el año
'''