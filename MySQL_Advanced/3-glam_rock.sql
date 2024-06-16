-- TAsk 3. Old school band - lists all bands
-- bands will be ranked by their longevity
SELECT
	band_name,
	IFNULL(split, 2024) - formed AS lifespan
FROM
	metal_bands
WHERE
	FIND_IN_SET('Glam rock', style) > 0
ORDER BY
	lifespan DESC;

