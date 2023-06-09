# This will be a practice project for working with classes

I would like to create a few classes to simulate the database structure of a study aid. It will have question and answer objects, people/user objects, and subject objects, and library objects.

#### The user:

- will have an id
- will have a user name
- will have a dict of questions, keyed to subject

#### The question/answer:

- create id
- store the question and answer
- have a subject
- save created by information
- saves if pupblic or not

### The Library:

- used to create user id and question id for tracking
- stores all the question objects
- allow edits/deletions only if user created also requests (?)
- tracks all questions by subject
