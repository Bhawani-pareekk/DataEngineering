SELECT 
    e.name AS employee_name,
    COALESCE(m.name, 'No Manager') AS manager_name
FROM employee e
LEFT JOIN employee m 
    ON e.manager_id = m.empid;