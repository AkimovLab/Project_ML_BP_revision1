mol load cube job1/Diag_libra-3750-WFN_00157_1-1_0.cube
display projection Orthographic
axes location Off
menu files off
menu files on
display resetview
display resetview
mol delrep 0 0
mol addrep 0
display resetview
animate style Loop
menu color off
menu color on
color Display Background white
menu color off

proc rotate_axis {vec deg {molid top}} {
    # get the current matrix
    lassign [molinfo $molid get rotate_matrix] curr
    # the transformation matrix
    set r [trans axis $vec $deg]
    # get the new matrix
    set m [transmult $r $curr]
    # and apply it to the molecule
    molinfo $molid set rotate_matrix "{ $m }"
}

# around the X axis
#rotate_axis {1 0 0} 90
#rotate_axis {0 1 0} 180

scale by 1.800000 


menu graphics off
menu graphics on

mol modstyle 0 0 CPK 1.000000 0.300000 12.000000 12.000000
mol color Name
mol representation CPK 1.000000 0.300000 12.000000 12.000000
mol selection all
mol material Opaque
mol addrep 0
mol modcolor 1 0 ColorID 0
mol modstyle 1 0 Isosurface 0.000000 0 2 2 1 1
mol modcolor 1 0 ColorID 24
mol modstyle 1 0 Isosurface 0.000000 0 2 0 1 1
mol modstyle 1 0 Isosurface 0.000000 0 0 0 1 1
mol modstyle 1 0 Isosurface -0.015000 0 0 0 1 1
mol color ColorID 24
mol representation Isosurface -0.015000 0 0 0 1 1
mol selection all
mol material Opaque
mol addrep 0
mol modcolor 2 0 ColorID 30
mol modstyle 2 0 Isosurface 0.015000 0 0 0 1 1
menu graphics off
menu render off
menu render on
render Tachyon Diag_libra-3750- "/opt/vmd/lib/tachyon_LINUXAMD64 -aasamples 12 %s -format TGA -res 2048 2048 -o %s.tga"
mol delete 0
