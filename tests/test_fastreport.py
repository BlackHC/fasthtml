from pathlib import Path
from fasthtml.common import *
from fasthtml.fastreport import fast_report

def test_fast_report_with_function(tmp_path: Path):
    def page():
        return Titled('Hello', P('Test'))
    dest = tmp_path / 'report.html'
    path = fast_report(page, dest=dest)
    assert path == dest
    html = dest.read_text()
    assert '<title>Hello</title>' in html
    assert '<p>Test</p>' in html


def test_fast_report_with_content(tmp_path: Path):
    page = Titled('Other', P('World'))
    dest = tmp_path / 'report2.html'
    path = fast_report(page, dest=dest)
    assert path == dest
    html = dest.read_text()
    assert '<title>Other</title>' in html
    assert '<p>World</p>' in html
