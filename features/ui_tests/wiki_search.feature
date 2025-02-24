@gui
Feature: Test wiki
  As a tester
  I want to be able to search things on wikipedia
  In order to find what I'm looking for

  Scenario: Test your wikipedia visit
    Given I navigate to "https://en.wikipedia.org/"
    When I search for "Charles Darwin"
    Then The result page should contain "Origin of Species"