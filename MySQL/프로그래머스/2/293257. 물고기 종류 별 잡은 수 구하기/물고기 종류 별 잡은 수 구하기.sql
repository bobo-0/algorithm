SELECT COUNT(*) AS 'FISH_COUNT', N.FISH_NAME
FROM FISH_NAME_INFO AS N
JOIN FISH_INFO I
    ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY N.FISH_NAME
ORDER BY 1 DESC;