# Coding Challenge

• Connected Cities
  
  1. download cities.txt and connected_cities.py
  2. run connected_cities.py from terminal
  3. unit testing will be executed automatically

• Race simulation

  1. download simulated_race.py
  2. Optional: adjust any parameters within simulated_race.py - [num_samples, distance, accelerations/velocities for car, motorbike, truck, A = frontal area of vehicle, drag coefficient (cd_car, cd_motorbike, cd_truck)
  3. The simulation uses basic physics formulae to simulate the time needed for each vehicle to complete the race given the set of parameters above
  4. run simulated_race.py from terminal to view simulation results
  5. plotted in race_results.png

• Simple Rest/Microservice

  1. download simple_rest.py
  2. run simple_rest.py to serve up the data
  3. run a POST command using:
      
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
