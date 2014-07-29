ceilograph
==========

Ceilometer  Metrics to Graphite

1. Append this to your ceilometer.conf  
/etc/ceilometer/ceilometer.conf

[graphite]
prefix = ceilometer.
append_hostname = true

2. locate your entry_points.txt file for ceilometer and add this under the ceilometer.publishers group
Centos: /usr/lib/python2.6/site-packages/ceilometer-2013.2.3-py2.6.egg-info/entry_points.txt

[ceilometer.publisher]
graphite = ceilometer.publisher.graphite:GraphitePublisher


3. Edit your pipeline.yaml and set the publisher to look like: 

    publishers:
            - graphite://192.168.0.1:2003


4. Place the graphite.py inside publisher foler 
Centos: /usr/lib/python2.6/site-packages/ceilometer/publisher/


5. Restart openstack-ceilometer-compute
