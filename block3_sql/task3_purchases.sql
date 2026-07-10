SELECT DISTINCT a.client_id
FROM account a
JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
  AND t.type = 'purchase'
GROUP BY a.client_id, a.id
HAVING SUM(t.amount) < 5000;
