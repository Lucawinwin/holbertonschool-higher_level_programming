-- List all cities contained in database "hbtn_0d_usa"
Select cities.id, cities.name,states.name
From cities
JOIN states ON cities.state_id = states.id;
