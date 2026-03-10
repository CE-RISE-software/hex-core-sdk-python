import unittest

from ce_rise_hex_core_sdk import ApiClient, Configuration
from ce_rise_hex_core_sdk.api.admin_api import AdminApi
from ce_rise_hex_core_sdk.api.discovery_api import DiscoveryApi
from ce_rise_hex_core_sdk.api.models_api import ModelsApi


class TestSmokeClient(unittest.TestCase):
    def test_api_surfaces_exist(self):
        cfg = Configuration(host="http://localhost:8080")
        client = ApiClient(cfg)

        self.assertIsNotNone(AdminApi(client))
        self.assertIsNotNone(DiscoveryApi(client))
        self.assertIsNotNone(ModelsApi(client))

    def test_default_configuration_has_host(self):
        cfg = Configuration()
        self.assertTrue(isinstance(cfg.host, str))
        self.assertNotEqual(cfg.host, "")


if __name__ == "__main__":
    unittest.main()
