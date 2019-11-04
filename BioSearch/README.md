# Gene RESTful API Structure

 Endpoint | HTTP Method | Parameters | Result |
----------|-------------|------------|--------|
 gene/:name | **GET** | First n characters of gene name | Returns all gene entities that start with 'name' |
 gene/:name | **OPTIONS** | First n characters of gene name | Returns a description of the endpoint gene/:name |
 gene/:name/:species | **GET** | First n characters of gene name and exact species name | Returns all gene entities of a particular species that start with 'name' | 
 gene/:name/:species | **OPTIONS** | First n cha racters of gene name and exact species name | Returns a description of the endpoint gene/:name/:species |