import os
import tempfile
import unittest

import yaml

from core.config import ConfigManager


class TestConfigOutboundProxy(unittest.TestCase):
    def test_load_outbound_proxy_from_yaml(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            yaml_path = os.path.join(tmp, "settings.yaml")
            with open(yaml_path, "w", encoding="utf-8") as f:
                yaml.safe_dump(
                    {
                        "basic": {
                            "outbound_proxy": {
                                "enabled": "true",
                                "protocol": "socks5",
                                "host": "127.0.0.1",
                                "port": "7890",
                                "username": "u",
                                "password_enc": "enc",
                                "no_proxy": "localhost,127.0.0.1",
                                "direct_fallback": "false",
                            }
                        }
                    },
                    f,
                    allow_unicode=True,
                    sort_keys=False,
                )

            mgr = ConfigManager(yaml_path=yaml_path)
            outbound = mgr.config.basic.outbound_proxy

            self.assertTrue(outbound.enabled)
            self.assertEqual(outbound.protocol, "socks5")
            self.assertEqual(outbound.host, "127.0.0.1")
            self.assertEqual(outbound.port, 7890)
            self.assertEqual(outbound.username, "u")
            self.assertEqual(outbound.password_enc, "enc")
            self.assertEqual(outbound.no_proxy, "localhost,127.0.0.1")
            self.assertFalse(outbound.direct_fallback)

