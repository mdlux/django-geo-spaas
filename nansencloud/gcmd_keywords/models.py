from django.db import models

from nansencloud.gcmd_keywords.managers import PlatformManager
from nansencloud.gcmd_keywords.managers import InstrumentManager
from nansencloud.gcmd_keywords.managers import DataCenterManager
from nansencloud.gcmd_keywords.managers import ScienceKeywordManager
from nansencloud.gcmd_keywords.managers import ProjectManager
from nansencloud.gcmd_keywords.managers import HorizontalDataResolutionManager
from nansencloud.gcmd_keywords.managers import VerticalDataResolutionManager
from nansencloud.gcmd_keywords.managers import TemporalDataResolutionManager
from nansencloud.gcmd_keywords.managers import ISOTopicCategoryManager
from nansencloud.gcmd_keywords.managers import LocationManager

# GCMD keywords loaded into the models in migrations/0001_initial.py using the
# nersc-metadata package

class Platform(models.Model):

    category = models.CharField(max_length=100)
    series_entity = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=100)

    objects = PlatformManager()

    def __str__(self):
        return self.short_name

    def natural_key(self):
        return (self.short_name)

class Instrument(models.Model):

    category = models.CharField(max_length=100)
    instrument_class = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=100)

    objects = InstrumentManager()

    def __str__(self):
        return self.short_name

    def natural_key(self):
        return (self.short_name)

class ISOTopicCategory(models.Model):
    '''
    The <ISO_Topic_Category> field is used to identify the keywords in the ISO
    19115 - Geographic Information Metadata (http://www.isotc211.org/) Topic
    Category Code List. It is a high-level geographic data thematic
    classification to assist in the grouping and search of available geographic
    data sets.

    Directory Interchange Format (DIF) Writer's Guide, 2015.
    Global Change Master Directory.
    National Aeronautics and Space Administration.
    [http://gcmd.nasa.gov/add/difguide/]. 
    '''
    name = models.CharField(max_length=100)
    # see http://gcmd.gsfc.nasa.gov/add/difguide/iso_topics.html for
    #description = models.TextField() 

    objects = ISOTopicCategoryManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)

class DataCenter(models.Model):
    ''' The data center is needed to control data access and also for indexing
    to allow search.
    '''
    bucket_level0 = models.CharField(max_length=200)
    bucket_level1 = models.CharField(max_length=200)
    bucket_level2 = models.CharField(max_length=200)
    bucket_level3 = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=200)
    data_center_url = models.URLField()

    objects = DataCenterManager()

    def __str__(self):
        return self.short_name

    def natural_key(self):
        return (self.short_name)

class Location(models.Model):
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    subregion1 = models.CharField(max_length=50)
    subregion2 = models.CharField(max_length=50)
    subregion3 = models.CharField(max_length=50)

    objects = LocationManager()

    def __str__(self):
        return '%s %s' %(self.subregion2, self.subregion3)

    def natural_key(self):
        return (category, type, subregion1, subregion2,
            subregion3)

class ScienceKeyword(models.Model):
    category = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    term = models.CharField(max_length=30)
    variable_level_1 = models.CharField(max_length=30)
    variable_level_2 = models.CharField(max_length=30)
    variable_level_3 = models.CharField(max_length=30)
    detailed_variable = models.CharField(max_length=80)

    objects = ScienceKeywordManager()

    def __str__(self):
        return '%s' %self.detailed_variable

    def natural_key(self):
        return (self.category, self.topic, self.term, self.variable_level_1,
                self.variable_level_2, self.variable_level_3)

class Project(models.Model):
    bucket = models.CharField(max_length=6)
    short_name = models.CharField(max_length=80)
    long_name = models.CharField(max_length=220)

    objects = ProjectManager()

    def __str__(self):
        return self.short_name

    def natural_key(self):
        return (self.bucket, self.short_name)

class HorizontalDataResolution(models.Model):
    range = models.CharField(max_length=220)

    objects = HorizontalDataResolutionManager()

    def __str__(self):
        return self.range

    def natural_key(self):
        return (self.range)

class VerticalDataResolution(models.Model):
    range = models.CharField(max_length=220)

    objects = VerticalDataResolutionManager()

    def __str__(self):
        return self.range

    def natural_key(self):
        return (self.range)

class TemporalDataResolution(models.Model):
    range = models.CharField(max_length=220)

    objects = TemporalDataResolutionManager()

    def __str__(self):
        return self.range

    def natural_key(self):
        return (self.range)

