import OpenGL.GL as gl
import pangolin
import cv2
import numpy as np
import time
import parser


def main():
    image = cv2.imread("723.jpg",0)
    pangolin.CreateWindowAndBind('Main', 820, 640)
    gl.glEnable(gl.GL_DEPTH_TEST)

    # Define Projection and initial ModelView matrix
    scam = pangolin.OpenGlRenderState(
        pangolin.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.2, 100),
        pangolin.ModelViewLookAt(30, -20, 76, 0, 0, 0, pangolin.AxisDirection.AxisY))
    handler = pangolin.Handler3D(scam)

    # Create Interactive View in window
    dcam = pangolin.CreateDisplay()
    dcam.SetBounds(0.0, 1.0, 0.0, 1.0, -640.0/480.0)
    dcam.SetHandler(handler)

    while not pangolin.ShouldQuit():
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glClearColor(0, 0, 0, 0)
        dcam.Activate(scam)
        
        # Render OpenGL Cube
        pangolin.glDrawColouredCube()

        # Draw Point Cloud
        #points = np.random.random((3,3)) 
        
        points = np.array([ [1, 0, 0],[1.4, 0, 0],[2.1, -0.5, 0.1] ]) 
        
        points = points*np.array([1,1,-1])
        
        pos,pixels = parser.get_data("but.jpg", 3)
        
        #print  (points)
        
        #points = image/255 
        #colors = np.zeros((len(points), 3))
        #colors[:, 1] = 1 -points[:, 0] / 10.
        #colors[:, 2] = 1 - points[:, 1] / 10.
        #colors[:, 0] = 1 - points[:, 2] / 10.

        gl.glPointSize(2)
        gl.glColor3f(1.0, 0.0, 0.0)
        # access numpy array directly(without copying data), array should be contiguous.
        #pangolin.DrawPoints(points, colors)    
        #pangolin.DrawPoints(points)
        pangolin.DrawPoints(pos,pixels)
        #time.sleep(0.5)
        pangolin.FinishFrame()

if __name__ == '__main__':
    main()