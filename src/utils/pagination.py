from src.common.mixins import Page


__all__ = ('get_paginated_response',)


def paginate(query, page):
    page_size = Page.page_size
    if page <= 0:
        page = 1
    if page_size <= 0:
        page_size = 10

    # query.filter() returns list and query.filter_by returns iterator
    if isinstance(query, list):
        offset = page_size * (page - 1) if page > 1 else 0
        items = query[offset: offset + page_size]
        total = len(query)
    else:
        items = query.limit(page_size).offset((page - 1) * page_size).all()
        total = query.order_by(None).count()
    return Page(items, page, total)


def get_paginated_response(query, request):
    try:
        page_no = int(request.args.get('page', 1))
    except ValueError:
        page_no = 1
    page = paginate(query, page_no)
    data = {
        'results': [obj.to_dict() for obj in page.items],
        'total': page.total,
        'next': page.next_page,
        'previous': page.previous_page
    }
    return data
