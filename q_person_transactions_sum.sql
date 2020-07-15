/*
	*** Author: Tatsiana Kalinina
    *** Date: 15.07.2020
    *** Task: Provide Transactions for the Users 345 and 1234, aggregated monthly, sorted by month,
			  for the period from 15.02.2020 till 06.06.2020
*/
USE enote;

SELECT
	p.id_person,
    concat(YEAR(t.transaction_date),'.', lpad(MONTH(t.transaction_date),2,0)) as month,
    round(sum(t.transaction_amount),2) as sum_of_transactions
FROM
	enote.person p
		left join enote.account a on a.id_person = p.id_person
		left join enote.transaction t on t.id_account = a.id_account
WHERE
	1=1
	AND p.id_person IN (1234, 345)
    AND DATE(t.transaction_date) BETWEEN '2020-02-15' AND '2020-06-06'
GROUP BY 
	p.id_person,
    month
ORDER BY
	p.id_person DESC,
    month;
	
	