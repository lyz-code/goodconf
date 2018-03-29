from goodconf import GoodConf
from .utils import env_var


def test_conf_env_var(mocker, tmpdir):
    mocked_load_config = mocker.patch('goodconf._load_config')
    path = tmpdir.join('myapp.json')
    path.write('')
    c = GoodConf(file_env_var='CONF')
    with env_var('CONF', str(path)):
        c.load()
    mocked_load_config.assert_called_once_with(str(path))


def test_all_env_vars(mocker):
    mocked_set_values = mocker.patch('goodconf.GoodConf.set_values')
    c = GoodConf()
    c.load()
    mocked_set_values.assert_called_once_with({})


def test_provided_file(mocker, tmpdir):
    mocked_load_config = mocker.patch('goodconf._load_config')
    path = tmpdir.join('myapp.json')
    path.write('')
    GoodConf().load(str(path))
    mocked_load_config.assert_called_once_with(str(path))


def test_default_files(mocker, tmpdir):
    mocked_load_config = mocker.patch('goodconf._load_config')
    path = tmpdir.join('myapp.json')
    path.write('')
    bad_path = tmpdir.join('does-not-exist.json')
    c = GoodConf(default_files=[bad_path, path])
    c.load()
    mocked_load_config.assert_called_once_with(path)