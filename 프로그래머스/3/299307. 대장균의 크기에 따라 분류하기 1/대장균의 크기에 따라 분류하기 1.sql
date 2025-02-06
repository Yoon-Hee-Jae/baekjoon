SELECT ID,
        CASE
            WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
            WHEN SIZE_OF_COLONY > 100 THEN 'MEDIUM'
            WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        END AS SIZE
FROM ECOLI_DATA
ORDER BY ID;
