-- 코드를 입력하세요
SELECT U.user_id,U.nickname
,concat(U.city,' ',U.street_address1,' ',U.street_address2) AS 전체주소
,concat(LEFT(tlno,3), '-', MID(tlno,4,4),'-', RIGHT(tlno,4)) AS 전화번호
FROM used_goods_board B join used_goods_user U ON B.writer_id = U.user_id
GROUP BY writer_id
HAVING count(writer_id) >= 3
ORDER BY U.user_id DESC