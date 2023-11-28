# Albums Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._ 

## 1. Design and create the Table

n/a - created


## 2. Create Test SQL seeds

n/a - data exists

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
class Album(id, title, release_year, artist_id)

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = 0
        self.title = ""
        self.release_year = ""
        self.artist_id = 0

    def __eq__()
    # test something = something else

    def __repr__()
    # makes string prettier
```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*



## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class StudentRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of Album objects.

    # Gets a single record by its ID
    # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT title, release_year, artist_id FROM albums WHERE id = $1;

        # Returns an array of Album objects.

        # Add more methods below for each operation you'd like to implement.

    def create(self, album):
        #Executes SQL query:
        #Insert title, release_year, artist_id to albums
        #Does not return

    def delete(self, album):
        #Execute SQL query:
        #Delete from albums where id = x
        #does not return

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.



```python
#test_artist:
def test_artist_constructs():
def test_artists_format_nicely():
def test_artists_are_equal():

#test_artist_repository.py

def test_get_all_albums():

def test_find_single():

def test_create_album():

def test_delete_album():
```


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->