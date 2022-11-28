# Extract Spark-style JSON from planet.osm data.
# Typical invocation:
# spark-submit osm-get-certain-tag.py /courses/datasets/openstreetmaps get-certain-tag

import sys

assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types, Row

spark = SparkSession.builder.appName("OSM point of interest extracter").getOrCreate()
assert spark.version >= "2.4"  # make sure we have Spark 2.4+
spark.sparkContext.setLogLevel("WARN")
sc = spark.sparkContext
spark.conf.set("spark.sql.session.timeZone", "UTC")

from lxml import etree
import dateutil.parser

# import datetime


def get_certain_tag(line, tag_type):
    root = etree.fromstring(line)
    if root.tag != "node":
        return

    tags = {tag.get("k"): tag.get("v") for tag in root.iter("tag")}
    if tag_type not in tags:
        return
    if "name" not in tags:
        return
    if "amenity" in tags:
        return
    if tag_type == "tourism":
        tourism_type = tags["tourism"]
        if (
            tourism_type == "information"
            or tourism_type == "apartment"
            or tourism_type == "guest house"
            or tourism_type == "hostel"
            or tourism_type == "hotel"
            or tourism_type == "motel"
            or tourism_type == "resort"
            or tourism_type == "yes"
        ):
            return

    lat = float(root.get("lat"))
    lon = float(root.get("lon"))
    
    # You can control on lat and long more with code
    # if lat < 49.16 or lat > 49.341:
    #     return
    # if lon < -123.28 or lon > -122.9:
    #     return

    # https://stackoverflow.com/q/969285/6871666
    # unix_time = dateutil.parser.parse(root.get("timestamp")).timestamp()
    # unix_time = datetime.datetime.strptime(root.get('timestamp'), "%Y-%m-%dT%H:%M:%S%z").timestamp()
    type = tags[tag_type]
    del tags[tag_type]
    if "name" in tags:
        name = tags["name"]
        del tags["name"]
    # else:
    #     name = None
    yield Row(lat=lat, lon=lon, type=type, name=name, tags=tags)


def main(inputs, output, tag_type):
    lines = sc.textFile(inputs)
    nodes = lines.flatMap(lambda line: get_certain_tag(line, tag_type))

    node_schema = types.StructType(
        [
            types.StructField("lat", types.DoubleType(), nullable=False),
            types.StructField("lon", types.DoubleType(), nullable=False),
            # types.StructField("unix_time", types.DoubleType(), nullable=False),
            # types.StructField('timestamp', types.TimestampType(), nullable=False),
            types.StructField("type", types.StringType(), nullable=False),
            types.StructField("name", types.StringType(), nullable=True),
            types.StructField(
                "tags",
                types.MapType(types.StringType(), types.StringType()),
                nullable=False,
            ),
        ]
    )

    node = spark.createDataFrame(nodes, schema=node_schema)
    # work around Python to Spark datetime conversion problems
    node = node.select(
        "lat",
        "lon",
        # functions.from_unixtime(node["unix_time"]).alias("timestamp"),
        "type",
        "name",
        "tags",
    )
    # node = node.cache()
    node.write.json(output, mode="overwrite", compression="gzip")


# node.write.parquet(output + "-parquet", mode="overwrite", compression="lz4")


if __name__ == "__main__":
    inputs = sys.argv[1]
    output = sys.argv[2]
    tag_type = sys.argv[3]
    main(inputs, output, tag_type)
