-- 0M to 1M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 0 AND id <= 1000000
) rm
WHERE r.id = rm.id;

-- 1M to 2M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 1000000 AND id <= 2000000
) rm
WHERE r.id = rm.id;

-- 2M to 3M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 2000000 AND id <= 3000000
) rm
WHERE r.id = rm.id;

-- 3M to 4M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 3000000 AND id <= 4000000
) rm
WHERE r.id = rm.id;

-- 4M to 5M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 4000000 AND id <= 5000000
) rm
WHERE r.id = rm.id;

-- 5M to 6M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 5000000 AND id <= 6000000
) rm
WHERE r.id = rm.id;

-- 6M to 7M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 6000000 AND id <= 7000000
) rm
WHERE r.id = rm.id;

-- 7M to 8M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 7000000 AND id <= 8000000
) rm
WHERE r.id = rm.id;

-- 8M to 9M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 8000000 AND id <= 9000000
) rm
WHERE r.id = rm.id;

-- 9M to 10M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 9000000 AND id <= 10000000
) rm
WHERE r.id = rm.id;

-- 10M to 11M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 10000000 AND id <= 11000000
) rm
WHERE r.id = rm.id;

-- 11M to 12M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 11000000 AND id <= 12000000
) rm
WHERE r.id = rm.id;

-- 12M to 13M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 12000000 AND id <= 13000000
) rm
WHERE r.id = rm.id;

-- 13M to 14M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 13000000 AND id <= 14000000
) rm
WHERE r.id = rm.id;

-- 14M to 15M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 14000000 AND id <= 15000000
) rm
WHERE r.id = rm.id;

-- 15M to 16M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 15000000 AND id <= 16000000
) rm
WHERE r.id = rm.id;

-- 16M to 17M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 16000000 AND id <= 17000000
) rm
WHERE r.id = rm.id;

-- 17M to 18M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 17000000 AND id <= 18000000
) rm
WHERE r.id = rm.id;

-- 18M to 19M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 18000000 AND id <= 19000000
) rm
WHERE r.id = rm.id;

-- 19M to 20M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 19000000 AND id <= 20000000
) rm
WHERE r.id = rm.id;

-- 20M to 21M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 20000000 AND id <= 21000000
) rm
WHERE r.id = rm.id;

-- 21M to 22M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 21000000 AND id <= 22000000
) rm
WHERE r.id = rm.id;

-- 22M to 23M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 22000000 AND id <= 23000000
) rm
WHERE r.id = rm.id;

-- 23M to 24M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 23000000 AND id <= 24000000
) rm
WHERE r.id = rm.id;

-- 24M to 25M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 24000000 AND id <= 25000000
) rm
WHERE r.id = rm.id;

-- 25M to 26M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 25000000 AND id <= 26000000
) rm
WHERE r.id = rm.id;

-- 26M to 27M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 26000000 AND id <= 27000000
) rm
WHERE r.id = rm.id;

-- 27M to 28M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 27000000 AND id <= 28000000
) rm
WHERE r.id = rm.id;

-- 28M to 29M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 28000000 AND id <= 29000000
) rm
WHERE r.id = rm.id;

-- 29M to 30M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 29000000 AND id <= 30000000
) rm
WHERE r.id = rm.id;

-- 30M to 31M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 30000000 AND id <= 31000000
) rm
WHERE r.id = rm.id;

-- 31M to 32M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 31000000 AND id <= 32000000
) rm
WHERE r.id = rm.id;

-- 32M to 33M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 32000000 AND id <= 33000000
) rm
WHERE r.id = rm.id;

-- 33M to 34M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 33000000 AND id <= 34000000
) rm
WHERE r.id = rm.id;

-- 34M to 35M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 34000000 AND id <= 35000000
) rm
WHERE r.id = rm.id;

-- 35M to 36M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 35000000 AND id <= 36000000
) rm
WHERE r.id = rm.id;

-- 36M to 37M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 36000000 AND id <= 37000000
) rm
WHERE r.id = rm.id;

-- 37M to 38M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 37000000 AND id <= 38000000
) rm
WHERE r.id = rm.id;

-- 38M to 39M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 38000000 AND id <= 39000000
) rm
WHERE r.id = rm.id;

-- 39M to 40M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 39000000 AND id <= 40000000
) rm
WHERE r.id = rm.id;

-- 40M to 41M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 40000000 AND id <= 41000000
) rm
WHERE r.id = rm.id;

-- 41M to 42M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 41000000 AND id <= 42000000
) rm
WHERE r.id = rm.id;

-- 42M to 43M
UPDATE recording r
SET rank = rm.rank
FROM (
  SELECT id, rating + rating_count AS rank
  FROM recording_meta
  WHERE id > 42000000 AND id <= 43000000
) rm
WHERE r.id = rm.id;

