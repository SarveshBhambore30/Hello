Feature: OrangeHRM Login
    @valid_login
    Scenario: Login to OrangeHRM with valid parameter
        Given I launch chrome browser
        When I open orange hrm homepage
        And Enter username "Admin" and password "admin123"
        And Click on Login button
        Then User must successfully login to the HRM Dashboard page

    @multiple_login
    Scenario Outline: Login to OrangeHRM with multiple parameters
        Given I launch chrome browser
        When I open orange hrm homepage
        And Enter username "<username>" and password "<password>"
        And Click on Login button
        Then User must successfully login to the HRM Dashboard page

        Examples:
            | username | password |
            | Admin    | admin123 |
            | admin123 | Admin    |
            | adminxy  | admin123 |
            | admin    | adminxy  |
