from django.test import TestCase
from apps.mpm.models import Musica

# Create your tests here.
class MusicaTestCase(TestCase):
    def setUp(self):
        Musica.objects.create(
            slug="oracao-pela-familia",
            nome="ORACAO PELA FAMILIA",
            rating=81.4,
            votes=15)
    def test_add_music_rate(self):
        oracao_pela_familia = Musica.objects.get(slug="oracao-pela-familia")

        new_rating = (oracao_pela_familia.rating*oracao_pela_familia.votes+100)/(oracao_pela_familia.votes+1);

        oracao_pela_familia.add_rate(5)

        self.assertEqual(oracao_pela_familia.rating, new_rating)
        print "New rating = ", oracao_pela_familia.rating
        print "New votes = ", oracao_pela_familia.votes
