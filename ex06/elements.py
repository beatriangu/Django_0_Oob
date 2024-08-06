#!/usr/bin/python3

from elem import Elem, Text


class Html(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='html', attr=attr, content=content, tag_type='double')


class Head(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='head', attr=attr, content=content, tag_type='double')


class Body(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='body', attr=attr, content=content, tag_type='double')


class Title(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='title', attr=attr, content=content, tag_type='double')


class Meta(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')


class Img(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='img', attr=attr, content=content, tag_type='simple')


class Table(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='table', attr=attr, content=content, tag_type='double')


class Th(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='th', attr=attr, content=content, tag_type='double')


class Tr(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='tr', attr=attr, content=content, tag_type='double')


class Td(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='td', attr=attr, content=content, tag_type='double')


class Ul(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='ul', attr=attr, content=content, tag_type='double')


class Ol(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='ol', attr=attr, content=content, tag_type='double')


class Li(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='li', attr=attr, content=content, tag_type='double')


class H1(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='h1', attr=attr, content=content, tag_type='double')


class H2(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='h2', attr=attr, content=content, tag_type='double')


class P(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='p', attr=attr, content=content, tag_type='double')


class Div(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(attr=attr, content=content, tag_type='double')


class Span(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='span', attr=attr, content=content, tag_type='double')


class Hr(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='hr', attr=attr, content=content, tag_type='double')


class Br(Elem):
        def __init__(self, content=None, attr: dict = {}):
                super().__init__(tag='br', attr=attr, content=content, tag_type='double')



def test():
    html = Elem('html', attr={'lang': 'en'},
                content=[
                    Elem('head', content=[
                        Elem('meta', attr={'charset': 'UTF-8'}),
                        Elem('title', content=Text('Sample Page'))
                    ]),
                    Elem('body', content=[
                        Elem('h1', content=Text('Welcome to my Website!')),
                        Elem('p', content=Text('This is a sample page generated using Python.')),
                        Elem('img', attr={'src': 'image.jpg', 'alt': 'Sample Image'}),
                        Elem('hr'),
                        Elem('h2', content=Text('List of Items')),
                        Elem('ul', content=[
                            Elem('li', content=Text('Item 1')),
                            Elem('li', content=Text('Item 2')),
                            Elem('li', content=Text('Item 3'))
                        ]),
                        Elem('div', attr={'class': 'footer'}, content=[
                            Elem('p', content=Text('© 2024 My Website'))
                        ])
                    ])
                ])
    print(html)

if __name__ == '__main__':
    test()

