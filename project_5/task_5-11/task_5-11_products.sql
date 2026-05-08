SELECT *

FROM products

WHERE category = 'Электроника' ;

;


SELECT *

FROM products

WHERE category = 'Одежда' and name like '%женские%' ;

;


SELECT *

FROM products

WHERE category = 'Продукты' or category = 'Книги' ;

;


SELECT *

FROM products

WHERE not category = 'Бытовая техника' ;

;

SELECT *

FROM products

WHERE category = 'Электроника' or category = 'Одежда' or category = 'Книги';

;

SELECT *

FROM products

WHERE category = 'Электроника' and name like '%Samsung%' or category = 'Бытовая техника' ;
;


SELECT *

FROM products

WHERE (category in ('Электроника', 'Бытовая техника', 'Одежда')
 and id between 1 and 15 
and not name like '%Samsung%' ) 
or category = 'Книги'

;


