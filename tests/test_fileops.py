from pathlib import Path

import pytest

from openhands.runtime.utils import files

SANDBOX_PATH_PREFIX = '/workspace'
CONTAINER_PATH = '/workspace'
HOST_PATH = 'workspace'


def test_resolve_path():
    assert (
        files.resolve_path('test.txt', '/workspace', HOST_PATH, CONTAINER_PATH)
        == Path(HOST_PATH) / 'test.txt'
    )
    assert (
        files.resolve_path('subdir/test.txt', '/workspace', HOST_PATH, CONTAINER_PATH)
        == Path(HOST_PATH) / 'subdir' / 'test.txt'
    )
    assert (
        files.resolve_path(
            Path(SANDBOX_PATH_PREFIX) / 'test.txt',
            '/workspace',
            HOST_PATH,
            CONTAINER_PATH,
        )
        == Path(HOST_PATH) / 'test.txt'
    )
    assert (
        files.resolve_path(
            Path(SANDBOX_PATH_PREFIX) / 'subdir' / 'test.txt',
            '/workspace',
            HOST_PATH,
            CONTAINER_PATH,
        )
        == Path(HOST_PATH) / 'subdir' / 'test.txt'
    )
    assert (
        files.resolve_path(
            Path(SANDBOX_PATH_PREFIX) / 'subdir' / '..' / 'test.txt',
            '/workspace',
            HOST_PATH,
            CONTAINER_PATH,
        )
        == Path(HOST_PATH) / 'test.txt'
    )
    with pytest.raises(PermissionError):
        files.resolve_path(
            Path(SANDBOX_PATH_PREFIX) / '..' / 'test.txt',
            '/workspace',
            HOST_PATH,
            CONTAINER_PATH,
        )
    with pytest.raises(PermissionError):
        files.resolve_path(
            Path('..') / 'test.txt', '/workspace', HOST_PATH, CONTAINER_PATH
        )
    with pytest.raises(PermissionError):
        files.resolve_path(
            Path('/') / 'test.txt', '/workspace', HOST_PATH, CONTAINER_PATH
        )
    assert (
        files.resolve_path('test.txt', '/workspace/test', HOST_PATH, CONTAINER_PATH)
        == Path(HOST_PATH) / 'test' / 'test.txt'
    )


codex/add-tests-for-read-lines-function

codex/add-tests-for-read-lines-function-awyb1q
main
def test_read_lines_final_segments():
    lines = [f"line {i}\n" for i in range(5)]

    # Request the last line using different end values
    assert files.read_lines(lines, start=4) == ["line 4\n"]
    assert files.read_lines(lines, start=4, end=-1) == ["line 4\n"]
    assert files.read_lines(lines, start=4, end=5) == ["line 4\n"]
    assert files.read_lines(lines, start=4, end=10) == ["line 4\n"]

    # Reading the last two lines explicitly
    assert files.read_lines(lines, start=3, end=5) == ["line 3\n", "line 4\n"]

    # If start is beyond the end of the list, an empty list is returned
    assert files.read_lines(lines, start=len(lines)) == []
codex/add-tests-for-read-lines-function




main
def test_read_lines_eof_exact_end():
    lines = ['1\n', '2\n', '3\n']
    assert files.read_lines(lines, start=2, end=3) == ['3\n']


def test_read_lines_eof_overflow_end():
    lines = ['1\n', '2\n', '3\n']
    assert files.read_lines(lines, start=2, end=10) == ['3\n']
main
