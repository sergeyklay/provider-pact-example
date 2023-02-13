Feature: Foo API

  Background:
    Given openapi ./foo-api.yaml

  Scenario Outline: Delete foo
    When DELETE /v1/foo/(id:string)
    Then status 204
    Examples:
      | id                          |
      | CAC10D70-0000-0000-000030AA |
