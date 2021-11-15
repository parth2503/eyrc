class Robot:
    def __init__(self,x,y,facing):
        self.x=x
        self.y=y
        self.facing=facing

    def next(self):
        if(self.facing=='east'):
            return [x+1][y]
        elif self.facing=='west':
            return [x-1][y]
        elif self.facing=='north':
            return y+1
        return y-1


    def right(self):
        if(self.facing=='east'):
            self.facing='south'
        elif(self.facing=='south'):
            self.facing='west'
        elif(self.facing=='west'):
            self.facing='north'
        elif(self.facing=='north'):
            self.facing='east'
    def left(self):
        if(self.facing=='east'):
            self.facing='north'
        elif(self.facing=='north'):
            self.facing='west'
        elif(self.facing=='west'):
            self.facing='south'
        elif(self.facing=='south'):
            self.facing='east'
    def move(self):

        if(self.facing=='east'):
            self.x+=1
        elif(self.facing=='south'):
            self.y-=1
        elif(self.facing=='west'):
            self.x-=1
        elif(self.facing=='north'):
            self.y+=1

    def report(self):
        print(self.x,self.y,self.facing)

    def check(self):
        for [x,y,facing] in obstacles:    
            if(x==self.x and y==self.y and facing==self.facing):
                return False
        if self.y==1 and self.facing=='south':
            return False      
        if self.y==5 and self.facing=='north':
            return False        
        if self.x==1 and self.facing=='west':
            return False        
        if self.x==5 and self.facing=='east':
            return False
        return True

start=[1,1,'south']
stop=[2,2]
obstacles=[[2,1,'east'],[3,1,'west'],[3,2,'north'],[3,3,'south'],[3,3,'north'],[3,4,'south'],[4,3,'north'],[4,4,'south'],[1,1,'north'],[1,2,'south'],[2,3,'north'],[2,4,'south']]
f1=True
f2=True

robot=Robot(start[0],start[1],start[2])

solved=False

visited=[[False for i in range(6)] for j in range(6)]

def solve(robot):

    if visited[robot.x][robot.y]:
        return False

    visited[robot.x][robot.y]=True
    robot.report()
    if(robot.x==stop[0] and robot.y==stop[1]):
        solved=True
        return True

    if robot.check():
        robot.move()
        if solve(robot):
            return True
        else:
            robot.left()
            robot.report()
            robot.left()
            robot.report()
            robot.move()

    robot.right()
    robot.report()
    if robot.check():
        robot.move()
        if solve(robot):
            return True
        else:
            robot.left()
            robot.report()
            robot.left()
            robot.report()
            robot.move()

    robot.left()
    robot.report()
    robot.left()
    robot.report()
    if robot.check():
        robot.move()
        if solve(robot):
            return True
        else:
            robot.left()
            robot.report()
            robot.left()
            robot.report()
            robot.move()

    robot.left()
    robot.report()
    if robot.check():
        robot.move()
        if solve(robot):
            return True
        else:
            robot.left()
            robot.report()
            robot.left()
            robot.report()
            robot.move()

    visited[robot.x][robot.y]=False

solve(robot)


'''
    og=robot
        
    if(robot.facing=='north'):
        robot.right()
    elif(robot.facing=='south'):
        robot.left()
    elif(robot.facing=='west'):
        robot.right()
        robot.right()

    if(robot.check()):
        robot.move()
        if not solve(robot):
            return False
        return True

    robot=og

    if(robot.facing=='east'):
        robot.left()
    elif(robot.facing=='west'):
        robot.right()
    elif(robot.facing=='south'):
        robot.right()
        robot.right()
    
    if(robot.check()):
        robot.move()
        if not solve(robot):
            return False
        return True


    robot=og

    if(robot.facing=='north'):
        robot.left()
    elif(robot.facing=='south'):
        robot.right()
    elif(robot.facing=='east'):
        robot.right()
        robot.right()

    if(robot.check()):
        robot.move()
        if not solve(robot):
            return False
        return True

    robot=og

    if(robot.facing=='west'):
        robot.left()
    elif(robot.facing=='east'):
        robot.right()
    elif(robot.facing=='north'):
        robot.right()
        robot.right()

    if(robot.check()):
        robot.move()
        if not solve(robot):
            return False
        return True

   
    return False
    '''  

        

