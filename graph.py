#!/usr/bin/env python3

#
# (c) 2017 by Chris Zimmermann
#

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
#
# Plot charts based on overall commits
#

import pygal
from pygal.style import LightGreenStyle

#
# Read commits from file and return dict in the shape: {YYYMM: # of commits}
#

def readCommits(fileN):
    commitD = {}
    with open(fileN, 'rt') as f:
        for i in f:
            lin = i.split(':')
            dateL = lin [1].rstrip().lstrip().replace('-', '').split(' ')
            for j in dateL:
                dateP = j [:6]
                if dateP in commitD:
                    commitD [dateP] += 1
                else:
                    commitD [dateP] = 1

    return commitD

#
# Accumulate monthly commits yielding a dict in the shape: {YYYY: # of commits }
#

def sumYear(years):
    totals = {}
    for y in years.keys():
        year = y [:4]
        if year in totals:
            totals [year] += years [y]
        else:
            totals [year] = years [y]

    return totals

# Plot bar chart from dict

def plot(data):
    style = LightGreenStyle
    style.label_font_size = 25
    style.title_font_size = 35
    linec = pygal.Bar(style = style, show_legend = False)
    linec.title = ''
    linec.x_labels = map(str, range(2007, 2016))

    li = []
    for i in range(2007, 2016):
        a = str(i)
        li.append(data [a])
    linec.add('b43', li)

    return linec

def main():

    # Assuming we find the data in the file 'commits.txt' (cf. 
    commitD = readCommits('commits.txt')
    accD = sumYear(commitD)
    linec = plot(accD)
    linec.render_to_png('com.png')
    linec.render_to_file('com.svg')
    
if __name__ == '__main__':
    exit (main())

