def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[5]) <= (15.0):
        if (input[8]) <= (2.0):
            var0 = [0.0, 1.0, 0.0, 0.0]
        else:
            var0 = [0.0, 0.0, 0.0, 1.0]
    else:
        var0 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        var1 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            var1 = [0.0, 1.0, 0.0, 0.0]
        else:
            var1 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[6]) <= (1.5):
            var2 = [1.0, 0.0, 0.0, 0.0]
        else:
            var2 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[5]) <= (15.0):
            var2 = [0.0, 0.0, 0.0, 1.0]
        else:
            var2 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        if (input[1]) <= (2.5):
            var3 = [0.0, 0.0, 1.0, 0.0]
        else:
            var3 = [1.0, 0.0, 0.0, 0.0]
    else:
        var3 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[1]) <= (2.5):
            var4 = [0.0, 1.0, 0.0, 0.0]
        else:
            var4 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[8]) <= (1.5):
            var4 = [0.0, 0.0, 0.0, 1.0]
        else:
            var4 = [0.0, 0.0, 1.0, 0.0]
    if (input[8]) <= (2.0):
        if (input[1]) <= (2.5):
            var5 = [0.0, 0.0, 1.0, 0.0]
        else:
            var5 = [1.0, 0.0, 0.0, 0.0]
    else:
        var5 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        if (input[6]) <= (1.5):
            var6 = [1.0, 0.0, 0.0, 0.0]
        else:
            var6 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[5]) <= (15.0):
            var6 = [0.0, 0.0, 0.0, 1.0]
        else:
            var6 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        var7 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var7 = [0.0, 0.0, 1.0, 0.0]
        else:
            var7 = [0.0, 0.0, 0.0, 1.0]
    if (input[8]) <= (1.5):
        if (input[4]) <= (5.0):
            var8 = [0.0, 0.0, 0.0, 1.0]
        else:
            var8 = [0.0, 0.0, 1.0, 0.0]
    else:
        var8 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (17.5):
        if (input[6]) <= (1.5):
            var9 = [1.0, 0.0, 0.0, 0.0]
        else:
            var9 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[4]) <= (5.0):
            var9 = [0.0, 0.0, 0.0, 1.0]
        else:
            var9 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        var10 = [0.0, 0.0, 1.0, 0.0]
    else:
        var10 = [0.0, 0.0, 0.0, 1.0]
    if (input[7]) <= (60.0):
        var11 = [1.0, 0.0, 0.0, 0.0]
    else:
        var11 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[3]) <= (5.0):
            var12 = [1.0, 0.0, 0.0, 0.0]
        else:
            var12 = [0.0, 0.0, 1.0, 0.0]
    else:
        var12 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var13 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[3]) <= (5.0):
            var13 = [1.0, 0.0, 0.0, 0.0]
        else:
            var13 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        var14 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[0]) <= (14.0):
            var14 = [0.0, 1.0, 0.0, 0.0]
        else:
            var14 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        var15 = [0.0, 1.0, 0.0, 0.0]
    else:
        var15 = [0.0, 0.0, 0.0, 1.0]
    if (input[7]) <= (60.0):
        if (input[5]) <= (15.0):
            var16 = [0.0, 1.0, 0.0, 0.0]
        else:
            var16 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[7]) <= (75.0):
            var16 = [0.0, 0.0, 0.0, 1.0]
        else:
            if (input[5]) <= (15.0):
                var16 = [0.0, 0.0, 0.0, 1.0]
            else:
                var16 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        if (input[5]) <= (15.0):
            var17 = [0.0, 1.0, 0.0, 0.0]
        else:
            var17 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[0]) <= (24.5):
            var17 = [0.0, 0.0, 1.0, 0.0]
        else:
            var17 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[8]) <= (2.0):
            var18 = [1.0, 0.0, 0.0, 0.0]
        else:
            var18 = [0.0, 0.0, 1.0, 0.0]
    else:
        var18 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[0]) <= (14.0):
            var19 = [1.0, 0.0, 0.0, 0.0]
        else:
            var19 = [0.0, 0.0, 1.0, 0.0]
    else:
        var19 = [0.0, 0.0, 0.0, 1.0]
    if (input[7]) <= (65.0):
        if (input[6]) <= (1.5):
            var20 = [1.0, 0.0, 0.0, 0.0]
        else:
            var20 = [0.0, 1.0, 0.0, 0.0]
    else:
        var20 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var21 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[7]) <= (60.0):
            var21 = [1.0, 0.0, 0.0, 0.0]
        else:
            var21 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        var22 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[5]) <= (15.0):
            var22 = [0.0, 0.0, 0.0, 1.0]
        else:
            var22 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[3]) <= (5.0):
            var23 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[0]) <= (24.5):
                var23 = [0.0, 0.0, 1.0, 0.0]
            else:
                var23 = [0.0, 0.0, 0.0, 1.0]
    else:
        var23 = [1.0, 0.0, 0.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[7]) <= (65.0):
            var24 = [0.0, 1.0, 0.0, 0.0]
        else:
            var24 = [0.0, 0.0, 0.0, 1.0]
    else:
        var24 = [1.0, 0.0, 0.0, 0.0]
    if (input[6]) <= (1.5):
        if (input[4]) <= (5.0):
            var25 = [1.0, 0.0, 0.0, 0.0]
        else:
            var25 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[0]) <= (17.5):
            var25 = [0.0, 1.0, 0.0, 0.0]
        else:
            var25 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        var26 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var26 = [0.0, 0.0, 1.0, 0.0]
        else:
            var26 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var27 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[0]) <= (14.0):
            var27 = [1.0, 0.0, 0.0, 0.0]
        else:
            var27 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        if (input[6]) <= (1.5):
            var28 = [1.0, 0.0, 0.0, 0.0]
        else:
            var28 = [0.0, 1.0, 0.0, 0.0]
    else:
        var28 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[5]) <= (15.0):
            var29 = [0.0, 1.0, 0.0, 0.0]
        else:
            var29 = [1.0, 0.0, 0.0, 0.0]
    else:
        var29 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[0]) <= (14.0):
            var30 = [0.0, 1.0, 0.0, 0.0]
        else:
            var30 = [0.0, 0.0, 0.0, 1.0]
    else:
        var30 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        var31 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[0]) <= (14.0):
            var31 = [0.0, 1.0, 0.0, 0.0]
        else:
            var31 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[7]) <= (60.0):
            var32 = [1.0, 0.0, 0.0, 0.0]
        else:
            var32 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[3]) <= (5.0):
            if (input[7]) <= (60.0):
                var32 = [0.0, 1.0, 0.0, 0.0]
            else:
                var32 = [0.0, 0.0, 0.0, 1.0]
        else:
            var32 = [0.0, 0.0, 0.0, 1.0]
    if (input[8]) <= (2.0):
        if (input[6]) <= (1.5):
            var33 = [1.0, 0.0, 0.0, 0.0]
        else:
            var33 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            var33 = [0.0, 0.0, 1.0, 0.0]
        else:
            var33 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[1]) <= (2.5):
            var34 = [0.0, 0.0, 1.0, 0.0]
        else:
            var34 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[0]) <= (14.0):
            var34 = [0.0, 1.0, 0.0, 0.0]
        else:
            var34 = [0.0, 0.0, 0.0, 1.0]
    if (input[1]) <= (2.5):
        if (input[7]) <= (60.0):
            var35 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[4]) <= (5.0):
                var35 = [0.0, 0.0, 0.0, 1.0]
            else:
                var35 = [0.0, 0.0, 1.0, 0.0]
    else:
        var35 = [1.0, 0.0, 0.0, 0.0]
    if (input[7]) <= (60.0):
        if (input[5]) <= (15.0):
            var36 = [0.0, 1.0, 0.0, 0.0]
        else:
            var36 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[5]) <= (15.0):
            var36 = [0.0, 0.0, 0.0, 1.0]
        else:
            var36 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[6]) <= (1.5):
            var37 = [0.0, 0.0, 1.0, 0.0]
        else:
            var37 = [0.0, 0.0, 0.0, 1.0]
    else:
        var37 = [1.0, 0.0, 0.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[8]) <= (0.5):
            var38 = [0.0, 0.0, 0.0, 1.0]
        else:
            if (input[8]) <= (2.0):
                var38 = [0.0, 1.0, 0.0, 0.0]
            else:
                var38 = [0.0, 0.0, 0.0, 1.0]
    else:
        var38 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[3]) <= (5.0):
            var39 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[8]) <= (1.5):
                var39 = [0.0, 0.0, 0.0, 1.0]
            else:
                var39 = [0.0, 0.0, 1.0, 0.0]
    else:
        var39 = [1.0, 0.0, 0.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[0]) <= (14.0):
            var40 = [0.0, 1.0, 0.0, 0.0]
        else:
            var40 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[4]) <= (5.0):
            if (input[7]) <= (60.0):
                var40 = [1.0, 0.0, 0.0, 0.0]
            else:
                var40 = [0.0, 0.0, 1.0, 0.0]
        else:
            var40 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        var41 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[1]) <= (2.5):
            var41 = [0.0, 0.0, 1.0, 0.0]
        else:
            var41 = [1.0, 0.0, 0.0, 0.0]
    if (input[0]) <= (14.0):
        var42 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[3]) <= (5.0):
            if (input[7]) <= (75.0):
                var42 = [0.0, 0.0, 0.0, 1.0]
            else:
                var42 = [0.0, 0.0, 1.0, 0.0]
        else:
            var42 = [0.0, 0.0, 0.0, 1.0]
    if (input[4]) <= (5.0):
        if (input[0]) <= (14.0):
            var43 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[3]) <= (5.0):
                var43 = [0.0, 0.0, 0.0, 1.0]
            else:
                if (input[7]) <= (75.0):
                    var43 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var43 = [0.0, 0.0, 0.0, 1.0]
    else:
        var43 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[8]) <= (1.5):
            if (input[4]) <= (5.0):
                var44 = [0.0, 0.0, 0.0, 1.0]
            else:
                var44 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[3]) <= (5.0):
                var44 = [0.0, 0.0, 0.0, 1.0]
            else:
                var44 = [0.0, 0.0, 1.0, 0.0]
    else:
        var44 = [1.0, 0.0, 0.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[3]) <= (5.0):
            if (input[8]) <= (2.0):
                var45 = [0.0, 1.0, 0.0, 0.0]
            else:
                var45 = [0.0, 0.0, 0.0, 1.0]
        else:
            var45 = [0.0, 0.0, 0.0, 1.0]
    else:
        var45 = [0.0, 0.0, 1.0, 0.0]
    var46 = add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), var4), var5), var6), var7), var8), var9), var10), var11), var12), var13), var14), var15), var16), var17), var18), var19), var20), var21), var22), var23), var24), var25), var26), var27), var28), var29), var30), var31), var32), var33), var34), var35), var36), var37), var38), var39), var40), var41), var42), var43), var44), var45)
    if (input[5]) <= (15.0):
        var47 = [0.0, 0.0, 0.0, 1.0]
    else:
        var47 = [1.0, 0.0, 0.0, 0.0]
    if (input[4]) <= (5.0):
        if (input[6]) <= (1.5):
            var48 = [1.0, 0.0, 0.0, 0.0]
        else:
            var48 = [0.0, 1.0, 0.0, 0.0]
    else:
        var48 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        var49 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[4]) <= (5.0):
            if (input[8]) <= (1.5):
                var49 = [0.0, 0.0, 0.0, 1.0]
            else:
                var49 = [0.0, 0.0, 1.0, 0.0]
        else:
            var49 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[6]) <= (1.5):
            var50 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[8]) <= (0.5):
                var50 = [0.0, 0.0, 0.0, 1.0]
            else:
                if (input[0]) <= (14.0):
                    var50 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var50 = [0.0, 0.0, 0.0, 1.0]
    else:
        var50 = [1.0, 0.0, 0.0, 0.0]
    if (input[6]) <= (1.5):
        if (input[8]) <= (2.0):
            var51 = [1.0, 0.0, 0.0, 0.0]
        else:
            var51 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[7]) <= (65.0):
            var51 = [0.0, 1.0, 0.0, 0.0]
        else:
            var51 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        if (input[0]) <= (14.0):
            var52 = [0.0, 1.0, 0.0, 0.0]
        else:
            var52 = [0.0, 0.0, 0.0, 1.0]
    else:
        var52 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[0]) <= (14.0):
            var53 = [0.0, 1.0, 0.0, 0.0]
        else:
            var53 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[1]) <= (2.5):
            var53 = [0.0, 0.0, 1.0, 0.0]
        else:
            var53 = [1.0, 0.0, 0.0, 0.0]
    if (input[2]) <= (2.5):
        if (input[0]) <= (14.0):
            var54 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[5]) <= (15.0):
                var54 = [0.0, 0.0, 0.0, 1.0]
            else:
                var54 = [0.0, 0.0, 1.0, 0.0]
    else:
        var54 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        var55 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            if (input[5]) <= (15.0):
                var55 = [0.0, 0.0, 0.0, 1.0]
            else:
                var55 = [0.0, 0.0, 1.0, 0.0]
        else:
            var55 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        var56 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[0]) <= (14.0):
            var56 = [0.0, 1.0, 0.0, 0.0]
        else:
            var56 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[1]) <= (2.5):
            var57 = [0.0, 1.0, 0.0, 0.0]
        else:
            var57 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            var57 = [0.0, 0.0, 1.0, 0.0]
        else:
            var57 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        if (input[7]) <= (65.0):
            var58 = [1.0, 0.0, 0.0, 0.0]
        else:
            var58 = [0.0, 0.0, 1.0, 0.0]
    else:
        var58 = [0.0, 0.0, 0.0, 1.0]
    if (input[3]) <= (5.0):
        if (input[8]) <= (2.0):
            var59 = [1.0, 0.0, 0.0, 0.0]
        else:
            var59 = [0.0, 0.0, 0.0, 1.0]
    else:
        var59 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[7]) <= (60.0):
            var60 = [0.0, 1.0, 0.0, 0.0]
        else:
            var60 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[0]) <= (14.0):
            var60 = [1.0, 0.0, 0.0, 0.0]
        else:
            var60 = [0.0, 0.0, 1.0, 0.0]
    if (input[6]) <= (1.5):
        if (input[1]) <= (2.5):
            var61 = [0.0, 0.0, 1.0, 0.0]
        else:
            var61 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[0]) <= (14.0):
            var61 = [0.0, 1.0, 0.0, 0.0]
        else:
            var61 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        if (input[7]) <= (60.0):
            var62 = [0.0, 1.0, 0.0, 0.0]
        else:
            var62 = [0.0, 0.0, 0.0, 1.0]
    else:
        var62 = [0.0, 0.0, 1.0, 0.0]
    if (input[2]) <= (2.5):
        if (input[7]) <= (75.0):
            var63 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[4]) <= (5.0):
                var63 = [0.0, 0.0, 0.0, 1.0]
            else:
                var63 = [0.0, 0.0, 1.0, 0.0]
    else:
        var63 = [0.0, 0.0, 0.0, 1.0]
    if (input[7]) <= (60.0):
        var64 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[4]) <= (5.0):
            var64 = [0.0, 0.0, 0.0, 1.0]
        else:
            var64 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        if (input[6]) <= (1.5):
            var65 = [1.0, 0.0, 0.0, 0.0]
        else:
            var65 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[8]) <= (1.5):
            if (input[3]) <= (5.0):
                var65 = [0.0, 0.0, 1.0, 0.0]
            else:
                var65 = [0.0, 0.0, 0.0, 1.0]
        else:
            var65 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        var66 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var66 = [0.0, 0.0, 1.0, 0.0]
        else:
            var66 = [0.0, 0.0, 0.0, 1.0]
    if (input[4]) <= (5.0):
        if (input[7]) <= (60.0):
            var67 = [0.0, 1.0, 0.0, 0.0]
        else:
            var67 = [0.0, 0.0, 0.0, 1.0]
    else:
        var67 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        var68 = [1.0, 0.0, 0.0, 0.0]
    else:
        var68 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        var69 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[7]) <= (60.0):
            var69 = [1.0, 0.0, 0.0, 0.0]
        else:
            var69 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        if (input[5]) <= (15.0):
            var70 = [0.0, 1.0, 0.0, 0.0]
        else:
            var70 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[0]) <= (24.5):
            var70 = [0.0, 0.0, 0.0, 1.0]
        else:
            var70 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        var71 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[8]) <= (2.0):
            if (input[1]) <= (2.5):
                var71 = [0.0, 0.0, 1.0, 0.0]
            else:
                var71 = [1.0, 0.0, 0.0, 0.0]
        else:
            var71 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        if (input[1]) <= (2.5):
            var72 = [0.0, 1.0, 0.0, 0.0]
        else:
            var72 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var72 = [0.0, 0.0, 1.0, 0.0]
        else:
            var72 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[1]) <= (2.5):
            var73 = [0.0, 1.0, 0.0, 0.0]
        else:
            var73 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[7]) <= (75.0):
            if (input[3]) <= (5.0):
                var73 = [0.0, 0.0, 0.0, 1.0]
            else:
                var73 = [0.0, 0.0, 1.0, 0.0]
        else:
            var73 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[7]) <= (65.0):
            var74 = [0.0, 1.0, 0.0, 0.0]
        else:
            var74 = [0.0, 0.0, 0.0, 1.0]
    else:
        var74 = [0.0, 0.0, 1.0, 0.0]
    if (input[8]) <= (0.5):
        var75 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            if (input[6]) <= (1.5):
                var75 = [1.0, 0.0, 0.0, 0.0]
            else:
                var75 = [0.0, 1.0, 0.0, 0.0]
        else:
            var75 = [0.0, 0.0, 0.0, 1.0]
    if (input[6]) <= (1.5):
        var76 = [0.0, 0.0, 1.0, 0.0]
    else:
        var76 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        if (input[0]) <= (14.0):
            var77 = [0.0, 1.0, 0.0, 0.0]
        else:
            var77 = [0.0, 0.0, 0.0, 1.0]
    else:
        var77 = [1.0, 0.0, 0.0, 0.0]
    if (input[0]) <= (14.0):
        var78 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[5]) <= (15.0):
            var78 = [0.0, 0.0, 0.0, 1.0]
        else:
            var78 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (14.0):
        var79 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[0]) <= (24.5):
            var79 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[6]) <= (1.5):
                var79 = [0.0, 0.0, 1.0, 0.0]
            else:
                var79 = [0.0, 0.0, 0.0, 1.0]
    if (input[8]) <= (1.5):
        var80 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[5]) <= (15.0):
            var80 = [0.0, 0.0, 0.0, 1.0]
        else:
            var80 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        var81 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var81 = [0.0, 0.0, 1.0, 0.0]
        else:
            var81 = [0.0, 0.0, 0.0, 1.0]
    if (input[3]) <= (5.0):
        if (input[1]) <= (2.5):
            if (input[0]) <= (14.0):
                var82 = [0.0, 1.0, 0.0, 0.0]
            else:
                var82 = [0.0, 0.0, 0.0, 1.0]
        else:
            var82 = [1.0, 0.0, 0.0, 0.0]
    else:
        var82 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        var83 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[0]) <= (14.0):
            var83 = [1.0, 0.0, 0.0, 0.0]
        else:
            var83 = [0.0, 0.0, 1.0, 0.0]
    if (input[5]) <= (15.0):
        var84 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[3]) <= (5.0):
            if (input[1]) <= (2.5):
                var84 = [0.0, 0.0, 1.0, 0.0]
            else:
                var84 = [1.0, 0.0, 0.0, 0.0]
        else:
            var84 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (24.5):
        if (input[6]) <= (1.5):
            if (input[8]) <= (2.0):
                var85 = [1.0, 0.0, 0.0, 0.0]
            else:
                var85 = [0.0, 0.0, 1.0, 0.0]
        else:
            var85 = [0.0, 1.0, 0.0, 0.0]
    else:
        var85 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var86 = [0.0, 0.0, 0.0, 1.0]
    else:
        var86 = [0.0, 0.0, 1.0, 0.0]
    if (input[0]) <= (24.5):
        if (input[1]) <= (2.5):
            if (input[8]) <= (2.0):
                var87 = [0.0, 1.0, 0.0, 0.0]
            else:
                var87 = [0.0, 0.0, 0.0, 1.0]
        else:
            var87 = [1.0, 0.0, 0.0, 0.0]
    else:
        var87 = [0.0, 0.0, 1.0, 0.0]
    if (input[8]) <= (0.5):
        if (input[5]) <= (15.0):
            var88 = [0.0, 0.0, 0.0, 1.0]
        else:
            var88 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var88 = [1.0, 0.0, 0.0, 0.0]
        else:
            var88 = [0.0, 1.0, 0.0, 0.0]
    if (input[0]) <= (14.0):
        var89 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var89 = [0.0, 0.0, 1.0, 0.0]
        else:
            var89 = [0.0, 0.0, 0.0, 1.0]
    if (input[0]) <= (14.0):
        if (input[1]) <= (2.5):
            var90 = [0.0, 1.0, 0.0, 0.0]
        else:
            var90 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[2]) <= (2.5):
            var90 = [0.0, 0.0, 1.0, 0.0]
        else:
            var90 = [0.0, 0.0, 0.0, 1.0]
    if (input[2]) <= (2.5):
        if (input[0]) <= (14.0):
            var91 = [1.0, 0.0, 0.0, 0.0]
        else:
            var91 = [0.0, 0.0, 1.0, 0.0]
    else:
        var91 = [0.0, 0.0, 0.0, 1.0]
    if (input[2]) <= (2.5):
        if (input[8]) <= (2.0):
            if (input[6]) <= (1.5):
                var92 = [1.0, 0.0, 0.0, 0.0]
            else:
                var92 = [0.0, 1.0, 0.0, 0.0]
        else:
            var92 = [0.0, 0.0, 1.0, 0.0]
    else:
        var92 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var93 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[1]) <= (2.5):
            var93 = [0.0, 0.0, 1.0, 0.0]
        else:
            var93 = [1.0, 0.0, 0.0, 0.0]
    if (input[0]) <= (14.0):
        var94 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[3]) <= (5.0):
            var94 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[7]) <= (75.0):
                var94 = [0.0, 0.0, 1.0, 0.0]
            else:
                var94 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        var95 = [0.0, 0.0, 0.0, 1.0]
    else:
        var95 = [0.0, 0.0, 1.0, 0.0]
    if (input[8]) <= (2.0):
        var96 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[6]) <= (1.5):
            var96 = [0.0, 0.0, 1.0, 0.0]
        else:
            var96 = [0.0, 0.0, 0.0, 1.0]
    if (input[5]) <= (15.0):
        if (input[8]) <= (0.5):
            var97 = [0.0, 0.0, 0.0, 1.0]
        else:
            var97 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[7]) <= (60.0):
            var97 = [1.0, 0.0, 0.0, 0.0]
        else:
            var97 = [0.0, 0.0, 1.0, 0.0]
    if (input[1]) <= (2.5):
        if (input[3]) <= (5.0):
            if (input[5]) <= (15.0):
                var98 = [0.0, 0.0, 0.0, 1.0]
            else:
                var98 = [0.0, 0.0, 1.0, 0.0]
        else:
            var98 = [0.0, 0.0, 1.0, 0.0]
    else:
        var98 = [1.0, 0.0, 0.0, 0.0]
    if (input[5]) <= (15.0):
        if (input[7]) <= (60.0):
            var99 = [0.0, 1.0, 0.0, 0.0]
        else:
            var99 = [0.0, 0.0, 0.0, 1.0]
    else:
        var99 = [0.0, 0.0, 1.0, 0.0]
    if (input[7]) <= (60.0):
        if (input[5]) <= (15.0):
            var100 = [0.0, 1.0, 0.0, 0.0]
        else:
            var100 = [1.0, 0.0, 0.0, 0.0]
    else:
        var100 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(var46, var47), var48), var49), var50), var51), var52), var53), var54), var55), var56), var57), var58), var59), var60), var61), var62), var63), var64), var65), var66), var67), var68), var69), var70), var71), var72), var73), var74), var75), var76), var77), var78), var79), var80), var81), var82), var83), var84), var85), var86), var87), var88), var89), var90), var91), var92), var93), var94), var95), var96), var97), var98), var99), var100), 0.01)

