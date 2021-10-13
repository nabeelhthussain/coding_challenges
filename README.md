# Coding Challenge

• Connected Cities
  
  1. run connected_cities.py from terminal
  2. the program will read the data from cities.txt
  3. unit testing will be executed 

• Race simulation

  1. Optional: adjust any parameters within simulated_race.py 
  2. run simulated_race.py from terminal to view simulation results

• Simple Rest/Microservice

  1. run simple_rest.py to serve up the data
  2. run a POST command using:
      
      curl -XPOST http://127.0.0.1:8080/company/Apple -H "Content-Type: application/json"  --data '{ "company": "Apple", "views": "1199", "title": "Technology" }'
      
      ## OUTPUT:
      
      {
          "company": "Apple",
          "views": "1199",
          "title": "Technology"
      }

  3. run a GET command using:
 
      curl -XGET http://127.0.0.1:8080/company/Apple
      
      ## OUTPUT:
      
      {
          "company": "Apple",
          "views": "1199",
          "title": "Technology"
      }
