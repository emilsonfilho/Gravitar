from configs.constants import G

def computeAllAccelerations(bodies):
    newAccelerations = []
    
    for body in bodies:
        newAccelerations.append(body.computeAcceleration(bodies))
        
    return newAccelerations