
# Gene RESTful API Structure

 Endpoint | HTTP Method | Result |
----------|-------------|--------|
 gene/:name/ | **GET** | Returns all gene entities that start with 'name' |
 gene/:name/ | **OPTIONS** | Returns a description of the endpoint gene/:name |
 gene/:name/:species/ | **GET** | Returns all gene entities of a particular species that start with 'name' | 
 gene/:name/:species/ | **OPTIONS** | Returns a description of the endpoint gene/:name/:species |

### Parameters
* :name - represents first n characters of the gene name
* :species - represents exact name of species

# Deployed API Version
https://alv2017.pythonanywhere.com/gene/

**Note:** In browsable API (and in all the cases when 'Accept: text/html' content type is requested) the result set is limited to 5 instances, and it serves solely for demonstration purposes.

### Sample Calls
* https://alv2017.pythonanywhere.com/gene/zswim/
* https://alv2017.pythonanywhere.com/gene/zswim/neovison_vison/

# Project Requirements

1. Python v3.6.8
2. Django v2.2.6
3. djangorestframework v3.10.3
4. mysqlclient v1.4.4 (Python package)
5. MySQL database 5.6.46


# Automated Tests

The automated tests should be run in development environment only.
The test can be run by issuing the command in the project command shell:
```
python manage.py test --keepdb
```
 
# Project Assignment Follow Up

I didn't manage to complete the project 100%, so I decided just to write down what has been done so far.
I'm going to need a couple more days to finish the whole project. I will go through each assignment task
step by step, and explain what I have done and what I haven't done. I marked the tasks that I have 
completed with (+) sign, and the tasks that I didn't manage to complete with the (-) sign.

### Assignment

Using Python, create a simple RESTful API service with a single endpoint which allows users
to search for a gene by its name in a public Ensembl database.

**Comment:** I used Django and DjangoREST frameworks. 

- (+) Publish your answer in GitHub. Your answer should be presented as just one GitHub URL.

- (-) Your applications will be tested using the methods described in 
      https://github.com/jouanmarcriera/vagrant-file
      
**Comment:** The project is not ready for testing. 

### Business Rules

1. (+) The endpoint should accept the following parameters:

	* **name (required)** - minimum 3 letters prefix of a searched gene name case insenitive match;
	* **species (optional)** - full name of the target species;
	
**Comment:** 
* I created two endpoints gene/:name/ and gene/:name/:species/.
* There are genes with names of 1 or 2 characters, so I decided that the API accepts 
  name entries having 1 or more characters. In case when the user enters 1 or 2 characters
  the exact name match is implemented. In case when the user enters 3 or more characters,
  the prefix name match is implemented.
  
2. (+) The endpoint should return a JSON response with all the entities matching the searh criteria.
	  Response should contain the following fields: 
	    **id** (db column: stable_id), 
	  	**name** (db column: display_name),
	  	**species** (db column: species).
	  
**Comment:** My endpoints return **JSON** and **text/html** responses. This is in order to implement 
Browsable API feature. In production environment it is easy to remove the support for
**text/html** responses.

3. (+) The service should use the public Ensembl database as its data source.

**Comment:** The problem is that the current implementation of the public Ensembl database
does not satisfy our API needs. My decision was to download the table that the API relies
upon and set it for the API needs. In order to meet the requirments as close as possible
I implemented the opportunity to use the copy of Ensembl database as a remote read-only database.

4. (+) Service should answer only get queries.

**Comment:** Currently the service answers **OPTIONS** requests as well. This is in order to 
document the API. This option can be easily removed, however I think that it is quite nice
API feature, and so I decided to keep it.

### Additional Requirements

1. (+) Provide tests for your applications with sufficient documentations on how to run them.

**Comment:** At the very top of the README.md I provided the documentation of the API structure,
I hope that this document provides a clear idea on how to implement the tests. I also managed
to implement automated API testing.

2. (+) Automate the tests.

**Comment:** The automation tests are located in geneapi/tests directory.
Currently the tests check API calls against the calls to DB. It was a challenge
to implement automated tests, due to Django restrictions when testing on multiple databases. 

3. (-) Include sufficient details on how to run your app using Docker, with minimum number 
of steps possible.

**Comment:** I will do my best to deploy the API today, but I'm afraid that I will be 
missing the deadline.

4. (-) Prepare documentation on how to run you app using Docker, with minimum number of steps
possible.

5. (+) Document you API. Desirable: OpenAPI(Swagger) description.

**Comment:** I provided the API endpoint description at the very top of the README.md.
I also used BrowsableAPI feature, so the user/tester can read the method documentation
in the browser, and use GUI to test the API calls.

  
  


















