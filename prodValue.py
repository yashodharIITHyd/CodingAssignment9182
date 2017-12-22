class greatestProductValue:
	def __init__(self,mat,count):
		self.mat = mat
		self.m = len(mat)
		self.n = len(mat[0])
		self.count=count

	def getVertical(self,i,j):
		val=1
		count=0
		x,y = i,j
		while i<self.m and count<self.count:
			val*=self.mat[i][j]
			i+=1
			count+=1
		return {'status':count==self.count,'data':val,'direction':'vertical','x':x,'y':y}

	def getHorizontal(self,i,j):
		val=1
		count=0
		x,y = i,j
		while j<self.n and count<self.count:
			val*=self.mat[i][j]
			j+=1
			count+=1
		return {'status':count==self.count,'data':val,'direction':'horizontal','x':x,'y':y}

	def getRightDiagonal(self,i,j):
		val=1
		count=0
		x,y = i,j
		while j<self.n and i<self.m and count<self.count:
			val*=self.mat[i][j]
			j+=1
			i+=1
			count+=1
		return {'status':count==self.count,'data':val,'direction':'rightDiagonal','x':x,'y':y}

	def getLeftDiagonal(self,i,j):
		val=1
		count=0
		x,y = i,j
		while i<self.m and j<self.n and count<self.count:
			val*=self.mat[i][j]
			j-=1
			i+=1
			count+=1
		return {'status':count==self.count,'data':val,'direction':'leftDiagonal','x':x,'y':y}

	def calculate(self):
		value = {'data':-float('Inf')}
		for i in xrange(0,self.m):
			for j in xrange(0,self.n):
				values = [self.getLeftDiagonal(i,j),self.getRightDiagonal(i,j),self.getHorizontal(i,j),self.getVertical(i,j)]
				values = filter((lambda e : e['status']==True),values)
				if len(values)>0:
					value2 = max(values,key=lambda e : e['data'])
					if value['data']<value2['data']:
						value = value2
		print 'Value : ',value['data']
		x,y=value['x'],value['y']
		print 'position x : ',x,' y : ',y
		print 'direction : ',value['direction']

f1 = open('matrix.txt','r')
mat=[map(int,line.strip().split(' ')) for line in f1]
g1 = greatestProductValue(mat,4)
g1.calculate()