import json
import requests
from behave import given, when, then, step

from features.support.helpers import generate_random, retrieve_synthetic


@step('I set the API endpoint to "{endpoint}"')
def step_set_endpoint(context, endpoint):
    # Store the endpoint template. It can include a placeholder {id}.
    context.endpoint = endpoint


@step('I set the post id to "{post_id}"')
def step_set_post_id(context, post_id):
    # Save the dynamic post id into the context.
    if str(post_id).lower() == "auto":
        context.feature_data["post_id"] = generate_random()
    elif str(post_id).lower() == "synthetic":
        context.feature_data["post_id"] = retrieve_synthetic()
    else:
        context.feature_data["post_id"] = post_id

@step('I set the request body as')
def step_set_request_body(context):
    # Load the JSON payload from the multi-line string provided in the feature file.
    context.request_body = json.loads(context.text)

@step('I send a GET request to the endpoint')
def step_send_get_request(context):
    # Replace the {id} placeholder with the actual post id if needed.
    endpoint = context.endpoint
    context.response = requests.get(endpoint + f"/{context.feature_data["post_id"]}")

@step('I send a POST request to the endpoint')
def step_send_post_request(context):
    context.request_body = {
        "title": "foo",
        "body": "bar",
        "userId": context.feature_data["post_id"]
      }

    context.response = requests.post(context.endpoint, json=context.request_body)


@step('I send a DELETE request to the endpoint')
def step_send_delete_request(context):
    endpoint = context.endpoint
    context.response = requests.delete(endpoint + f"/{context.feature_data["post_id"]}")


@step('the response status code should be {expected_status:d}')
def step_check_status_code(context, expected_status):
    actual_status = context.response.status_code
    assert actual_status == expected_status, (
        f"Expected status code {expected_status} but got {actual_status}"
    )

@step('the response should contain "{text}"')
def step_check_response_content(context, text):
    response_text = context.response.text
    assert text in response_text, (
        f"Expected to find '{text}' in response, but got: {response_text}"
    )