Feature:
  @login_tests
  Scenario Outline:Login validation with Valid and Invalid credentials
        Given The user is on the login page
        When  The user enters <username> and <password> and login
        And   Click on login button
        Then  The valid user gets <result> and land on Dashboard
        But  The Invalid user gets <result> and login error

        Examples:
          | username                       | password   | result                      |
          | vigneswaranprathibha@gmail.com | VZidane$23 | Dashboard                   |
          |                                | VZidane$23 | Email required!             |
          | prathibha@gmail.com            |            | Password required!          |

