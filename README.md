# Persistent Petitioners Optimal Deck

When I learned about the card Persistent Petitioner, I
was super excited. I had always loved the idea of Mill decks
and here is the opportunity to make a deck with just
Persistent Petitioners and Islands. So, if each players start out
with 60 cards, what is the optimal Persistent Petitioners (now abbreviated
as PP) to Island ratio?


![Image of Persistent Petitioners](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=457188&type=card)


I decided to approach this doing Monte Carlo simulations, with the assumption
that your opponent was not using removal or in any way destroying the PPs
each turn. This is way too idealistic, as removal, direct damage and even
having to sacrifice your creatures will happen during a real 
match. I figured the ideal deck would be a good proxy for the best
possible PP + Island only deck.

To run the simulation of all these decks with default values
(large number of runs, 60 cards per deck and trying every combination
of 0 lands to 60 lands).

```python
python persistent.py
```

With a small number of runs you'll get something like this:
```python
Islands	Min Turns	Max Turns	Average	Lost
0	-1		-1		-1	1000
1	-1		-1		-1	1000
2	-1		53		31	103
3	8		53		28	0
4	8		52		22	0
5	6		50		19	0
6	6		48		16	0
7	6		37		14	0
8	6		36		13	0
9	6		38		12	0
10	6		35		10	0
11	6		32		10	0
12	6		29		9	0
13	6		28		9	0
14	6		26		8	0
15	6		23		8	0
16	6		22		8	0
17	6		23		7	0
18	6		22		7	0
19	6		18		7	0
20	6		22		7	0
21	6		17		7	0
22	6		15		7	0
23	6		14		7	0
24	6		13		6	0
25	6		14		6	0
26	6		16		6	0
27	6		14		6	0
28	6		12		6	0
29	6		14		7	0
30	6		13		6	0
31	6		14		7	0
32	6		13		7	0
33	6		17		7	0
34	6		15		7	0
35	6		16		7	0
36	6		16		7	0
37	6		17		7	0
38	6		18		7	0
39	6		19		8	0
40	6		21		8	0
41	6		18		8	0
42	6		23		9	0
43	6		23		9	0
44	6		24		9	0
45	6		26		11	0
46	7		31		11	0
47	7		29		12	0
48	7		31		13	0
49	7		31		14	0
50	7		37		15	0
51	7		34		16	0
52	7		39		18	0
53	7		41		19	0
54	7		44		21	0
55	7		43		23	0
56	7		51		25	0
57	16		52		28	0
58	20		53		33	0
59	-1		53		37	17
60	-1		-1		-1	1000
```

So if a deck has less than 2 islands or is all islands, then
there are either not enough mana to cast PPs or no PPs to cast.
These all result in 1000 losses (no wins). I went with the balance
of lowest average first and then bring down lowest maximum.
This led me to use 24 islands in one deck and 36 PPs.

If your opponent has 200 cards in their deck and you have 60, the optimal
deck is 22 islands and 38 PPs and you could win in 12 turns.

In a game where both of you have 40 cards, you'll want 18 islands and 22 PPs.