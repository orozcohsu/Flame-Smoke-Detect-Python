#! /usr/bin/env python
# coding=utf-8
import cv2

help_message = '''
*******************************INFO************************************
USAGE: click.py <image_names> ...

Click the picture show the coordinate and BGR value of the point, ESC to stop.
*****************************INFO_END**********************************
'''


def coordinate(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONUP:
        print "*" * 20
        print 'Coordinate: %s' % [x, y]
        print 'BGR: %s' % img[x][y]


if __name__ == '__main__':
    import sys
    from glob import glob
    import itertools as it

    print help_message

    img = None

    for fn in it.chain(*map(glob, sys.argv[1:])):
        print 'the picture:',
        print fn
        try:
            img = cv2.imread(fn)
            print 'image'
            if img is None:
                print 'Failed to load image file:', fn
                continue
        except:
            print 'loading error'
            continue
    if img is None:
        print 'please input the right order !!!\n'
    else:
        width, height, r = img.shape
        print "size of the picture: {}*{}px".format(width, height)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', coordinate)

        while True:
            cv2.imshow('image', img)
            if cv2.waitKey(0) & 0xFF == 27:
                break
            else:
                continue

    cv2.destroyAllWindows()
