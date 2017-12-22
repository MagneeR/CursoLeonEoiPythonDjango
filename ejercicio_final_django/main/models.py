from django.db import models

TOURNAMENT_CATEGORIES = (
    (0, 'Fuerza'),
    (1, 'Destreza'),
    (2, 'Resistencia'),
)


# Create your models here.
class Fighter(models.Model):
    alias = models.CharField(max_length = 15, primary_key = True)
    avatar = models.ImageField(upload_to = 'avatars')
    force = models.PositiveIntegerField('Fuerza', default=4)
    skill = models.PositiveIntegerField('Habilidad', default=3)
    resistance = models.PositiveIntegerField('Resistencia', default=3)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'

class Tournament(models.Model):
    name = models.CharField('Nombre', max_length = 150)
    start_date = models.DateTimeField('Hora de inicio de inscripcion') #Si pongo null true ese campo no seria obligatorio
    finish_date = models.DateTimeField('Hora de fin de inscripcion')
    fighter_count = models.IntegerField('Nº de luchadores')
    category = models.IntegerField('Categoría', choices = TOURNAMENT_CATEGORIES, default = 1)
    fighters = models.ManyToManyField(Fighter, verbose_name = 'Luchadores')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'


class Combat(models.Model):
    date = models.DateTimeField('Fecha/hora', auto_now = True)
    fighter1 = models.ForeignKey(Fighter, verbose_name = 'Luchador 1', related_name='fighter1', on_delete = models.CASCADE)
    fighter2 = models.ForeignKey(Fighter, verbose_name='Luchador 2',related_name='fighter2', on_delete = models.CASCADE)
    tournament = models.ForeignKey(Tournament, verbose_name = 'Torneo', related_name='combats', on_delete = models.CASCADE)

    def __str__(self):
        return '{} vs {}'.format(self.fighter1.alias, self.fighter2.alias)

    class Meta:
        verbose_name = 'Combate'
        verbose_name_plural = 'Combates'