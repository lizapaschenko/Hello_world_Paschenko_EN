SELECT product_id, count (*)

FROM suppliers

group by product_id 

order by product_id ;
