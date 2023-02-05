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

  Scenario Outline: Successful getting list of products
    When GET /v1/products
    And request-header Accept? (string)
    Then status 200
    Examples:
      | Accept           |
      | application/json |
      | */*              |

  Scenario Outline: Successful getting list of products in a given category
    When GET /v1/products?category=(category:string)
    And request-header Accept? (string)
    Then status 200
    Examples:
      | Accept           | category    |
      | application/json | smartphones |
      | application/json | laptops     |
      | */*              | smartphones |
      | */*              |             |

  Scenario Outline: Successful getting list of products using search term
    When GET /v1/products?q=(q:string)
    And request-header Accept? (string)
    Then status 200
    Examples:
      | Accept           | q     |
      | application/json | phone |
      | application/json |       |
      | */*              | HP    |
      | */*              |       |
