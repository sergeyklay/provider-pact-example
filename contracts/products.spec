Feature: Single product API

  Background:
    Given openapi ./documentation.yaml

  Scenario Outline: Getting a product that does not exist
    When GET /v1/products/(id:number)
    Then status 404
    Examples:
      | id       |
      | 10000000 |

  Scenario Outline: Successful getting product by ID
    When GET /v1/products/(id:number)
    Then status 200
    Examples:
      | id |
      | 42 |

  Scenario Outline: Deleting a product that does not exist
    When DELETE /v1/products/(id:number)
    Then status 404
    Examples:
      | id       |
      | 10000000 |

  Scenario Outline: Successful deleting product by ID
    When DELETE /v1/products/(id:number)
    Then status 204
    Examples:
      | id   |
      | 7777 |

  Scenario Outline: Successful getting list of products
    When GET /v1/products?expanded=(number)
    Then status 200
    Examples:
      | expanded |
      | 1        |

  Scenario Outline: Successful getting list of products in a given category
    When GET /v1/products?category=(string)&expanded=(number)
    Then status 200
    Examples:
      | category    | expanded |
      | smartphones | 1        |
      | laptops     | 1        |
      |             | 1        |

  Scenario Outline: Successful getting list of products using search term
    When GET /v1/products?q=(string)
    Then status 200
    Examples:
      | q     | expanded |
      | phone | 1        |
      | HP    | 1        |
      |       | 1        |
