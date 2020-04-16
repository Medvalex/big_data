#* bash code for MR

hadoop jar ~/hadoop-streaming.jar -D mapred.reduce.tasks=0 -input /user/alexander.medvedev/lab03s_in/ -output /user/alexander.medvedev/lab03s/result/ -mapper ./mapper.py -file "mapper.py"

hadoop fs -mkdir /user/alexander.medvedev/lab03s_in

hadoop fs -cp /labs/lab03data/* /user/alexander.medvedev/lab03s_in