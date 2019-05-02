# to run this test from command line:
# python -m unittest test_app.py from the root of the project

# Standard library imports...
import unittest

# Local imports...
from app import create_app


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data ='{"1":20,"2":30}'

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_home(self):
        '''
        Requesting root expect 200
        '''
        response = self.client().get('/')
        self.assertEqual(response.status_code, 200)


    def test_status(self):
        '''
        Requesting status expect 200
        '''
        response = self.client().get('/status/')
        self.assertEqual(response.status_code, 200)


    def test_initialise(self):
        '''
        Sending incomplete request expect 400
        '''
        response = self.client().post('/initialise/')
        self.assertEqual(response.status_code, 400)


    def test_initialise2(self):
        '''
        Sending complete request expect 200
        '''
        response = self.client().post('/initialise/', data=self.data,
                              content_type='application/json',
                              follow_redirects=True)
        json_response = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Operation Completed Succesfully", json_response)

    def test_payment1(self):
        '''
        Sending incomplete request expect 400 and error message
        '''
        response = self.client().post('/payment/',
                                      content_type='application/json',
                                      follow_redirects=True)
        json_response = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual('''{
  "error": "Missing data in the request"
}
''', json_response)


    def test_payment2(self):
        '''
        Sending complete request expect 200
        '''
        response = self.client().post('/payment/', data=self.data,
                              content_type='application/json',
                              follow_redirects=True)
        json_response = response.get_data(as_text=True)
        print(json_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Operation Completed Succesfully", json_response)


    def test_status2(self):
        '''
        Requesting status after initialisation and payment expect 200
        '''
        response = self.client().get('/status/')
        json_response = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('''{
  "1": 40, 
  "2": 60
}
''', json_response)

    def test_change(self):
        '''
        Sending complete request expect 200
        '''
        response = self.client().post('/change/6',
                              content_type='application/json',
                              follow_redirects=True)
        json_response = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('''false
''', json_response)


    def test_status3(self):
        '''
        Requesting status after initialisation and change expect 200
        '''
        response = self.client().post('/change/6',
                              content_type='application/json',
                              follow_redirects=True)
        response = self.client().get('/status/')
        json_response = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('''{
  "1": 40, 
  "2": 57
}
''', json_response)


if __name__ == '__main__':
    unittest.main()