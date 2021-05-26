import numpy as np

def Hubeny(lat0, lon0, lat1, lon1):
    """ 距離[m]算出 """
    Dy = (lat1 - lat0) * np.pi/180    # 2点の緯度(ラジアン)の差
    Dx = (lon1 - lon0) * np.pi/180    # 2点の軽度(ラジアン)の差
#     P = np.mean([lat0, lat1])
    P = np.mean([lat0, lat1], axis=0)    # 配列用 debug
    Rx = 6378137.000        # WGS84 長半径(赤道半径)
    Ry = 6356752.314245     # WGS84 短半径(極半径)
    
    E = np.sqrt((Rx**2 - Ry**2) / Rx**2)    # 離心率
    W = np.sqrt(1-(E**2)*((np.sin(P))**2))
    M = Rx*(1-(E**2)) / W**3    # 子午線曲率半径
    N = Rx / W                  # 卯酉線曲率半径
    D = np.sqrt(((Dy*M)**2) + ((Dx*N*np.cos(P))**2))
    return D