'''
while(not(robot.x==stop[0] and robot.y==stop[1])):

    robot.report()

    if(robot.x<stop[0] and  f1):
        if(robot.facing=='north'):
            robot.right()
        elif(robot.facing=='south'):
            robot.left()
        elif(robot.facing=='west'):
            robot.right()
            robot.right()

    elif(robot.x>stop[0] and f1):
        if(robot.facing=='north'):
            robot.left()
        elif(robot.facing=='south'):
            robot.right()
        elif(robot.facing=='east'):
            robot.right()
            robot.right()

    elif(robot.y<stop[1] and f2):
        if(robot.facing=='east'):
            robot.left()
        elif(robot.facing=='west'):
            robot.right()
        elif(robot.facing=='south'):
            robot.right()
            robot.right()
    elif(robot.y>stop[1] and f2):
        if(robot.facing=='west'):
            robot.left()
        elif(robot.facing=='east'):
            robot.right()
        elif(robot.facing=='north'):
            robot.right()
            robot.right()
    
    robot.report()

    if(robot.check()):
        robot.move()
        f1=True
        f2=True
    else:
        if robot.facing=='east':
            f2=False
            if robot.y>stop[1]:
                robot.right()
                robot.move()
                robot.left()

                if not robot.check():
                    robot.left()
                    robot.move()
                    robot.move()
                    robot.right()     
                    
                    if not robot.check():
                        robot.right()
                        robot.move()
                        robot.right()            


            else:
                robot.left()
                robot.move()
                robot.right()

                if not robot.check():
                    robot.right()
                    robot.move()
                    robot.move()
                    robot.left()


                    if not robot.check():
                        robot.left()
                        robot.move()
                        robot.left()
        elif robot.facing=='west':
            f2=False
            if robot.y<stop[1]:
                robot.right()
                robot.move()
                robot.left()

                if not robot.check():
                    robot.left()
                    robot.move()
                    robot.move()
                    robot.right()

                    if not robot.check():
                        robot.right()
                        robot.move()
                        robot.right()
            else:
                robot.left()
                robot.move()
                robot.right()

                if not robot.check():
                    robot.right()
                    robot.move()
                    robot.move()
                    robot.left()


                    if not robot.check():
                        robot.left()
                        robot.move()
                        robot.left()
        elif robot.facing=='north':
            f1=False
            if robot.x<stop[1]:
                robot.right()
                robot.move()
                robot.left()

                if not robot.check():
                    robot.left()
                    robot.move()
                    robot.move()
                    robot.right()

                    if not robot.check():
                        robot.right()
                        robot.move()
                        robot.right()
            else:
                robot.left()
                robot.move()
                robot.right()

                if not robot.check():
                    robot.right()
                    robot.move()
                    robot.move()
                    robot.left()


                    if not robot.check():
                        robot.left()
                        robot.move()
                        robot.left()
        elif robot.facing=='south':
            f1=False
            if robot.y>stop[1]:
                robot.right()
                robot.move()
                robot.left()

                if not robot.check():
                    robot.left()
                    robot.move()
                    robot.move()
                    robot.right()

                    if not robot.check():
                        robot.right()
                        robot.move()
                        robot.right()
            else:
                robot.left()
                robot.move()
                robot.right()

                if not robot.check():
                    robot.right()
                    robot.move()
                    robot.move()
                    robot.left()


                    if not robot.check():
                        robot.left()
                        robot.move()
                        robot.left()
    robot.report() 

'''