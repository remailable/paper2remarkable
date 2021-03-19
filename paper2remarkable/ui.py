# -*- coding: utf-8 -*-

"""Command line interface

Author: G.J.J. van den Burg
License: See LICENSE file
Copyright: 2019, G.J.J. van den Burg

"""

import copy
import os
import sys


from .exceptions import UnidentifiedSourceError, InvalidURLError
from .providers import providers, LocalFile
from .utils import follow_redirects, is_url


def exception(msg):
    print("ERROR: " + msg, file=sys.stderr)
    print("Error occurred. Exiting.", file=sys.stderr)
    print("", file=sys.stderr)
    print("", file=sys.stderr)
    raise SystemExit(1)


def choose_provider(url: str):
    provider = cookiejar = None
    if is_url(url):
        new_input, cookiejar = follow_redirects(url)
        provider = next((p for p in providers if p.validate(new_input)), None)
    else:
        # not a proper URL or non-existent file
        raise UnidentifiedSourceError

    if provider is None:
        raise InvalidURLError

    return provider, new_input, cookiejar


def get_pdf_from_url(url: str):
    provider, new_input, cookiejar = choose_provider(url)
    prov = provider()
    prov.run(new_input, filename="test.pdf")


"""
def main():
    args = parse_args()
    set_excepthook(args.debug)

    if args.center and args.right:
        exception("Can't center and right align at the same time!")

    if args.center and args.no_crop:
        exception("Can't center and not crop at the same time!")

    if args.right and args.no_crop:
        exception("Can't right align and not crop at the same time!")

    if args.filename and not len(args.filename) == len(args.input):
        exception(
            "When providing --filename and multiple inputs, their number must match."
        )

    config = load_config(path=args.config)
    options = merge_options(args, config=config)

    filenames = (
        [None] * len(args.input) if not args.filename else args.filename
    )

    for cli_input, filename in zip(args.input, filenames):
        provider, new_input, cookiejar = choose_provider(cli_input)
        prov = provider(
            verbose=options["core"]["verbose"],
            upload=options["core"]["upload"],
            debug=args.debug,
            experimental=options["core"]["experimental"],
            crop=options["core"]["crop"],
            blank=options["core"]["blank"],
            remarkable_dir=args.remarkable_dir,
            rmapi_path=options["system"]["rmapi"],
            pdftoppm_path=options["system"]["pdftoppm"],
            pdftk_path=options["system"]["pdftk"],
            qpdf_path=options["system"]["qpdf"],
            gs_path=options["system"]["gs"],
            css=options["html"]["css"],
            font_urls=options["html"]["font_urls"],
            cookiejar=cookiejar,
        )
        prov.run(new_input, filename=filename)
"""
