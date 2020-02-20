import json
import requests
import os
import pprint
import logging


os.environ['NO_PROXY']='127.0.0.1'
JOPLIN_HOST = 'http://localhost:41184'
token = '8f015d416d10f1eb855d752d56aa1e14caf165909030b7abf38e6a594c7aac8d590e247a75aa8fd623578761383be264425d5604c4d640bf6daa6e74cf3c3852'
context = 'houdini'



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("jopi")

def joplin_query():
    """
    """
    pass






def get_tags():
    """
    return json{}
    """
    url = '{0}/tags/'.format(JOPLIN_HOST)
    data ={
            'token':token,
    }
    query = requests.get(url=url,params= data)
    if query.status_code < 227:
            logger.info('get data from {0}'.format(url))
            if query.json():
                return query.json()
            else:
                logger.info('No Tags exits')
                return dict()
    else:
            logger.error('joplin api request failed with {0}'.format(query.raise_for_status()))
            raise Exception





def get_context_notebook(context):
    """
    return notbook json{}
    """
    url = '{0}/folders/'.format(JOPLIN_HOST)
    data ={
            'token':token,
    }
    query = requests.get(url=url,params= data)
    if query.status_code < 227:
            logger.info('get data from {0}'.format(url))
            if query.json():
                return query.json()
            else:
                logger.info('No Tags exits')
                return dict()
    else:
            logger.error('joplin api request failed with {0}'.format(query.raise_for_status()))
            raise Exception









def create_note(titel ,body ,file_link, tags):
    """
    return bool sucess
    """
    
    url = '{0}/notes/'.format(JOPLIN_HOST)
    data ={
            'token':token,
    }





if __name__ == '__name__':
    a = get_tags()
    pprint.pprint(a)

