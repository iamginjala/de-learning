--joins on public data set 

select employees.name as emp_name, employees.role as emp_role,department.name as dep_name 
from my-first-project-412721.employee_data.employees 
full outer join my-first-project-412721.employee_data.department
on employees.department_id = department.department_id

-- sub queries

SELECT
	station_id,
	num_bikes_available,
	(SELECT
		AVG(num_bikes_available)
	FROM bigquery-public-data.new_york.citibike_stations) AS avg_num_bikes_available
FROM bigquery-public-data.new_york.citibike_stations;

-- the above query can be written using window funtion 

SELECT station_id, num_bikes_available, AVG(num_bikes_available) over() as avg_bike  FROM `bigquery-public-data.new_york.citibike_stations`

--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

select sum(c.population) 
from city c 
join country 
on c.countrycode = country.code
where country.continent = 'Asia'


-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
select c.name 
from city c
join country co
on c.countrycode = co.code
where co.continent = 'Africa'

--Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

select co.continent, floor(avg(c.population))
from city c
join country co
on c.countrycode = co.code
group by 1