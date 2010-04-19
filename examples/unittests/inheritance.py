import unittest

import math
from gpyconf import Configuration
from gpyconf.fields import IntegerField, CharField, FloatField

class ConfigurationSuperclass(Configuration):
    field1_from_superclass = IntegerField()

class ConfigurationSuperclass2(ConfigurationSuperclass):
    field1_from_superclass2 = CharField()

class InheritedConfiguration(ConfigurationSuperclass2):
    field1_from_subclass = FloatField()


class InheritanceTest(unittest.TestCase):
    def runTest(self):
        self.config = InheritedConfiguration()
        self.assert_('field1_from_superclass' in self.config.fields)
        self.assert_('field1_from_superclass2' in self.config.fields)
        self.assert_('field1_from_subclass' in self.config.fields)

        self.config.field1_from_superclass = 42
        self.config.field1_from_superclass2 = 'hello world'
        self.config.field1_from_subclass = round(math.pi, 10)

        self.config.save()
        del self.config

        self.config = InheritedConfiguration()
        self.assertEqual(self.config.field1_from_superclass, 42)
        self.assertEqual(self.config.field1_from_superclass2, 'hello world')
        self.assertEqual(self.config.field1_from_subclass, round(math.pi, 10))

if __name__ == '__main__':
    unittest.main()
