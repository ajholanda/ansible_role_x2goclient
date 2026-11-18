import pytest


@pytest.fixture
def x2go_package(host):
    return host.package("x2goclient")


def test_x2goclient_is_installed(x2go_package):
    assert x2go_package.is_installed


def test_x2goclient_binary_exists(host):
    binary = host.file("/usr/bin/x2goclient")
    assert binary.exists
    assert binary.is_file
