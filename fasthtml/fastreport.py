"""Utilities for building static HTML reports with FastHTML"""

from pathlib import Path
from .fastapp import fast_app
from .core import Client

__all__ = ['fast_report']


def fast_report(func, dest='report.html', route='/', **app_kwargs):
    """Render `func` using FastHTML and save to `dest`.

    `func` should be a callable that behaves like a FastHTML route handler,
    returning FT elements or anything supported by FastHTML. Parameters in
    `app_kwargs` are forwarded to :func:`fast_app` so you can enable features
    such as KaTeX or additional headers. The rendered HTML page is written to
    `dest` and the path to the generated file is returned.
    """
    # Build a temporary FastHTML app
    app, rt = fast_app(**app_kwargs)[:2]

    # Register the handler on the provided route
    rt(route)(func)

    # Call the route using the in-memory client
    cli = Client(app)
    html = cli.get(route).text

    # Write output HTML
    dest = Path(dest)
    dest.write_text(html, encoding='utf-8')
    return dest
