Feature:
  @login_tests
  Scenario Outline:Login validation with Valid and Invalid credentials
        Given The user is on the login page
        When  The user enters <username> and <password> and login
        And   Click on login button
        Then  The user gets <result>

        Examples:
          | username                       | password   | result                      |
          | vigneswaranprathibha@gmail.com | VZidane$23 | Dashboard                   |
          |                                | VZidane$23 | Email required!             |
          | prathibha@gmail.com            |            | Password required!          |

