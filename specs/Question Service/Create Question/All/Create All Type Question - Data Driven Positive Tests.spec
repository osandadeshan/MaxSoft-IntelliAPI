Create All Type Question using Question Service - Data Driven Positive Tests Specification
==========================================================================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_all_type, create_question-positive_tests, positive, ci_ready


table: /resources/data_driven_test_csv/create_question/question_service/create_question_all_type-positive_tests.csv


* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name              |Value To Be Stored     |
    |---------------|---------------------------|-----------------------|
    |scenario       |deckId                     |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a question using a valid payload
---------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set               |
     |--------------------------------|-------------------|---------------|----------------------------|----------------------------------------|
     |#creatorId                      |n                  |               |                            |<creatorId>                             |
     |#creatorPlatform                |n                  |               |                            |<creatorPlatform>                       |
     |#creatoredSource                |n                  |               |                            |<creatoredSource>                       |
     |#creatoredType                  |n                  |               |                            |<creatoredType>                         |
     |#deckId                         |y                  |scenario       |deckId                      |                                        |
     |#kind                           |n                  |               |                            |<kind>                                  |
     |#isDeleted                      |n                  |               |                            |<isDeleted>                             |
     |#tempQuestionId                 |n                  |               |                            |<tempQuestionId>                        |
     |#learningObjectives             |n                  |               |                            |<learningObjectives>                    |
     |#imageUrl                       |n                  |               |                            |<imageUrl>                              |
     |#media                          |n                  |               |                            |<media>                                 |
     |#questionPrompt                 |n                  |               |                            |<prompt>                                |
     |#promptType                     |n                  |               |                            |<promptType>                            |
     |#timeout                        |n                  |               |                            |<timeout>                               |
     |#rationale                      |n                  |               |                            |<rationale>                             |
     |#boxId                          |n                  |               |                            |<boxId>                                 |
     |#correctAttempts                |n                  |               |                            |<correctAttempts>                       |
     |#inCorrectAttempts              |n                  |               |                            |<inCorrectAttempts>                     |
     |#lastAswered                    |n                  |               |                            |<lastAswered>                           |
     |#questionId                     |n                  |               |                            |<questionId>                            |
     |#skips                          |n                  |               |                            |<skips>                                 |
     |#userId                         |n                  |               |                            |<userId>                                |
     |#correctAnswerList              |n                  |               |                            |<correctAnswerList>                     |
     |#answer1Id                      |n                  |               |                            |<answer1Id>                             |
     |#answer1Value                   |n                  |               |                            |<answer1Value>                          |
     |#answer1Type                    |n                  |               |                            |<answer1Type>                           |
     |#answer1CaseSensitive           |n                  |               |                            |<answer1CaseSensitive>                  |
     |#answer2Id                      |n                  |               |                            |<answer2Id>                             |
     |#answer2Value                   |n                  |               |                            |<answer2Value>                          |
     |#answer2Type                    |n                  |               |                            |<answer2Type>                           |
     |#answer2CaseSensitive           |n                  |               |                            |<answer2CaseSensitive>                  |
     |#answer3Id                      |n                  |               |                            |<answer3Id>                             |
     |#answer3Value                   |n                  |               |                            |<answer3Value>                          |
     |#answer3Type                    |n                  |               |                            |<answer3Type>                           |
     |#answer3CaseSensitive           |n                  |               |                            |<answer3CaseSensitive>                  |
     |#answer4Id                      |n                  |               |                            |<answer4Id>                             |
     |#answer4Value                   |n                  |               |                            |<answer4Value>                          |
     |#answer4Type                    |n                  |               |                            |<answer4Type>                           |
     |#answer4CaseSensitive           |n                  |               |                            |<answer4CaseSensitive>                  |
     |#answer5Id                      |n                  |               |                            |<answer5Id>                             |
     |#answer5Value                   |n                  |               |                            |<answer5Value>                          |
     |#answer5Type                    |n                  |               |                            |<answer5Type>                           |
     |#answer5CaseSensitive           |n                  |               |                            |<answer5CaseSensitive>                  |
     |#tags                           |n                  |               |                            |<tags>                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.media                          |<media>                                                  |
     |$.question.prompt                         |<prompt>                                                 |
     |$.question.imageUrl                       |<imageUrl>                                               |
     |$.question.promptType                     |<promptType>                                             |
     |$.deleted                                 |<isDeleted>                                              |
     |$.stats.questionId                        |<questionId>                                             |
     |$.stats.userId                            |<userId>                                                 |
     |$.stats.boxId                             |<boxId>                                                  |
     |$.stats.skips                             |<skips>                                                  |
     |$.stats.inCorrectAttempts                 |<inCorrectAttempts>                                      |
     |$.stats.correctAttempts                   |<correctAttempts>                                        |
     |$.learningObjectives                      |<learningObjectives>                                     |
     |$.rationale                               |<rationale>                                              |
     |$.tags                                    |<tags>                                                   |
     |$.creatorId                               |<creatorId>                                              |
     |$.creatoredType                           |<creatoredType>                                          |
     |$.creatorPlatform                         |<creatorPlatform>                                        |
     |$.creatoredSource                         |<creatoredSource>                                        |
     |$.tempQuestionId                          |<tempQuestionId>                                         |
     |$.correctAnswers[0]                       |<correctAnswerList>                                      |
//     |$.answers[0].id                           |<answer1Id>                                              |
//     |$.answers[0].value                        |<answer1Value>                                           |
//     |$.answers[0].type                         |<answer1Type>                                            |
//     |$.answers[0].caseSensitive                |<answer1CaseSensitive>                                   |
//     |$.answers[1].id                           |<answer2Id>                                              |
//     |$.answers[1].value                        |<answer2Value>                                           |
//     |$.answers[1].type                         |<answer2Type>                                            |
//     |$.answers[1].caseSensitive                |<answer2CaseSensitive>                                   |
//     |$.answers[2].id                           |<answer3Id>                                              |
//     |$.answers[2].value                        |<answer3Value>                                           |
//     |$.answers[2].type                         |<answer3Type>                                            |
//     |$.answers[2].caseSensitive                |<answer3CaseSensitive>                                   |
//     |$.answers[3].id                           |<answer4Id>                                              |
//     |$.answers[3].value                        |<answer4Value>                                           |
//     |$.answers[3].type                         |<answer4Type>                                            |
//     |$.answers[3].caseSensitive                |<answer4CaseSensitive>                                   |