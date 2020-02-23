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



    # # Fallback
    # msg = 'OK'
    # joplin_port = 41184 #standart port

    # # Check for Port
    # try :
    #     ping = requests.get(url='http://localhost:{0}/ping/'.format(joplin_port))#,params={'token':token}
    #     if ping.text != 'JoplinClipperServer':
    #         logger.info('Joplin port is {0}'.format(joblin_port))
    #         pass

    # except requests.exceptions.ConnectionError as e:
    #     for port in range(41184,41195):
    #         try:
    #             ping = requests.get(url='http://localhost:{0}/ping/'.format(port))#,params={'token':token}
    #             if ping.text == 'JoplinClipperServer':
    #                 joblin_port = port
    #                 logger.info('Joplin port is {0}'.format(joblin_port))
    #                 break
    #         except requests.exceptions.ConnectionError:
    #             continue
    #     else:
    #         msg ='Cant connect to Joplin:'

    # except requests.exceptions.ConnectionError as e:
    #     logger.info('Connection error: {0}'.format(e))