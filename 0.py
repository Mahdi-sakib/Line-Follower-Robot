from controller import Robot
robot=Robot()
timestep = int(robot.getBasicTimeStep())
time_step=32
max_speed=6.28
#motor
left_motor_front= robot.getDevice('wheel2')
left_motor_front.setPosition(float('inf'))
left_motor_front.setVelocity(0.0)


right_motor_front= robot.getDevice('wheel1')
right_motor_front.setPosition(float('inf'))
right_motor_front.setVelocity(0.0)

left_motor_back= robot.getDevice('wheel4')
left_motor_back.setPosition(float('inf'))
left_motor_back.setVelocity(0.0)


right_motor_back= robot.getDevice('wheel3')
right_motor_back.setPosition(float('inf'))
right_motor_back.setVelocity(0.0)


right_ir=robot.getDevice('ds_right')
right_ir.enable(time_step)
mid_ir=robot.getDevice('ds_mid')
mid_ir.enable(time_step)
left_ir=robot.getDevice('ds_left')
left_ir.enable(time_step)

while robot.step(timestep) !=-1:
   right_ir_val = right_ir.getValue()
   mid_ir_val = mid_ir.getValue()
   left_ir_val = left_ir.getValue()
   
   print("left: {} mid: {} right: {}".format(left_ir_val,mid_ir_val,right_ir_val))
   
   left_speed_f = max_speed
   right_speed_f = max_speed
   left_speed_b = max_speed
   right_speed_b = max_speed 
   
   
   if left_ir_val<1000 and right_ir_val<1000 and mid_ir_val>=1000:
    left_motor_front.setVelocity(left_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_front.setVelocity(right_speed_f)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val<1000 and right_ir_val>=1000 and mid_ir_val>=1000:
    left_motor_front.setVelocity(left_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_front.setVelocity(0)
    right_motor_back.setVelocity(0)   
    
   if left_ir_val>=1000 and right_ir_val<1000 and mid_ir_val>=1000:
    left_motor_front.setVelocity(0)
    left_motor_back.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    right_motor_back.setVelocity(right_speed_b) 
    
   if left_ir_val>=1000 and right_ir_val<1000 and mid_ir_val<1000:
    left_motor_front.setVelocity(0)
    left_motor_back.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    right_motor_back.setVelocity(right_speed_b) 
    
   if left_ir_val<1000 and right_ir_val>=1000 and mid_ir_val<1000:
    right_motor_front.setVelocity(0)
    right_motor_back.setVelocity(0)
    left_motor_front.setVelocity(left_speed_f)
    right_motor_back.setVelocity(right_speed_b)  
    
   if left_ir_val<1000 and right_ir_val<1000 and mid_ir_val<1000:
    left_motor_front.setVelocity(left_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_front.setVelocity(right_speed_f)
    right_motor_back.setVelocity(right_speed_b) 
    
    pass   