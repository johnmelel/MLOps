from feast import Entity, Feature, FeatureView, ValueType, FileSource
from feast.data_format import ParquetFormat

athlete = Entity(name="athlete_id", value_type=ValueType.INT64, description="Athlete ID")

df_v1_source = FileSource(
    path="data/df_v1.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
    file_format=ParquetFormat(),
)

df_v2_source = FileSource(
    path="data/df_v2.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
    file_format=ParquetFormat(),
)

athlete_features_v1 = FeatureView(
    name="athlete_features_v1",
    entities=["athlete_id"],
    ttl=None,
    features=[
        Feature(name="gender", dtype=ValueType.STRING),
        Feature(name="age", dtype=ValueType.INT64),
        Feature(name="height", dtype=ValueType.INT64),
        Feature(name="weight", dtype=ValueType.INT64),
        Feature(name="total_olympic_lift", dtype=ValueType.INT64),
        Feature(name="total_powerlifting_lift", dtype=ValueType.INT64),
        Feature(name="overall_total_lift", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=df_v1_source,
)

athlete_features_v2 = FeatureView(
    name="athlete_features_v2",
    entities=["athlete_id"],
    ttl=None,
    features=[
        Feature(name="gender", dtype=ValueType.STRING),
        Feature(name="age", dtype=ValueType.INT64),
        Feature(name="height", dtype=ValueType.INT64),
        Feature(name="weight", dtype=ValueType.INT64),
        Feature(name="BMI", dtype=ValueType.FLOAT),
        Feature(name="candj_to_weight_ratio", dtype=ValueType.FLOAT),
        Feature(name="snatch_to_weight_ratio", dtype=ValueType.FLOAT),
        Feature(name="deadlift_to_weight_ratio", dtype=ValueType.FLOAT),
        Feature(name="backsq_to_weight_ratio", dtype=ValueType.FLOAT),
    ],
    online=True,
    batch_source=df_v2_source,
)
