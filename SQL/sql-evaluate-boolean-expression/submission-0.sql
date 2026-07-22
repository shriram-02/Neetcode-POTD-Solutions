SELECT 
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '>' THEN
            CASE WHEN v1.value > v2.value THEN 'true' ELSE 'false' END
        WHEN e.operator = '<' THEN
            CASE WHEN v1.value < v2.value THEN 'true' ELSE 'false' END
        WHEN e.operator = '=' THEN
            CASE WHEN v1.value = v2.value THEN 'true' ELSE 'false' END
    END AS value
FROM expressions e
JOIN variables v1
ON e.left_operand = v1.name
JOIN variables v2
ON e.right_operand = v2.name;