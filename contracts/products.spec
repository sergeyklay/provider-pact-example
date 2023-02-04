Feature: Products API

  Background:
    Given openapi ./documentation.yaml

  Scenario Outline: Get Product Not Found Error
    When GET /v1/products/(id:number)
    Then status 404
    Examples:
      | id  |
      | 100 |

  Scenario Outline: Get Product Success
    When GET /v1/products/(id:number)
    Then status 200
    Examples:
      | id |
      | 1  |

  Scenario Outline: Products List Success
    When GET /v1/products
    Then status 200
