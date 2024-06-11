-- Task 2. Best Band ever - ranks country origins of bands
-- Script can be executed on any db
SELECT DISTINCT 'origin', SUM('fans') as 'nb_fans' FROM 'metal_bands'
GROUP BY 'origin'
ORDER BY 'nb_fans' DESC;

