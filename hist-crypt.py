import click
import sys

import ciphers.caesar
import ciphers.affine
import ciphers.substitution
import ciphers.vignere


COPRIME_TO_26 = ['1', '3', '5', '7', '9', '11',
                 '15', '17', '19', '21', '23', '25']


@click.group()
def cli():
    pass


@click.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.IntRange(-26, 26))
def caesar(file, key):    
    click.echo(ciphers.caesar.shift(file.read(), key).strip())


@click.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-a", type=click.Choice(COPRIME_TO_26), required=True)
@click.option("-b", type=click.INT, required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def affine(file, a, b, decrypt):
    if decrypt:
        print(ciphers.affine.decrypt(file.read(), int(a), int(b)).strip())
    else:
        print(ciphers.affine.encrypt(file.read(), int(a), int(b)).strip())


@click.command()
@click.option("-f", "--file",
              help="name of file containing text or stdin if blank",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-k", "--key", type=click.STRING, required=True)
@click.option("-d", "--decrypt", default=False, is_flag=True)
def vignere(file, key, decrypt):
    if decrypt:
        print(ciphers.vignere.decrypt(file.read(), key).strip())
    else:
        print(ciphers.vignere.encrypt(file.read(), key).strip())



@click.command()
@click.option("-f", "--file",
              help="name of file containing text",
              type=click.File('r'),
              default=sys.stdin)
@click.option("-m", "--mapfile", type=click.File('r'), required=True)
def substitution(file, mapfile):
    mapping = ciphers.substitution.import_dict(mapfile)
    print(ciphers.substitution.substitute(file.read(), mapping).strip())


cli.add_command(caesar)
cli.add_command(affine)
cli.add_command(vignere)
cli.add_command(substitution)


if __name__ == "__main__":
    cli()