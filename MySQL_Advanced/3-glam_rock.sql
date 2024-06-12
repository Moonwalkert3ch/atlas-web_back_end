-- TAsk 3. Old school band - lists all bands
-- bands will be ranked by their longevity
SELECT
	band_name,
	TIMESTAMPDIFF(YEAR, forward, IFNULL(split, CURDATE())) AS lifespan
FROM
	metal_bands
WHERE
	main_style = 'Glam rock'
ORDER BY
	lifespan DESC;

