INSERT INTO courses_test (question, correct_answer, module_id) VALUES
-- Python Questions

('What keyword is used to create a class in Python?', 'class', 2),
('How do you call a function in Python?', 'my_function()', 2),
('What is the default return value of a function in Python?', 'None', 2),
('How do you handle exceptions in Python?', 'try/except', 2),
('What is a lambda function in Python?', 'An anonymous function', 2),

('What is inheritance in OOP?', 'A way to create a new class using a base class', 3),
('What is a constructor in Python?', 'A special method to initialize an object', 3),
('What is polymorphism?', 'The ability to use a common interface for different data types', 3),
('What is the difference between class and instance variables?', 'Class variables are shared; instance variables are unique to each object', 3),
('What does self refer to in a class method?', 'The instance of the class', 3),

('Which command is used to install a library in Python?', 'pip install', 4),
('What does the NumPy function np.array() do?', 'Creates a NumPy array', 4),
('How do you import a library in Python?', 'import library_name', 4),
('What is Pandas primarily used for?', 'Data manipulation and analysis', 4),
('Which library is used for web scraping in Python?', 'BeautifulSoup', 4),

('How do you read a text file line by line in Python?', 'for line in file:', 5),
('What is the mode for writing to a file in Python?', '"w"', 5),
('How do you close a file in Python?', 'file.close()', 5),
('What method is used to write to a file in Python?', 'file.write()', 5),
('What happens if you try to read a closed file?', 'An IOError is raised', 5),

('What is an exception in Python?', 'An error that occurs during program execution', 6),
('What is the purpose of the finally block?', 'To execute code regardless of an exception', 6),
('What does raise do in Python?', 'Triggers an exception', 6),
('How do you catch multiple exceptions?', 'Using multiple except blocks', 6),
('What is the AssertionError?', 'An error raised when an assertion fails', 6),

('What library is commonly used for database interaction in Python?', 'SQLite', 7),
('How do you connect to a SQLite database in Python?', 'sqlite3.connect("database.db")', 7),
('What is an ORM?', 'Object-Relational Mapping', 7),
('How do you execute a SQL query in Python?', 'cursor.execute("SQL QUERY")', 7),
('What method is used to commit a transaction in Python?', 'connection.commit()', 7),

('What is web scraping?', 'Extracting data from websites', 8),
('What is the requests library used for?', 'Making HTTP requests', 8),
('How do you parse HTML in Python?', 'Using BeautifulSoup', 8),
('What method retrieves the content of a webpage?', 'response.content', 8),
('How can you find elements by class name using BeautifulSoup?', 'soup.find_all(class_="class_name")', 8),

('What is unit testing?', 'Testing individual components of a program', 9),
('Which library is commonly used for testing in Python?', 'unittest', 9),
('What does assert do in testing?', 'Checks if a condition is true', 9),
('What is the purpose of mock objects in testing?', 'To simulate the behavior of real objects', 9),
('How do you run tests using unittest?', 'python -m unittest', 9),

('What is the final project in Python?', 'A comprehensive project applying learned concepts', 10),

-- Java Questions
('What is the output of System.out.println(2 + 3);?', '5', 11),
('Which of the following is a valid variable name in Java?', 'myVar', 11),
('What is the correct syntax for defining a method in Java?', 'void myMethod() {}', 11),
('Which library is commonly used for data structures in Java?', 'Java Collections Framework', 11),
('What is the correct syntax for reading a file in Java?', 'new FileReader("file.txt")', 11),

('What keyword is used to define a method in Java?', 'void', 12),
('How do you call a method in Java?', 'myMethod();', 12),
('What is method overloading?', 'Defining multiple methods with the same name but different parameters', 12),
('What is the return type of the main method in Java?', 'void', 12),
('How do you handle exceptions in Java?', 'try/catch', 12),

('What is inheritance in OOP?', 'A way to create a new class from an existing class', 13),
('What is a constructor in Java?', 'A special method that initializes objects', 13),
('What is polymorphism in Java?', 'The ability for a method to do different things based on the object', 13),
('What is an abstract class?', 'A class that cannot be instantiated', 13),
('What is an interface in Java?', 'A reference type that can contain only constants, method signatures, and nested types', 13),

('Which command is used to import a package in Java?', 'import packageName;', 14),
('What does the ArrayList class do?', 'Stores a resizable array of elements', 14),
('How do you create a HashMap in Java?', 'new HashMap<>();', 14),
('What is the purpose of the Collections class?', 'Provides static methods for operating on collections', 14),
('What is a Set in Java?', 'A collection that does not allow duplicate elements', 14),

('How do you read a file in Java?', 'Using FileReader', 15),
('What is the mode for writing to a file in Java?', 'FileWriter', 15),
('How do you close a file in Java?', 'file.close();', 15),
('What happens if you try to read a closed file in Java?', 'IOException is thrown', 15),
('What is a BufferedReader?', 'A class for reading text from a character input stream', 15),

('What is an exception in Java?', 'An event that disrupts the normal flow of execution', 16),
('What is the purpose of the finally block?', 'To execute code regardless of an exception', 16),
('What does throw do in Java?', 'Indicates that a method can throw an exception', 16),
('What is a checked exception?', 'An exception that must be either caught or declared in the method signature', 16),
('What is an unchecked exception?', 'An exception that does not need to be caught or declared', 16),

