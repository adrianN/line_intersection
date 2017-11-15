Line Segment Intersection
=================

Detecting line segment intersections using the sweepline algorithm in Python.

I'm not completely sure that this is correct, but it seems to work at least if the lines are in general position. I used it to check whether a graph embedding contains crossing edges. Since many edges share endpoints (the vertices..), this code does not report an intersection if a line starts on another.

This code uses the sweep line algorithm as explained [here](http://www.cs.uiuc.edu/~jeffe/teaching/373/notes/x06-sweepline.pdf). However, I don't use a balanced search tree, instead I insertion-sort a list, so the worst case performance is quadratic. It seems to be reasonably fast on the instances I tried anyway. It should be simple to replace the search structure if it's too slow for you.
