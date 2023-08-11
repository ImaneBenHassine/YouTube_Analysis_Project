 # to copy all the JSON file to same location
 AWS s3 cp . s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs_refrence_data/ --recursive --exclude "*" --include "*".json"
	 

# this command will create two different folders inside our bucket & will start uploading all the json file from your computer to the S3 bucket inside the youtube folder inside the raw statistics 
#to copy all data files to its own location, folowwing Hiva-style patterns 

    AWS s3 cp CAvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=ca/
	AWS s3 cp DEvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=de/
	AWS s3 cp FRvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=fr/
	AWS s3 cp GBvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=gb/
	AWS s3 cp INvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=in/
	AWS s3 cp JPvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=jp/
	AWS s3 cp KRvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=kr/
	AWS s3 cp MXvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=mx/
	AWS s3 cp RUvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=ru/
	AWS s3 cp USvideos.csv s3://de-on-youtube-raw-eu-west-3-dev/youtube/raw_statistcs/region=us/
	