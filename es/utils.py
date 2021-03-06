import random
import string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.question)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_solution(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.nom)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_slug_generator_produit(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_partenaire(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.company) 
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_slug_generator_dashboard_Opportunite(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_dashboard_Annonce(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_dashboard_Fidelite(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_dashboard_Marketing(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_dashboard_Commerciale(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
