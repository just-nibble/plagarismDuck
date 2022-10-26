from duckduckgo_search import ddg


def search(query):
    response = ddg(query)
    return response
