#!/usr/bin/env python

from django.contrib.gis.db import models

class ActiveCall(models.Model):
    """
    An entry from Tyler's Active Call List:
    http://tylerpolice.com/acl/acl.aspx
    """
    case_number = models.TextField(unique=True)
    priority_code = models.TextField()
    incident = models.TextField()
    status_code = models.TextField()
    reported = models.DateTimeField()
    on_scene = models.DateTimeField(null=True, blank=True)
    street_number = models.TextField()
    street_prefix = models.TextField()
    street_name = models.TextField()
    street_suffix = models.TextField()
    cross_street_name = models.TextField()
    cross_street_suffix = models.TextField()

    raw_html = models.TextField()

    # These fields are based on the server timestamp, not now()
    first_seen = models.DateTimeField()
    last_modified = models.DateTimeField()
    last_seen = models.DateTimeField()

    class Meta:
        ordering = ('reported',)

    def __unicode__(self):
        """
        Print plural names.
        """
        return u'Case #%s - %s' % (self.case_number, self.incident)

