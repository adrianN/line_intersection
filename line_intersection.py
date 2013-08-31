from bisect import bisect_left, insort

class search:
	def __init__(self):
		self.values = []
	def insert(self, value):
		assert not value in self.values
		print "insert", value
		insort(self.values, value)

	def delete(self, value):
		assert value in self.values
		print "delete", value
		assert(self.values.pop(self.position(value)) == value)

	def find_neighbors(self, value):
		p = self.position(value)
		l = None
		r = None
		if p>0: l = self.values[p-1]
		if p<len(self.values)-1: r = self.values[p+1]
		return (l,r)

	def position(self, value):
	    i = bisect_left(self.values, value)
	    if i != len(self.values) and self.values[i] == value:
	        return i
	    raise ValueError

def cross_product((x1,y1), (x2,y2)):
	return x1*y2 - y1*x2

def intersect((o1,p1), (o2,p2)):
	d1 = (p1[0]-o1[0], p1[1]-o1[1])
	d2 = (p2[0]-o2[0], p2[1]-o2[1])

	cross = cross_product(d1,d2)
	
	x = (o2[0]-o1[0], o2[1]-o1[1])

	if abs(cross) == 0:
		#in the collinear case t or u are also zero, I think
		return False

	t = cross_product(x,d2)
	u = cross_product(x,d1)

	t = float(t)/cross
	u = float(u)/cross
	
	if 0<t<1 and 0<u<1:
		# print "intersection", (o1,p1), (o2,p2)
		inter1 = (o1[0]+p1[0]*u,o1[1]+p1[1]*u)
		inter2 = (o2[0]+p2[0]*t, o2[1]+p2[1]*t)
		# print t,u, inter1, inter2
		return True

	return False

def base_direction_transform(line_segments):
	for (x1,y1), (x2,y2) in line_segments:
		yield (x1,x2), (x2-x1, y2-y1)


def line_intersections(line_segments):
	""" A line is defined by a start point and an end point """	
	end_points = []
	for i, ((x,_), (x2,_)) in enumerate(line_segments):
		end_points.append((x,i,x>=x2))
		end_points.append((x2,i,x<x2))

	end_points = sorted(end_points)
	search_thingy = search()

	for _, label, is_right in end_points:
		segment = line_segments[label]
		if not is_right:
			search_thingy.insert(label)
			for n in search_thingy.find_neighbors(label):
				if n is not None and intersect(segment, line_segments[n]):
					yield segment, line_segments[n]
		else:
			p,s = search_thingy.find_neighbors(label)
			if p is not None and s is not None:
				pred = line_segments[p]
				succ = line_segments[s]
				if intersect(pred,succ):
					yield pred,succ
			search_thingy.delete(label)

