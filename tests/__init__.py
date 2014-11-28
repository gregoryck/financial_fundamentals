'''
Created on Sep 12, 2013

@author: akittredge
'''

import os

def turn_on_request_caching():
    pass

_test_docs_dir = os.path.join(os.path.dirname(__file__), 'assets') 
asset_file_path = lambda asset_file_name : os.path.join(_test_docs_dir, asset_file_name)
