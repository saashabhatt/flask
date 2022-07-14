### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  A lot of the differences in Python and Javascript are related to their differences in 
  syntax. Apart from that, Python generally throws more errors than Javascript. For 
  instance when a function is passed with incorrect parameters, Python throws an error
  whereas Javascript assigns undefined to these variables. Python also allows comparison 
  of dictionaries and lists whereas Javascript does not.  

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  Use the dict.get method. If the key does not except, the method returns
  None. For example:
  ```py
  dict.get(c)
  ```
  You can also use an if-else statement student to check if the key exist.

  ```py
  if c in dict:
    return dict['c']
  else
    return None
  ```

- What is a unit test?
  A testing method in which individual units of source code are tested to see if they
  are fit for use. 

- What is an integration test?
  A testing method in which functional modules are tested as a group to see if they work
  as expected. Examples include testing a route view function in flask. 

- What is the role of web application framework, like Flask?
  Flask provides tools and features to define the framework for responding to requests
  made by the client. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?
  Pass the variable as a parameter in app.route and then pass the parameter in the
  view function. For example,
  ```py
  @app.route('/forex/<currency>)
    def convert(currency):
      currency = currency
  ```

- How do you collect data from the query string using Flask?
  Query strings can be picked up from the request.args dictionary
  ```py
  @app.route('/something')
    def get_something():
      key = request.args.get("something")
  ```


- How do you collect data from the body of the request using Flask?
  Similar to the above, you use the request.form dictionary
  ```py
  @app.route('/something')
  def get_something():
      key = request.form.get('something')
```

- What is a cookie and what kinds of things are they commonly used for?
  Cookies are pieces of information (key-value pairs) that are used to identify the client by the server. These are stored on the client computer. The key is the domain and value is the information sent by the server to 
  the browser. Cookies are used to enhance user experience by allowing the user to return 
  where they previously stopped. For example, a user who has added items to their shopping 
  cart can return to adding more items or purchasing those items if the client stopped
  browsing after adding items to the cart. 

- What is the session object in Flask?
  Session objects are stored on the server side and similar to a cookie is a key value pair
  that is used to identify the client to allow for an enhanced browsing experience.

- What does Flask's `jsonify()` do?
  Converts json data in python to json string
