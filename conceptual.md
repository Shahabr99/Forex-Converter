### Conceptual Exercise

Answer the following questions below:

1. What are important differences between Python and JavaScript?

   One of the differences is syntax. For example in Python there is no var, let or const and for code blocks, we should use indentation rather than curly braces. Python handles data types in a different way compared to JavaScript. In Python variables have a specific data type that cannot be changed but in JavaScript which is a loose-typed language, data type of variables can be changed.

2. Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
   can try to get a missing key (like "c") _without_ your programming
   crashing.

   - Using dictionary method "get()"
   - Using try and except

3. What is a unit test?  
   Testing smaller units like functions or modules to see if they are working properly in isolation.

4. What is an integration test?  
   This type of testing verifies if different components or modules functioning correctly. It makes sure different components are working together properly.

5. What is the role of web application framework, like Flask?  
   Frameworks like Flask help developers to create web applications quickly and easily.

6. You can pass information to Flask either as a parameter in a route URL
   (like '/foods/pretzel') or using a URL query param (like
   'foods?type=pretzel'). How might you choose which one is a better fit
   for an application?  
   Chossing between these two depends on different factors such as data type, data complexity, or security.

- How do you collect data from a URL placeholder parameter using Flask?  
  Using route decorator.

- How do you collect data from the query string using Flask?
  By using request.args

- How do you collect data from the body of the request using Flask?

  By using request.form.get

- What is a cookie and what kinds of things are they commonly used for?  
  A cookie is a small piece of data that a website stores on a user's computer or mobile device.They are used for session management, personalization, and tracking.
- What is the session object in Flask?  
   session object is a way to store information that is specific to a user across multiple requests.

- What does Flask's `jsonify()` do?  
  Jsonify is a function that converts a Python dictionary to a JSON-formatted string.
