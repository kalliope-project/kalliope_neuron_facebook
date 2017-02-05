import logging
import facebook

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

Facebook_Actions = (
    "POST",
    "READ"
)


class Facebook_manager(NeuronModule):
    def __init__(self, **kwargs):
        super(Facebook_manager, self).__init__(**kwargs)

        self.token = kwargs.get('token', None)
        self.action = kwargs.get('action', None)
        self.user_name = kwargs.get('user_name', None)
        self.message = kwargs.get('message', None)
        self.nb_messages = int(kwargs.get('nb_messages', 10))  # Int

        if self._is_parameters_ok():
            graph = facebook.GraphAPI(self.token)
            if self.action == Facebook_Actions[0]: # POST
                if self._is_post_parameters_ok():
                    graph.put_wall_post(message=self.message)

                    message = {
                        "action": self.action,
                        "message": self.message
                    }

            if self.action == Facebook_Actions[1]:  # READ
                if self._is_read_parameters_ok():

                    profile = graph.get_object(self.user_name)
                    posts = graph.get_connections(profile['id'], 'posts')

                    posts_messages = list()
                    if "data" in posts:
                        count = 0
                        for data in posts["data"]:
                            if count >= self.nb_messages:
                                break
                            count += 1
                            # count < self.nb_messages
                            if "message" in data:
                                posts_messages.append(data["message"])

                    message = {
                        "action": self.action,
                        "user_name": self.user_name,
                        "posts": posts_messages
                    }

            self.say(message)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron.
        :return: True if parameters are ok, raise an exception otherwise.

        .. raises:: MissingParameterException
        """
        if self.token is None:
            raise MissingParameterException("Facebook needs a slack_token")
        if self.action is None:
            raise MissingParameterException("Facebook needs an action parameter")
        return True

    def _is_post_parameters_ok(self):
        """
        Check if parameters required to POST a message are present.
        :return: True, if parameters are OK, raise exception otherwise.

        .. raises:: MissingParameterException
        """
        if self.message is None:
            raise MissingParameterException("Facebook POST needs a message")

        return True


    def _is_read_parameters_ok(self):
        """
        Check if parameters required to READ a message are present.
        :return: True, if parameters are OK, raise exception otherwise.

        .. raises:: MissingParameterException
        """
        if self.user_name is None:
            raise MissingParameterException("Facebook READ needs a user name")

        return True
