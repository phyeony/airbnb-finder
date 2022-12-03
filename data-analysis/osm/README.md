## file description
`amenities-vancouver.json.gz` is a given json.gz by Prof Greg. \
`clean-up-osm-amenities.py` is to clean up that file.

## Steps for getting the osm data for vancouver
1. Downloaded data from https://towardsdatascience.com/beginner-guide-to-download-the-openstreetmap-gis-data-24bbbba22a38 \
Saved in raw_data planet_-123.299,49.145_-122.867,49.357.osm.gz.
Exported with -123.299 < long < -122.867 and 49.145 < lat < 49.357.

2. Disassembled the data with the provided python program `disassemble-osm.py` and following command which was executed in `output/disassemble` dir;     
   
    `pv ../../raw-data/planet_-123.278,49.178_-122.988,49.315.osm.gz | gzip -d | python3 ../../disassemble-osm.py | split -C1000M -d -a 4 --additional-suffix='.xml' --filter='gzip > $FILE.gz' - osm-planet-`

3. Run `osm-get-certain-tag` to get osm data with certain tags.

    Example:
    To get tag with "tourism" run `spark-submit osm-get-certain.tag.py output/disassemble/ output/tourism tourism`


## Some tips I found along the way:
**How to copy hdfs file over to your local machine:** (Not related to the steps above.)

    Inside cluster : `hadoop fs -copyToLocal output` \
    Then inside your local machine: `scp -r cluster.cs.sfu.ca:~/output . `
