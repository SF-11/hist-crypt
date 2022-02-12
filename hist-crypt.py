import click
import sys

import ciphers.caesar
import ciphers.affine
import ciphers.substitution
import ciphers.vignere
import ciphers.adfgvx
import ciphers.playfair
import ciphers.bacon


COPRIME_TO_26 = ['1', '3', '5', '7', '9', '11',
                 '15', '17', '19', '21', '23', '25']


@click.group()
def cli():
    pass


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.IntRange(-26, 26), required=True)
def caesar(file, key):    
    click.echo(ciphers.caesar.shift(file.read(), key).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-a", type=click.Choice(COPRIME_TO_26), required=True)
@click.option("-b", type=click.INT, required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def affine(file, a, b, decrypt):
    if decrypt:
        click.echo(ciphers.affine.decrypt(file.read(), int(a), int(b)).strip())
    else:
        click.echo(ciphers.affine.encrypt(file.read(), int(a), int(b)).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.STRING, required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def vignere(file, key, decrypt):
    if decrypt:
        click.echo(ciphers.vignere.decrypt(file.read(), key).strip())
    else:
        click.echo(ciphers.vignere.encrypt(file.read(), key).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-m", "--mapfile", type=click.File('r'), required=True)
def substitution(file, mapfile):
    mapping = ciphers.substitution.import_dict(mapfile)
    click.echo(ciphers.substitution.substitute(file.read(), mapping).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.STRING, required=True)
@click.option("-a", "--alphafile",
              help="File containing 5x5 or 6x6 ADFGV(X) subsititution square, comma delimeters",
              type=click.File('r'), required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def adfgvx(file, key, alphafile, decrypt):
    alpha_square = ciphers.adfgvx.load_alpha_square(alphafile)
    if decrypt:
        click.echo(ciphers.adfgvx.decrypt(file.read(), key, alpha_square).strip())
    else:
        click.echo(ciphers.adfgvx.encrypt(file.read(), key, alpha_square).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.STRING, required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def playfair(file, key, decrypt):
    if decrypt:
        click.echo(ciphers.playfair.decrypt(file.read(), key).strip())
    else:
        click.echo(ciphers.playfair.encrypt(file.read(), key).strip())


@cli.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("--hide", 
              type=click.STRING, 
              help="Message to hide in the text", 
              required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def bacon(file, hide, decrypt):
    if decrypt:
        click.echo(ciphers.bacon.decrypt(file.read()).strip())
    else:
        click.echo(ciphers.bacon.encrypt(hide, file.read()).strip())


if __name__ == "__main__":
    cli()