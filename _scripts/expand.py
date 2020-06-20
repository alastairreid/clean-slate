#! /usr/bin/env python3

import json
import yaml
from yaml import dump
from yaml import CDumper as Dumper

from datetime import date

import re
import string
import sys

def name2url(x):
    x = x.lower()
    x = x.replace(" ", "-")
    return x

# Convert links from list of labels
# to (label: url) pairs
def patch_links(header):
    for c in ["notes", "papers"]:
        xs = header.get(c, [])
        xs = { x: name2url(f"{c}/{x}") for x in xs }
        header[c] = xs

def patch_md(header, body):
    patch_links(header)
    body = [ l for l in body if not re.match("{% include ", l) ]
    return (header, body)

def read_md(f):
    with open(f) as file:
        ls = file.readlines()
        t = ls[1:].index("---\n")
        header = ls[1:t+1]
        body = ls[t+2:]
        header = yaml.safe_load("".join(header))
        return (header, body)

def add_links(links):
    for (x, url) in links.items():
        print(f'[{x}]: {url}')

# for every link to a page, add a back reference
def add_backrefs(ps):
    ns = {}
    for p, (h, _) in ps.items():
        h["refs"] = []
        for x, url in h["notes"].items():
            ns.setdefault(url, {})[x] = name2url(p)
        # todo: papers
    for url, xs in ns.items():
        if url in ps:
            ps[url][0]["refs"] = xs
        else:
            print(f"Reference to missing page {url}")

def pp_refs(label, xs):
    if xs:
        print(f"{label}: ")
        print(",\n".join([f"[{x}]({y})" for x, y in xs.items()]))
        print()

def print_file(i, header, body):
    print(i)
    print("---")
    print(yaml.dump(header))
    print("---")
    print("".join(body))
    pp_refs("Notes", header["notes"])
    pp_refs("Papers", header["papers"])
    pp_refs("Referenced by", header["refs"])
    add_links(header["notes"])
    add_links(header["papers"])

def do_files(fs):
    ps = { f[1:-3]: read_md(f) for f in fs }
    ps = { p: patch_md(h, b) for p, (h, b) in ps.items() }
    add_backrefs(ps)
    for p, (h, b) in ps.items():
        print_file(p, h, b)
        print("===================")

def main():
    do_files(sys.argv[1:])

main()
