"""Utilities for building static HTML reports with FastHTML"""

from pathlib import Path
from .fastapp import fast_app
from .core import Client

__all__ = ['fast_report']


def fast_report(content, dest='report.html', **app_kwargs):
    """Render `content` as a static HTML report and save to ``dest``.

    ``content`` may be either a callable (a typical FastHTML handler) or an
    object that FastHTML can render. It will be served at the root ``/`` route
    of a temporary app which is then invoked via the in-memory :class:`Client`.
    Parameters in ``app_kwargs`` are forwarded to :func:`fast_app` so additional
    options such as KaTeX can be enabled. The generated HTML file path is
    returned.
    """

    app, rt = fast_app(**app_kwargs)

    if callable(content):
        handler = content
    else:
        def handler(*args, **kwargs):
            return content

    rt('/')(handler)

    cli = Client(app)
    html = cli.get('/').text

    dest = Path(dest)
    dest.write_text(html, encoding='utf-8')
    return dest
