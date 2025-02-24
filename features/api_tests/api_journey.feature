Feature: API Service Testing
  As a software tester
  I want to test a demo api
  In order to make use of the demo site

  Scenario: POST Request with dynamic payload
    Given I set the API endpoint to "https://jsonplaceholder.typicode.com/posts"
    And I set the post id to "auto"
    When I send a POST request to the endpoint
    Then the response status code should be 201
    And the response should contain "id"

  Scenario: GET Request with dynamic post id
    Given I set the API endpoint to "https://jsonplaceholder.typicode.com/posts"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And the response should contain "userId"

  Scenario: DELETE Request with dynamic post id
    Given I set the API endpoint to "https://jsonplaceholder.typicode.com/posts"
    When I send a DELETE request to the endpoint
    Then the response status code should be 200