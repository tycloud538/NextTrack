-- SQL commands to create full-text search indices on musicbrainz database
CREATE INDEX artist_credit_search_idx ON artist_credit USING GIN (to_tsvector('english', name));

CREATE INDEX genre_search_idx ON genre USING GIN (to_tsvector('english', name));

CREATE INDEX tag_search_idx ON tag USING GIN (to_tsvector('english', name));

CREATE INDEX track_search_idx ON track USING GIN (to_tsvector('english', name));
