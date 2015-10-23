UserClassifier
===========

Classify apache log by `userid`.

The logs are available in several servers that will be processed in a cluster. The system architecture is shown below:

```
cluster
   |-- server01
   |-- server02
   |-- ...
```

--------------

In order to simulate, first generate some random log files. For this, type the following command:

```
python log_generator.py
```

After generating the log files, now it's time to classify them using the following command:

```
python main.py
```

The results are stored in the folder `users_sorted`.

While running, the log files are grouped by userid and stored in the folder `users_grouped`. After grouping, each user file is sorted and stored in the folder `users_sorted`.

--------------

Some parameters may be changed in the file `constants.py`.

The implementation is using `open` (for using local files or mounted folders from a remote server), but it can be replaced by some protocol like http or ftp for downloading files.