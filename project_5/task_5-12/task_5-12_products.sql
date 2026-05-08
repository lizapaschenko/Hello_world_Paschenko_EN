SELECT category, count (*)

FROM products

group by category ;

;

SELECT category, count (*)

FROM products

group by category 

order by count (*) DESC;
