
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
            #  'a': len(os.listdir(directory+"/BA")),
            #  'b': len(os.listdir(directory+"/BHA")),
            #  'c': len(os.listdir(directory+"/CHA")),
            #  'd': len(os.listdir(directory+"/CHHA")),
            #  'e': len(os.listdir(directory+"/DA")),
            #  'f': len(os.listdir(directory+"/DAA")),

            #  'g': len(os.listdir(directory+"/DHA")),
            #  'h': len(os.listdir(directory+"/DHAA")),
            #  'i': len(os.listdir(directory+"/DSA")),


            #  'j': len(os.listdir(directory+"/GA")),
             'k': len(os.listdir(directory+"/GHA")),
             'l': len(os.listdir(directory+"/GYA")),


             'm': len(os.listdir(directory+"/HA")),
             'n': len(os.listdir(directory+"/JA")),
             'o': len(os.listdir(directory+"/JHA")),
             'p': len(os.listdir(directory+"/KA")),
             'q': len(os.listdir(directory+"/KHA")),
             'r': len(os.listdir(directory+"/KSHA")),
             's': len(os.listdir(directory+"/LA")),

             't': len(os.listdir(directory+"/MA")),
             'u': len(os.listdir(directory+"/MSHA")),
             'v': len(os.listdir(directory+"/NA")),
             'w': len(os.listdir(directory+"/NAA")),
             'x': len(os.listdir(directory+"/NGA")),
             'y': len(os.listdir(directory+"/PA")),
             'z': len(os.listdir(directory+"/PHA")),
             'a': len(os.listdir(directory+"/RA")),
             'b': len(os.listdir(directory+"/TA")),
             'c': len(os.listdir(directory+"/TAA")),
             
             'd': len(os.listdir(directory+"/THA")),
             'e': len(os.listdir(directory+"/THAA")),
             'f': len(os.listdir(directory+"/TRA")),
             'g': len(os.listdir(directory+"/TSHA")),
             'h': len(os.listdir(directory+"/WA")),
             'i': len(os.listdir(directory+"/YA")),
             'j': len(os.listdir(directory+"/YAN")),
             
             
             }
  
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)

    # if interrupt & 0xFF == ord('a'):
    #     cv2.imwrite(directory+'BA/'+str(count['a'])+'.png',frame)
    # if interrupt & 0xFF == ord('b'):
    #     cv2.imwrite(directory+'BHA/'+str(count['b'])+'.png',frame)
    # if interrupt & 0xFF == ord('c'):
    #     cv2.imwrite(directory+'CHA/'+str(count['c'])+'.png',frame)
    # if interrupt & 0xFF == ord('d'):
    #     cv2.imwrite(directory+'CHHA/'+str(count['d'])+'.png',frame)
    # if interrupt & 0xFF == ord('e'):
    #     cv2.imwrite(directory+'DA/'+str(count['e'])+'.png',frame)
    # if interrupt & 0xFF == ord('f'):
    #     cv2.imwrite(directory+'DAA/'+str(count['f'])+'.png',frame)

    # if interrupt & 0xFF == ord('g'):
    #     cv2.imwrite(directory+'DHA/'+str(count['g'])+'.png',frame)
    # if interrupt & 0xFF == ord('h'):
    #     cv2.imwrite(directory+'DHAA/'+str(count['h'])+'.png',frame)
    # if interrupt & 0xFF == ord('i'):
    #     cv2.imwrite(directory+'DSA/'+str(count['i'])+'.png',frame)

    # if interrupt & 0xFF == ord('j'):
    #     cv2.imwrite(directory+'GA/'+str(count['j'])+'.png',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'GHA/'+str(count['k'])+'.png',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'GYA/'+str(count['l'])+'.png',frame)

    #13-19
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'HA/'+str(count['m'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'JA/'+str(count['n'])+'.png',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'JHA/'+str(count['o'])+'.png',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'KA/'+str(count['p'])+'.png',frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'KHA/'+str(count['q'])+'.png',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'KSHA/'+str(count['r'])+'.png',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'LA/'+str(count['s'])+'.png',frame)
  
    #20-29
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'MA/'+str(count['t'])+'.png',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'MSHA/'+str(count['u'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'NA/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'NAA/'+str(count['w'])+'.png',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'NGA/'+str(count['x'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'PA/'+str(count['y'])+'.png',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'PHA/'+str(count['z'])+'.png',frame)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'RA/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'TA/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'TAA/'+str(count['c'])+'.png',frame)
    
    #30-36
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'THA/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'THAA/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'TRA/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'TSHA/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'WA/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'YA/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'YAN/'+str(count['j'])+'.png',frame)
  

cap.release()
cv2.destroyAllWindows()