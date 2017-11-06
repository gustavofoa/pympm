from apps.mpm.models import Banner, Musica, Categoria, DiaLiturgico
import random


def banner_refresh():
    print('refreshing banners...')

    banners = Banner.objects.all()

    for categoria in Categoria.objects.all():
        categoria.banner_lateral = random.choice(banners)
        categoria.banner_footer = random.choice(banners)
        print('update banners for categoria: ', categoria.slug)
        categoria.save()

    for musica in Musica.objects.all():
        musica.banner_lateral = random.choice(banners)
        musica.banner_footer = random.choice(banners)
        print('update banners for musica: ', musica.slug)
        musica.save()

    for diaLiturgico in DiaLiturgico.objects.all():
        diaLiturgico.banner_lateral = random.choice(banners)
        diaLiturgico.banner_footer = random.choice(banners)
        print('update banners for diaLiturgico: ', diaLiturgico.slug)
        diaLiturgico.save()
