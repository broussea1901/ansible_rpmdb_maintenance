import os

def test_apache_installed(host):
    apache = host.package("httpd")
    assert apache.is_installed

def test_postgresql_installed(host):
    postgresql = host.package("postgresql")
    assert postgresql.is_installed