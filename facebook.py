import logging
import facebook

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Facebook(NeuronModule):
    def __init__(self, **kwargs):
        super(Facebook, self).__init__(**kwargs)

        token = kwargs.get('token', None)
        user_name = kwargs.get('user_name', None)

        graph = facebook.GraphAPI(token)
        profile = graph.get_object(user_name)
        posts = graph.get_connections(profile['id'], 'posts')
