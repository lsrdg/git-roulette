```
  ____ _ _        ____             _      _   _        
 / ___(_) |_     |  _ \ ___  _   _| | ___| |_| |_ ___  ~
| |  _| | __|____| |_) / _ \| | | | |/ _ \ __| __/ _ \ ~
| |_| | | ||_____|  _ < (_) | |_| | |  __/ |_| ||  __/ ~
 \____|_|\__|    |_| \_\___/ \__,_|_|\___|\__|\__\___| ~

```

Don't waste time organizing things for the next you get lost.

Git-roulette will take a Github user's name and randomly choose a repository
with the `--gh` option:

```
$ python git-roulette --gh lsrdg
iscrap
```
Now, just go work on that project, delete it, rewrite, reread, write
documentation, toast, cry, just be creative.

If you are feeling really bothered you can get a list of a user's repositories.
Maybe for reference, or maybe you just find something interesting.

Git-roulette will take a Github user's name and list all of its repositories with
the `--ghl` argument:

```
$ python git-roulette --ghl lsrdg
bashscripts
cirkoan
deoplete.nvim
dotfiles... etc
```
### Create an alias

If are lazy to even decide on which project you are going to work, you probably
don't wanna bother to write `p-y-t-h-o-n- -g-i-t--r-o-u-l-e-t-t-e`.
Open your `~/.bashrc` and create an alias, something like:

```
# git-roulette
alias gtr='python ~/PATH/TO/git-roulette/git-roulette.py'
```

Now, typing `gtr` will be equivalent to `python ~/PATH/TO/git-roulette/git-roulette.py`. 
However, *note* that `Python` should point to _Python3_.

## Contributing

Seriously? :D

## Random futurechangelog

- [ ] Add access to the Gitlab's API
- [ ] Add access to local repositories

## License

DWYWWIBDIY. Seriouly.
DWYWWIBDIY = Do whatever you want with it but do it yourself.
