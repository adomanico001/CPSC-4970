In this project you will create an interactive program to manage a todo list. You should create in a single python file called "todo_console_ui.py". Since we haven't introduced classes and functions yet, our data model will be simple.

Your "todo list" must be a list of 3-tuples where each tuple has the following form: (completed, description, due date/time) where <i>completed</i> is a boolean, <i>description</i> is a string and <i>due date/time</i> is a datetime.datetime object.

Do not create your own classes for this project. The idea here is to get used to working with lists and tuples so if you skip ahead to classes, you'll defeat the purpose.

Your user interface must include the following actions:

<br>List ALL todo items
<br>List all incomplete todo items<br>
<br>List incomplete todo items due today<br>
<br>Add a todo item<br>
<br>Complete a todo item<br>
<br>Quit<br>

Your program does not have to handle user input errors (you can assume that the user will enter responses correctly).
The grader will expect your program to work just like the one in the sample interaction (same menu items, same input format, same output format).
