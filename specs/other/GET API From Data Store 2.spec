# Invoke GET API From Data Store Without Authentication Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 1/20/2021
Time            : 1:58 PM
Description     : This is an executable specification file

tags: get_api, regression


    |JSON Path|Expected Response Status Code|
    |---------|-----------------------------|
    |$[0].url |200                          |
    |$[1].url |200                          |
    |$[2].url |200                          |
    |$[3].url |400                          |


## Invoke GET Request from a response's JSON Path value without authentication
* Given that a user needs to invoke "Get urls"
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |App-Name     |no                 |               |                        |IntelliAPI                         |
   |Organization |no                 |               |                        |MaxSoft                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                                  |
   |--------------|-------------------|---------------|------------------------|------------------------------------------------|
   |$[0].name     |no                 |               |                        |First photo                                     |
   |$[1].name     |no                 |               |                        |Second photo                                    |
   |$[3].name     |no                 |               |                        |Get all tasks with auth header                  |
* And the user saves an API request url in the JSON Path <JSON Path> to a data store
* And invoke a GET request from the API request url saved in the data store
* Then the status code for the request is <Expected Response Status Code>