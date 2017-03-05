Code snippets for B43 visualization:

git_stats.sh: pull b43 commits from clones kernel git repo and store in commits.txt
graphy.py: aggregate sums in commits.txt, convert to bar chart and store in png and svg files

Caveat: as graph.py expects the numbers in a file "commits.txt", please change also in git_stat.sh if you modify this file name 
