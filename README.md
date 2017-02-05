# Facebook_manager

A Kalliope Neuron used to :
- POST messages on your own wall
- READ posts of an other wall

## Synopsis

This neuron allows you to 
- POST a message to your facebook wall.
- READ a number of messages from a user_name.

## Installation
```bash
kalliope install --git-url https://github.com/kalliope-project/kalliope_neuron_facebook.git
```

## Specification

The Facebook Neuron has multiple available actions : POST, READ.

Each of them requires specific options, return values and synapses example : 

#### POST 
##### Options


| parameter   | required | type   | default | choices    | comment                              |
|-------------|----------|--------|---------|------------|--------------------------------------|
| action      | YES      | String | None    | POST, READ | Defines the action type              |
| token       | YES      | String | None    |            | The facebook token                   |
| message     | YES      | String | None    |            | The text to post                     |


##### Return Values

| Name    | Description                                | Type   | sample      |
|---------|--------------------------------------------|--------|-------------|
| action  | the action USED                            | String | POST        |
| message | The text posted on the wall                | String | Hi Kalliope |

##### Synapses example

``` yml
- name: "post-facebook"
  neurons:
    - facebook_manager:
        action: "POST"
        token: "MY_SECRET_TOKEN"
        args:
          - message
  signals:
    - order: "post on facebook {{ message }}"
```


#### READ
##### Options


| parameter   | required | type   | default | choices    | comment                              |
|-------------|----------|--------|---------|------------|--------------------------------------|
| action      | YES      | String | None    | POST, READ | Defines the action type              |
| token       | YES      | String | None    |            | The facebook token                   |
| nb_messages | No       | int    | 10      |            | number of messages to read           |
| user_name   | Yes      | String | None    |            | the user name                        |

##### Return Values

| Name     | Description                                | Type   | sample                                                                    |
|----------|--------------------------------------------|--------|---------------------------------------------------------------------------|
| action   | the action USED                            | String | POST                                                                      |
| posts    | The list of posts on the wall              | List   | ["hi there", "this is my wall", "Check out this new Kalliope neuron !"]   |
| user_name| The user name where to read message        | String | BillGates                                                                 |

##### Synapses example

``` yml
- name: "read-facebook"
  neurons:
    - facebook_manager:
        action: READ
        token: "MY_SECRET_TOKEN"
        nb_messages: 3
        args:
          - user_name
  signals:
    - order: "Read Facebook messages from {{ user_name }}"
```

An example using the Jinja2 templates files:
``` yml
- name: "read-facebook"
  signals:
    - order: "Read Bill Gates Facebook posts"
  neurons:
      - facebook_manager:
           token: "MY_SECRET_TOKEN"
           action: "READ"
           user_name: "BillGates"
           nb_messages: 3
           file_template: neurons/facebook_manager/facebook_template_test.j2
```

The template defined in the facebook_template_test.j2
``` jinja2
{% for post in posts %}
    {{ user_name }} wrote {{ post }}
{% endfor %}
```
##### 

## Notes

In order to be able to post on Facebook, you need to get a Facebook User access token. 

### How to get your Facebook User Access Token

1. checkout on the facebook doc : https://developers.facebook.com/tools/explorer/
1. log in with your facebook account.
1. Click on "Get Token" and select "Get User Access Token"
1. Select the rights you want for your token : for this neuron you need to check at least : "publish_actions" and "user_status" and "user_posts"
1. Use your token in your kalliope neuron and post a message !
