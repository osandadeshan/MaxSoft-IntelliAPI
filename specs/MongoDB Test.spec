MongoDB Test Specification
==========================
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/30/2018
Time         : 9:14 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



MongoDB Test
------------
* Given a user need to connect to the "deckservice_qaint" Mongo database and "user_decks" Collection
* And the user set the MongoDB Authentication as follows
     |Configuration                                   |Configuration Value                                  |
     |------------------------------------------------|-----------------------------------------------------|
     |Is authentication credentials required?         |No                                                   |
     |Username                                        |N/A                                                  |
     |Source                                          |N/A                                                  |
     |Password                                        |N/A                                                  |
* When the user executes the Mongo query using key as "title" and value as "API Deck3"