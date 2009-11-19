from django.test import TestCase, Client

class RequestVarsPanelTest(TestCase):

    def testSimpleKwargs(self):
        self.assertContains(self.client.get('/test2/'), 'test_view')

    def testComplexKwargs(self):
        self.assertContains(self.client.get('/test/'), 'test_view')
