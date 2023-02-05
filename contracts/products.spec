Feature: Products API

  Background:
    Given openapi ./documentation.yaml

  Scenario Outline: Get Product Success
    When GET /v1/products/(id:number)
    And request-header Accept? (string)
    Then status 400
    Examples:
      | id  | Accept           |
      | 1.1 | application/json |

  Scenario Outline: Get Product Not Found Error
    When GET /v1/products/(id:number)
    And request-header Accept? (string)
    Then status 404
    Examples:
      | id  | Accept           |
      | 100 | application/json |

  Scenario Outline: Get Product Success
    When GET /v1/products/(id:number)
    And request-header Accept? (string)
    Then status 200
    Examples:
      | id | Accept           |
      | 1  | application/json |
      | 4  | application/json |

  Scenario Outline: Products List Success
    When GET /v1/products?category=(category:string)&q=(q:string)
    And request-header Accept? (string)
    Then status 200
    Examples:
      | Accept           | category    | q       |
      | application/json |             | samsung |
      | application/json | laptops     |         |
      | */*              | smartphones | HP      |
      | */*              |             |         |
