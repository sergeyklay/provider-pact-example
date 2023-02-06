Feature: Products API

  Background:
    Given openapi ./documentation.yaml

  Scenario Outline: Bad request when getting the product by ID
    When GET /v1/products/(id:number)
    Then status 400
    Examples:
      | id  |
      | 1.1 |

  Scenario Outline: Product not found
    When GET /v1/products/(id:number)
    Then status 404
    Examples:
      | id  |
      | 100 |

  Scenario Outline: Successful getting product by ID
    When GET /v1/products/(id:number)
    Then status 200
    Examples:
      | id |
      | 1  |

  Scenario Outline: Successful getting list of products
    When GET /v1/products
    Then status 200

  Scenario Outline: Successful getting list of products in a given category
    When GET /v1/products?category=(category:string)
    Then status 200
    Examples:
      | category    |
      | smartphones |
      | laptops     |
      |             |

  Scenario Outline: Successful getting list of products using search term
    When GET /v1/products?q=(q:string)
    Then status 200
    Examples:
      | q     |
      | phone |
      | HP    |
      |       |
