def mkQuery(url, query):
    req = url + '?'
    for i in query:
        req += str(i) + '=' + str(query[i]) + '&'
    req = req[:-1]
    return req


if __name__ == "__main__":
    print(mkQuery("https://example.com", {"foo": "bar", "bar": "foo"}))