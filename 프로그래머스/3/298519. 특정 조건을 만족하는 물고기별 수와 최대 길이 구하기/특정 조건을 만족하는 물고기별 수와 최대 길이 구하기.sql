SELECT 
    COUNT(ID) AS FISH_COUNT, 
    MAX(LENGTH) AS MAX_LENGTH, 
    FISH_TYPE
FROM 
    (SELECT ID, FISH_TYPE, 
          CASE WHEN LENGTH < 10 THEN 10 ELSE LENGTH END AS LENGTH
     FROM FISH_INFO) AS ADJUSTED_FISH_INFO
WHERE 
    FISH_TYPE IN (
        SELECT FISH_TYPE
        FROM (
            SELECT FISH_TYPE, 
                   AVG(CASE WHEN LENGTH < 10 THEN 10 ELSE LENGTH END) AS AVG_LENGTH
            FROM FISH_INFO
            GROUP BY FISH_TYPE
            HAVING AVG(CASE WHEN LENGTH < 10 THEN 10 ELSE LENGTH END) >= 33
        ) AS AVG_FILTER
    )
GROUP BY 
    FISH_TYPE
ORDER BY 
    FISH_TYPE;
