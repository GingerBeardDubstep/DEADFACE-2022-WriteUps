# Forensic challenges

## First Strike

Here we are given a file containing access logs and error logs of an http server.

We are asked to find the ip address of the attacker.

The ip address is displayed on the left of every line : 165.227.73.138

## ToolBox

We are given the same files as before, we are asked to find which tool has been used at the beggining of the attack.

When we look at the user-agents used in the first part of the attack (for exemple at line 3), we can see `Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)` and more particularly `Nmap Scripting Engine`.

The tool used at the begining is Nmap then.

## GraveDigger 1

I didn't manage to solve thing challenge in time, but I understood the answer after :D

We are told in this challenge that `crypto_vamp`'s password in his friend's server is weak and has leaked : `123456789q` (we could have found this password using hydra and bruteforcing ssh with a dictionnary), we are also given the host name of the machine : `env.deadface.io`.

We are asked to find a flag associated with `Grave Digger 1`.

We can easily connect to the machine.

I tried to :
    - Enumerate file names containing `grave`, `digger` and `Grave Digger 1` : `find / -name "*grave*"`
    - Enumerate files which content contains the keywords : `grep -rnw / -e 'grave'`

But I didn't find anything.

Finally, by typing `env` (enumerates environement variables), I found the variable : `GRAVEDIGGER1=flag{d34dF4C3_en1roN_v4r}`.

## Agents of Chaos

This challenge is almost the same as ToolBox : we are asked to find the second tool used for the attack against the HTTP server (see First Strike and ToolBox).

We use the same technique as in ToolBox : we can find the user agent `Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:Port Check)` and more particularly `Nikto/2.1.6`.

The answer is Nikto then.

## Iterations

In this challenge we are asked which tool has likely been used to acquire credentials during the attack.

By looking at the user-agents I found `Mozilla/5.0 (Hydra)` and Hydra is indeed a tool that allows credentials bruteforce.

The answer is then Hydra.