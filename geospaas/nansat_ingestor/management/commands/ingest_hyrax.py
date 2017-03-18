import os
import time
import re
import urllib2

from django.core.management.base import BaseCommand, CommandError

from geospaas.nansat_ingestor.management.commands.ingest import Command as IngestCommand

# extend Ingest
class Command(IngestCommand):
    args = 'HYRAX_URL'
    help = 'Add file to catalog from HYRAX server'

    def handle(self, *args, **options):
        print 'Searching netcdf files. May takes some time...\n\n\n'
        nc_uris = find_netcdf_uris(args[0])
        num_nc_uris = len(nc_uris)
        print '\nTrying to ingest %d datasets\n'%num_nc_uris
        count = 0
        faile = []
        nc_uris_failed = list(nc_uris)
        nc_uris_succeeded = list(nc_uris)
        ind_failed = []
        ind_succeeded = []
        ind_pop = []
        try:
            cc = super(Command, self).handle(*nc_uris, **options)
        except:
            cc = 0
        for i in range(cc+1): # elements added or failing
            ind_pop.append(i)
            if i==cc:
                ind_failed.append(i)
            else:
                ind_succeeded.append(i)
        for i in ind_pop:
            nc_uris.pop(i) # avoid repetition
        for i in ind_failed:
            nc_uris_succeeded.pop(i) # log successes
        for i in ind_succeeded:
            nc_uris_failed.pop(i) # log fails

        print 'Failed:'
        for uri in nc_uris_failed:
            print uri
        print 'Successfully added %d of %d new \
                datasets'%(len(nc_uris_succeeded), num_nc_uris)
            

def find_netcdf_uris(uri0, sleep=1.0):
    uri0_base = os.path.split(uri0)[0]
    print 'Search in ', uri0_base
    # get HTML from the URL
    time.sleep(sleep)
    response = urllib2.urlopen(uri0)
    html = response.read()
    
    # find all links to netDCF
    nc_uris = [os.path.join(uri0_base, uri.replace('href="', '').replace('.nc.dds', '.nc'))
            for uri in re.findall('href=.*nc\.dds', html)]
    
    # find all links to sub-pages
    uris = [os.path.join(uri0_base, uri.replace('href="', ''))
            for uri in re.findall('href=.*/contents.html', html)]
    # get links to netcDF also from sub-pages
    try:
        for uri in uris:
            nc_uris += find_netcdf_uris(uri)
    except urllib2.HTTPError as e:
        print 'Server HTTP error %s'%e.message
    # return all links to netCDF
    return nc_uris

    