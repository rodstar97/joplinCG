import json
import requests
import os
import pprint
import logging
import sys
import psutil
from ui.utils import show_help

os.environ['NO_PROXY']='127.0.0.1'
JOPLIN_HOST = 'http://localhost:41184'
token = '8f015d416d10f1eb855d752d56aa1e14caf165909030b7abf38e6a594c7aac8d590e247a75aa8fd623578761383be264425d5604c4d640bf6daa6e74cf3c3852'
context = 'houdini'


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger("jopi")






class JoplinClient(requests.Session):
    """ 
    Shamles stolen from 
    https://github.com/foxmask/joplin-api/blob/master/joplin_api/core.py
    ported to Python 2.7

    """
    def __init__(self):
        super(JoplinClient, self).__init__()
        self.params = {}
        self.url = url


    def get_joplin(self):
        pass




    def query(self, method, path, fields='', **payload):
        """
        Query to Joplin API
        :param method: the kind of query to do
        :param path: endpoints url to the API eg 'notes' 'tags' 'folders'
        :param fields: fields we want to get
        :param payload: dict with all the necessary things to deal with the API
        :return json data
        """
        url = '{0}/{1}}/'.format(JOPLIN_HOST, folder)
        data ={
                'token':token,
        }

        if method not in ('get', 'post', 'put', 'delete'):
            raise ValueError('method expected: get, post, put, delete')


        query = self.get(url=url,params= data)
        if query.status_code < 227:
                logger.info('get data from {0}'.format(url))
                if query.json():
                    logger.debug('api query with status {0}'.format(query.raise_for_status()))
                    return query.json()
                else:
                    logger.info('No Tags exits')
                    return dict()
        else:
                logger.error('joplin api request failed with {0}'.format(query.raise_for_status()))
                raise Exception



def setup():
    """
    check, if able to connect to the joplin api

    return {url,port,token}
    """

    # Get Config data
    try:
        with open('config.json', "r") as config_file:
            config = json.load(config_file)

        if 'url' and 'port' and 'token' in config.keys():
            try:
                # test connectio to Joplin rest Api
                requests.get(url='{0}:{1}/ping/'.format(config['url'],config['port']), params={'token':config['token']})
                logger.info('config file is valid')

                # setup up connection attributes
                return {
                'url':config['url'],
                'port':config['port'],
                'token':config['token']}

            except requests.exceptions.ConnectionError as e:
                # get no connection to joplin
                logger.error('config not valid error: {0}'.format(e))
                logger.info('check if joplin is running')

                # check if Joplin is running
                for process in psutil.process_iter():
                    if process.name() == 'joplin':
                        logger.debug('joplin is running')
                        show_help('joplin app is running\nbut config file is not Valid\nplease check the help file')
                        break
                else:
                    logger.debug('joplin NOT running')
                    show_help('joplin app is not running\nplease start joplin ')

        else:
            #the config file failed to connect
            logger.error('config not valid')
            show_help('in the config.json one of the params is not valid\nplease check the help file')
            raise KeyError

    except EnvironmentError as e:
        show_help('cant open or find the config.json file\nplease check the help file')
        logger.error('error open config.json file with {0}'.format(e))








if __name__ == '__main__':
    setup()






