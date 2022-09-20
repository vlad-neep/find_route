from django.db import models

from django.core.exceptions import ValidationError

from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name of  route')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Time in travel')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='From city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='To city')
    trains = models.ManyToManyField('trains.Train', verbose_name='Trains list')

    def __str__(self):
        return f'Path: {self.name} from city {self.from_city}'

    class Meta:
        verbose_name = 'Path'
        verbose_name_plural = 'Paths'
        ordering = ['travel_times']

