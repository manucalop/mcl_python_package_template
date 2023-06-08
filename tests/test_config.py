import os
import unittest

from mcl_python_package_template.config import get_config


class TestConfig(unittest.TestCase):
    def setUp(self):
        pass

    def test_config(self):
        os.environ["ENV_NAME"] = "test"
        config = get_config("config.yaml")
        self.assertEqual(config.env_name, "test")


if __name__ == "__main__":
    unittest.main()
