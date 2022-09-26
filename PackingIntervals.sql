/*
This assumes you are using a table containing a unique patient identifier, a start datetime, and an end datetime.
I recommend trying this out first with a single patient to see if it has the desired results
To change the "grace period" between windows change the number within the DATEADD function
To remove the grace period and only combine in cases of overlap, remove the DATEADD function and just use FillDateTime or whatever
it is you are calling your Start DateTime
*/

WITH C1 as (
    SELECT
        PatientICN,
        FillDateTime,
        EndDate,
        CASE WHEN
            DATEADD(Day, -7, FillDateTime) <= MAX(EndDate) OVER(PARTITION BY PatientICN
                                                                ORDER BY FillDateTime, EndDate
                                                                ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
                                                               )
            THEN 0 ELSE 1
        END as isstart
    FROM Dflt.PM_Opioid_Window
),
C2 as (
    SELECT
        *,
        SUM(isstart) OVER(PARTITION BY PatientICN
                          ORDER BY FillDateTime, EndDate
                          ROWS UNBOUNDED PRECEDING) as grp
    FROM C1
)

SELECT
    PatientICN,
    MIN(FillDateTime) as StartDate,
    MAX(EndDate) as EndDate
FROM C2
GROUP BY PatientICN, grp