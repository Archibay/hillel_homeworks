from urllib import parse as p


def parse(query: str) -> dict:
    p.urlsplit(query)
    p.parse_qs(p.urlsplit(query).query)
    result = dict(p.parse_qsl(p.urlsplit(query).query))
    return result

    # if query.find('?') >= 0:
    #     end_of_link = query.split("?")[1]
    #     end_of_link = end_of_link.replace('=', ' ').replace('&', ' ')
    #     list_of_kv = end_of_link.split()  # created a list of future keys / values lists
    #     list_of_keys = []
    #     list_of_values = []
    #     for i in list_of_kv:
    #         if list_of_kv.index(i) % 2 == 0:
    #             list_of_keys.append(i)  # fill a keys list
    #         else:
    #             list_of_values.append(i)  # fill a values list
    #     res = dict.fromkeys(list_of_keys)  # create dict with keys by our key-list and None-values
    #     if len(list_of_values) > 0:
    #         a = 0
    #         for i in list_of_keys:
    #             res[i] = list_of_values[a]  # add values by our values list
    #             a += 1
    #     return res
    # else:
    #     return {}  # if link is not include '?' return empty dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/pagename=11&color=222') == {}
    assert parse('https://example.com/path/to/page?1=2&1=2&1=2&1=2&1=2&1=2&') == {'1': '2'}
    assert parse('https://example.com/path/to/page?car=smart&color=green&fuel_type=diesel&') == \
           {'car': 'smart', 'color': 'green', 'fuel_type': 'diesel'}
    assert parse('https://example.com/path/to/page?=&') == {}
    assert parse('https://example.com/path/to/page?name=1&name=2&name=3') == {'name': '3'}
    assert parse('https://example.com/path/to/page?name=ferret=1&color=blue') == {'name': 'ferret=1', 'color': 'blue'}
    assert parse('https://example.com/path/to/page?!=!&!!=!!') == {'!': '!', '!!': '!!'}
    assert parse('https://example.com/path/to/page?q=w&e=r&t=y') == {'q': 'w', 'e': 'r', 't': 'y'}
    assert parse('https://example.com/path/to/page?якийсь=1&текст=2') == {'якийсь': '1', 'текст': '2'}
    assert parse('https://example.com/path/to/page?!@$%^*()=1&{}[]:;",<.>/?=1') == \
           {'!@$%^*()': '1', '{}[]:;",<.>/?': '1'}

# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
