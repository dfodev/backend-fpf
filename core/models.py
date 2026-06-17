from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', null=False)
    modified_at = models.DateTimeField(auto_now=True, db_column='modified_at', null=False)
    active = models.BooleanField(default=True, db_column='active', null=False)

    class Meta:
        abstract = True
        managed = True


class State(ModelBase):
    name = models.CharField(db_column='name', null=False, blank=False, max_length=64)
    abbreviation = models.CharField(db_column='abbreviation', null=False, max_length=2)

    class Meta:
        db_table = 'state'


class City(ModelBase):
    name = models.CharField(db_column='name', null=False, blank=False, max_length=64)
    state = models.ForeignKey(db_column='id_state', to='State', on_delete=models.DO_NOTHING, null=False,
                              related_name='cities')

    class Meta:
        db_table = 'city'


class Zone(ModelBase):
    name = models.CharField(db_column='name', null=False, blank=False, max_length=64)

    class Meta:
        db_table = 'zone'


class District(ModelBase):
    name = models.CharField(db_column='name', null=False, blank=False, max_length=64)
    zone = models.ForeignKey(db_column='id_zone', to='Zone', on_delete=models.DO_NOTHING, null=False,
                             related_name='districts')
    city = models.ForeignKey(db_column='id_city', to='City', on_delete=models.DO_NOTHING, null=False,
                             related_name='districts')

    class Meta:
        db_table = 'district'
