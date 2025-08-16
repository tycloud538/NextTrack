-- 0k to 100k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 0
    AND recording.artist_credit <= 100000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 100k to 200k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 100000
    AND recording.artist_credit <= 200000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 200k to 300k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 200000
    AND recording.artist_credit <= 300000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 300k to 400k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 300000
    AND recording.artist_credit <= 400000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 400k to 500k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 400000
    AND recording.artist_credit <= 500000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 500k to 600k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 500000
    AND recording.artist_credit <= 600000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 600k to 700k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 600000
    AND recording.artist_credit <= 700000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 700k to 800k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 700000
    AND recording.artist_credit <= 800000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 800k to 900k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 800000
    AND recording.artist_credit <= 900000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 900k to 1000k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 900000
    AND recording.artist_credit <= 1000000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1000k to 1100k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1000000
    AND recording.artist_credit <= 1100000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1100k to 1200k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1100000
    AND recording.artist_credit <= 1200000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1200k to 1300k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1200000
    AND recording.artist_credit <= 1300000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1300k to 1400k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1300000
    AND recording.artist_credit <= 1400000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1400k to 1500k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1400000
    AND recording.artist_credit <= 1500000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1500k to 1600k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1500000
    AND recording.artist_credit <= 1600000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1600k to 1700k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1600000
    AND recording.artist_credit <= 1700000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1700k to 1800k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1700000
    AND recording.artist_credit <= 1800000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1800k to 1900k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1800000
    AND recording.artist_credit <= 1900000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 1900k to 2000k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 1900000
    AND recording.artist_credit <= 2000000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2000k to 2100k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2000000
    AND recording.artist_credit <= 2100000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2100k to 2200k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2100000
    AND recording.artist_credit <= 2200000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2200k to 2300k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2200000
    AND recording.artist_credit <= 2300000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2300k to 2400k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2300000
    AND recording.artist_credit <= 2400000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2400k to 2500k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2400000
    AND recording.artist_credit <= 2500000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2500k to 2600k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2500000
    AND recording.artist_credit <= 2600000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2600k to 2700k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2600000
    AND recording.artist_credit <= 2700000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2700k to 2800k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2700000
    AND recording.artist_credit <= 2800000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2800k to 2900k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2800000
    AND recording.artist_credit <= 2900000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 2900k to 3000k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 2900000
    AND recording.artist_credit <= 3000000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3000k to 3100k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3000000
    AND recording.artist_credit <= 3100000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3100k to 3200k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3100000
    AND recording.artist_credit <= 3200000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3200k to 3300k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3200000
    AND recording.artist_credit <= 3300000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3300k to 3400k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3300000
    AND recording.artist_credit <= 3400000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3400k to 3500k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3400000
    AND recording.artist_credit <= 3500000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3500k to 3600k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3500000
    AND recording.artist_credit <= 3600000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3600k to 3700k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3600000
    AND recording.artist_credit <= 3700000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3700k to 3800k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3700000
    AND recording.artist_credit <= 3800000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3800k to 3900k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3800000
    AND recording.artist_credit <= 3900000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 3900k to 4000k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 3900000
    AND recording.artist_credit <= 4000000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 4000k to 4100k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 4000000
    AND recording.artist_credit <= 4100000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 4100k to 4200k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 4100000
    AND recording.artist_credit <= 4200000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 4200k to 4300k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 4200000
    AND recording.artist_credit <= 4300000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 4300k to 4400k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 4300000
    AND recording.artist_credit <= 4400000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;

-- 4400k to 4500k
UPDATE artist_credit ac
SET rank = r.rank
FROM (
  SELECT recording.artist_credit AS id, SUM(rank) AS rank
  FROM recording
  WHERE recording.artist_credit > 4400000
    AND recording.artist_credit <= 4500000
  GROUP BY recording.artist_credit
) r
WHERE ac.id = r.id;