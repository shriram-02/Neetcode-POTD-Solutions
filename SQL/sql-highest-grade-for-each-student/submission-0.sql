SELECT student_id, exam_id, score
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY student_id
               ORDER BY score DESC, exam_id ASC
           ) AS rn
    FROM exam_results
) t
WHERE rn = 1
ORDER BY student_id;