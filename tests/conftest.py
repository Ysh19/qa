import os

import dotenv
import pytest
from sqlalchemy.testing.plugin.plugin_base import logging


@pytest.fixture(scope="session", autouse=True)
def envs():
    dotenv.load_dotenv()
    # print('envs')


@pytest.fixture(scope="session")
def app_url():
    # print("APP_URL",os.getenv("APP_URL"))
    return os.getenv("APP_URL")
