Feature: Products API

  Background:
    Given openapi ./documentation.yaml

  Scenario Outline: Get Product Success
    When GET /v1/products/100
    Then status 404
