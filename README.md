RECALL
======

Utility for saving and re-running bash commands in a system-wide repository



Setup

Put this in your .zshrc: 

`
precmd() {
    export LAST_COMMAND=$(fc -ln -1)
}
`