SELECT p.name, pr.price
FROM prices AS pr
JOIN products AS p ON pr.product_id = p.id;
