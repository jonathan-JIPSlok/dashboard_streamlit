CREATE TABLE IF NOT EXISTS data_pipeline (
    data_ingestao DateTime,
    data_line DateTime,
    tag String
)
ENGINE = MergeTree()
ORDER BY data_ingestao;

-- View daily summary
CREATE VIEW IF NOT EXISTS daily_summary AS
SELECT toDate(data_line) AS date,
       count(*) AS count
FROM data_pipeline
GROUP BY date;

-- View tag_summary
CREATE VIEW IF NOT EXISTS tag_summary AS
SELECT tag,
        count(*) AS count
FROM data_pipeline
GROUP BY tag;