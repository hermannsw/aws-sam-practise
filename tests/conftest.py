import pytest

from src.model.message_model import MessageModel


@pytest.fixture(scope='module', autouse=True)
def global_fixture():
    setup()
    yield
    remove_test_data()


def remove_test_data():
    MessageModel.delete_table()


def setup():
    if MessageModel.exists():
        MessageModel.delete_table()
    MessageModel.create_table(wait=True)
    m = MessageModel('id_01', 'user_01')
    m.save()
