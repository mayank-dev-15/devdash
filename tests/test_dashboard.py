import pytest, platform, shutil

def test_system_info():
    info = {'system': platform.system(), 'release': platform.release()}
    assert info['system'] in ('Linux', 'Darwin', 'Windows', 'Java')

def test_disk_usage():
    usage = shutil.disk_usage('/')
    assert usage.total > 0
