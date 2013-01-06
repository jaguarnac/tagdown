'''
AppModel class
'''
import pymongo

class AppModel(object):
    '''
    AppModel class.
    base class for all application models
    '''
    
    def __init__(self):
        '''
        Initialize the model, setup database connection
        '''