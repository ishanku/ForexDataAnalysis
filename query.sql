SELECT * FROM ForexHistoric;

SELECT * FROM ForexCurrent;

SELECT * FROM ForexHistoric
UNION ALL
SELECT * FROM ForexCurrent;