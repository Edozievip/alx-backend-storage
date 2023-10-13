-- A script that creates an index idx_name_first on the table names and the first letter of name and the score
-- Requirements:
-- Import this table dump: names.sql.zip
-- Only the first letter of name and score must be indexed

CREATE INDEX idx_name_first ON names(name(1), score);
