SELECT product_id, count (*)

FROM prices

group by product_id 

;


SELECT product_id, AVG (price)

FROM prices

group by product_id 

;



SELECT product_id, MIN (price)

FROM prices

group by product_id 


;

;

SELECT product_id, MAX (price)

FROM prices

group by product_id 


;
