-- SQL commands to create full-text search indices on musicbrainz database
create index artist_credit_search_idx on artist_credit using gin (to_tsvector('english', name));

create index recording_search_idx on recording using gin (to_tsvector('english', name));

create index tag_search_idx on tag using gin (to_tsvector('english', name));

-- SQL commands to help analyze ratings data
alter table artist_credit add rank integer not null default 0;

alter table recording add rank integer not null default 0;

alter table tag add rank integer not null default 0;

alter table recording_meta
  alter column rating type smallint using coalesce(rating, 0),
  alter column rating set default 0,
  alter column rating set not null;

alter table recording_meta
  alter column rating_count type integer using coalesce(rating_count, 0),
  alter column rating_count set default 0,
  alter column rating_count set not null;

create index recording_meta_rating_idx on recording_meta (rating desc nulls last);

create index recording_meta_rating_count_idx on recording_meta (rating_count desc nulls last);

-- SQL commands to generate rank values for tag
update tag t
set rank = r.count
from (
  select recording_tag.tag as id, count(*) as count
  from recording_tag
  group by recording_tag.tag
) r
where t.id = r.id;

-- SQL commands to generate rank values for recording
-- Commented out as using batched updates in update_recording_ranks.sql
-- update recording r
-- set rank = rm.rank
-- from (
--   select id, rating + rating_count as rank
--   from recording_meta
-- ) rm
-- where r.id = rm.id;

-- SQL commands to generate rank values for artist_credit
-- Commented out as using batched updates in update_artist_credit_ranks.sql
-- update artist_credit ac
-- set rank = r.rank
-- from (
--   select recording.artist_credit as id, sum(rank) as rank
--   from recording
--   group by recording.artist_credit
-- ) r
-- where ac.id = r.id;

-- SQL commands to create indexed rank columns on musicbrainz database
create index artist_credit_rank_idx on artist_credit (rank desc);

create index recording_rank_idx on recording (rank desc);

create index tag_rank_idx on tag (rank desc);