('What library is commonly used for database interaction in Java?', 'JDBC', 17),
('How do you connect to a database in Java?', 'DriverManager.getConnection(url, user, password)', 17),
('What is an ORM?', 'Object-Relational Mapping', 17),
('What method is used to execute a SQL query in Java?', 'Statement.executeQuery("SQL QUERY")', 17),
('What is a PreparedStatement?', 'A precompiled SQL statement for executing parameterized queries', 17),

('What is multithreading?', 'Executing multiple threads simultaneously', 18),
('What is the purpose of the synchronized keyword?', 'To control access to a block of code by multiple threads', 18),
('How do you create a thread in Java?', 'By implementing Runnable or extending Thread', 18),
('What is a thread pool?', 'A collection of pre-initialized threads for executing tasks', 18),
('What is a deadlock?', 'A situation where two threads are blocked forever, each waiting on the other', 18),

('What is unit testing in Java?', 'Testing individual units of code', 19),
('Which library is commonly used for testing in Java?', 'JUnit', 19),
('What does assert do in testing?', 'Checks if a condition is true', 19),
('How do you run tests using JUnit?', 'Using the JUnit test runner', 19),
('What is a test case in JUnit?', 'A method that contains assertions to verify behavior', 19),

('What is the final project in Java?', 'A comprehensive project applying learned concepts', 20),

-- .NET Questions
('What is the output of Console.WriteLine(2 + 3);?', '5', 21),
('Which of the following is a valid variable name in C#?', 'myVar', 21),
('What is the correct syntax for defining a method in C#?', 'void MyMethod() {}', 21),
('Which library is commonly used for data structures in .NET?', 'Collections', 21),
('What is the correct syntax for reading a file in C#?', 'File.ReadAllText("file.txt")', 21),

('What keyword is used to define a method in C#?', 'void', 22),
('How do you call a method in C#?', 'MyMethod();', 22),
('What is method overloading?', 'Defining multiple methods with the same name but different parameters', 22),
('What is the return type of the Main method in C#?', 'void', 22),
('How do you handle exceptions in C#?', 'try/catch', 22),

('What is inheritance in OOP?', 'A way to create a new class from an existing class', 23),
('What is a constructor in C#?', 'A special method that initializes objects', 23),
('What is polymorphism in C#?', 'The ability for a method to do different things based on the object', 23),
('What is an abstract class in C#?', 'A class that cannot be instantiated', 23),
('What is an interface in C#?', 'A reference type that defines a contract', 23),

('Which command is used to import a namespace in C#?', 'using namespace;', 24),
('What does the List<T> class do?', 'Stores a resizable array of elements', 24),
('How do you create a Dictionary in C#?', 'new Dictionary<TKey, TValue>();', 24),
('What is the purpose of the LINQ library?', 'To query collections in a more readable way', 24),
('What is a HashSet in C#?', 'A collection that does not allow duplicate elements', 24),

('How do you read a file in C#?', 'Using StreamReader', 25),
('What is the mode for writing to a file in C#?', 'FileMode.Create', 25),
('How do you close a file in C#?', 'file.Close();', 25),
('What happens if you try to read a closed file in C#?', 'IOException is thrown', 25),
('What is a StreamReader?', 'A class for reading characters from a byte stream', 25),

('What is an exception in C#?', 'An event that disrupts the normal flow of execution', 26),
('What is the purpose of the finally block in C#?', 'To execute code regardless of an exception', 26),
('What does throw do in C#?', 'Indicates that a method can throw an exception', 26),
('What is a checked exception in C#?', 'An exception that must be caught or declared', 26),
('What is an unchecked exception in C#?', 'An exception that does not need to be caught or declared', 26),

('What library is commonly used for database interaction in .NET?', 'Entity Framework', 27),
('How do you connect to a database in C#?', 'Using SqlConnection', 27),
('What is an ORM in .NET?', 'Object-Relational Mapping', 27),
('What method is used to execute a SQL query in C#?', 'SqlCommand.ExecuteReader()', 27),
('What is a DbContext in Entity Framework?', 'A class that manages database connections and entity objects', 27),

('What is LINQ?', 'Language Integrated Query', 28),
('How do you filter a collection using LINQ?', 'Using the Where() method', 28),
('What does the Select() method do in LINQ?', 'Projects each element into a new form', 28),
('What is deferred execution in LINQ?', 'The query is not executed until the results are enumerated', 28),
('How do you join two collections using LINQ?', 'Using the Join() method', 28),

('What is unit testing in .NET?', 'Testing individual units of code', 29),
('Which library is commonly used for testing in .NET?', 'MSTest or NUnit', 29),
('What does Assert do in testing?', 'Checks if a condition is true', 29),
('How do you run tests using MSTest?', 'Using the command line or Visual Studio test explorer', 29),
('What is a test case in NUnit?', 'A method that contains assertions to verify behavior', 29),

('What is the final project in .NET?', 'A comprehensive project applying learned concepts', 30);

