
def cyrus_beck_3d(line,prism_dimensions):
    """
    This Implements the Cyrus-Beck Algorithm for 3D line clipping against a rectangular prism.
    :param line:
    :param prism_dimensions:
    :return:
    """
    p0,p1 = line
    x0,y0,z0 = p0
    x1,y1,z1 = p1
    d=(x1-x0,y1-y0,z1-z0)

    (x_min,x_max),(y_min,y_max),(z_min,z_max)=prism_dimensions

    #Defining planes of the prism (normal,point on plane)

    planes=[
        ((1,0,0),(x_min,0,0)), # left
        ((-1,0,0),(x_max,0,0)), # right
        ((0,1,0),(0,y_min,0)), # bottom
        ((0,-1,0),(0,y_max,0)), # top
        ((0,0,1),(0,0,z_min)), # back
        ((0,0,-1),(0,0,z_max))  # front
    ]

    t_enter=0
    t_exit=1

    for normal,point in planes:
        n_dot_d = sum(n*d_i for n,d_i in zip(normal,d))
        if n_dot_d == 0:
            continue
        n_dot_p0=sum(n*(p0_i-point_i) for n,p0_i,point_i in zip(normal,p0,point))
        t=-n_dot_p0/n_dot_d
        if n_dot_d<0:
            t_enter=max(t_enter,t)
        else:
            t_exit=min(t_exit,t)

    if t_enter>t_exit:
        return None

    #clipped points
    clipped_p0=(
        x0+t_enter*d[0],
        y0+t_enter*d[1],
        z0+t_enter*d[2]
    )

    clipped_p1=(
        x0+t_exit*d[0],
        y0+t_exit*d[1],
        z0+t_exit*d[2]
    )

    return [clipped_p0,clipped_p1]



