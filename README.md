ceilograph
==========
Ceilometer  Metrics to Graphite

1. Append this to your _ceilometer.conf_  
```
[graphite]
prefix = ceilometer.
append_hostname = true
```

2. locate your entry_points.txt file for ceilometer and add this under the ceilometer.publishers group ( Centos: _/usr/lib/python2.6/site-packages/ceilometer-2013.2.3-py2.6.egg-info/entry_points.txt_ )
```
[ceilometer.publisher]
graphite = ceilometer.publisher.graphite:GraphitePublisher
```

3. Edit your _pipeline.yaml_ and set the publisher to look like: 
```
    publishers:
            - graphite://192.168.0.1:2003
```

4. Place the graphite.py inside publisher folder (Centos: _/usr/lib/python2.6/site-packages/ceilometer/publisher/_ )


5. Restart openstack-ceilometer-compute

Code Review: https://review.openstack.org/#/c/103479/2
