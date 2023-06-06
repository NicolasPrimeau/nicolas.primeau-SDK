import unittest

import sdk
import exceptions


class TheOneAPiSdkTest(unittest.TestCase):
    def test_list_movies(self):
        with self.assertRaises(exceptions.UnauthorizedError):
            sdk.TheOneApiSdk().movies.list().fetch()
