import numpy as np

class xy_move():
    def __init__(self,):
        pass
    def reset(self):
        self.target_x=0
        self.target_y=0
        self.move_x=20
        self.move_y=20

        state=np.array([self.target_x, self.target_y, self.move_x, self.move_y])
        return state
        
    def step(self, action):
        if action==0:
            self.move_y=self.move_y+1
        if action==1:
            self.move_y=self.move_y-1
        if action==2:
            self.move_x=self.move_x+1
        if action==3:
            self.move_x=self.move_x-1

        next_state=np.array([self.target_x, self.target_y, self.move_x, self.move_y])

        reward=-1
        if ((self.move_x-self.target_x)**2+(self.move_y-self.target_y)**2)==0:            
            done=1
        else:
            done=0

        return next_state, reward, done, 'info'
        
